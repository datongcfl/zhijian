#!/usr/bin/env python3
"""
ML-based Slop Classification Module
====================================
Machine learning models for slop detection with ensemble approach.

Models:
1. RandomForest - Baseline ensemble model
2. XGBoost - Gradient boosting for better accuracy
3. Ensemble - Combines multiple models for maximum accuracy

Performance Targets:
- Accuracy: >90%
- Precision: >85% (minimize false positives)
- Recall: >95% (catch most slop)
- F1-Score: >90%

Author: Flamehaven Labs
Version: 2.2.0
Date: 2026-01-08
"""

import hashlib
import hmac
import json
import logging
import os
import pickle
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, Tuple

import numpy as np

try:
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import (
        accuracy_score,
        f1_score,
        precision_score,
        recall_score,
    )
    from sklearn.model_selection import train_test_split

    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

try:
    import xgboost as xgb

    XGBOOST_AVAILABLE = True
except ImportError:
    XGBOOST_AVAILABLE = False

logger = logging.getLogger(__name__)

# Signing key for model files. Override via ZHIJIAN_MODEL_KEY to rotate.
# The HMAC envelope detects corruption/tampering; it is not a substitute for
# trusting the model source. Only load models you produced or verified.
_MODEL_FORMAT = "zhijian-model-v1"
_MODEL_SIGNING_KEY = os.environ.get("ZHIJIAN_MODEL_KEY", "zhijian-model-v1").encode("utf-8")


def _sign_model(payload: bytes) -> str:
    """Return an HMAC-SHA256 hex signature over a pickled payload."""
    return hmac.new(_MODEL_SIGNING_KEY, payload, hashlib.sha256).hexdigest()


@dataclass
class ModelMetrics:
    """Model performance metrics."""

    accuracy: float
    precision: float
    recall: float
    f1_score: float

    def __str__(self) -> str:
        return (
            f"Accuracy: {self.accuracy:.3f}, "
            f"Precision: {self.precision:.3f}, "
            f"Recall: {self.recall:.3f}, "
            f"F1: {self.f1_score:.3f}"
        )


class SlopClassifier:
    """ML-based slop classifier with ensemble support."""

    FEATURE_NAMES = [
        # Core metrics (v2.8.0 formula)
        "ldr_score",
        "inflation_score",  # renamed from bcr_score; density-based v2.8.0
        "ddc_score",
        # Pattern severity counts
        "pattern_count_critical",
        "pattern_count_high",
        "pattern_count_medium",
        "pattern_count_low",
        # v2.8.0: structural patterns
        "god_function_count",
        "dead_code_count",
        "deep_nesting_count",
        # Code structure
        "avg_complexity",
        "cross_language_patterns",
        "hallucination_count",
        "total_lines",
        "logic_lines",
        "empty_lines",
    ]

    def __init__(self, model_type: str = "ensemble"):
        """
        Initialize classifier.

        Args:
            model_type: "random_forest", "xgboost", or "ensemble"
        """
        if not SKLEARN_AVAILABLE:
            raise ImportError("scikit-learn not installed. Run: pip install scikit-learn")

        self.model_type = model_type
        self.rf_model: Optional[RandomForestClassifier] = None
        self.xgb_model: Optional[xgb.XGBClassifier] = None
        self.is_trained = False

    def load_dataset(self, dataset_path: Path) -> Tuple[np.ndarray, np.ndarray]:
        """Load training dataset from JSON file."""
        with open(dataset_path, "r") as f:
            data = json.load(f)

        # Extract features and labels
        good_examples = data["good"]
        bad_examples = data["bad"]

        features = []
        labels = []

        for example in good_examples:
            features.append([example[feat] for feat in self.FEATURE_NAMES])
            labels.append(0)  # Clean

        for example in bad_examples:
            features.append([example[feat] for feat in self.FEATURE_NAMES])
            labels.append(1)  # Slop

        return np.array(features), np.array(labels)

    def train_random_forest(
        self, features_train: np.ndarray, labels_train: np.ndarray
    ) -> RandomForestClassifier:
        """Train RandomForest classifier."""
        logger.info("Training RandomForest...")

        rf = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=2,
            class_weight="balanced",
            random_state=42,
            n_jobs=-1,
        )

        rf.fit(features_train, labels_train)

        # Feature importance
        feature_importance = sorted(
            zip(self.FEATURE_NAMES, rf.feature_importances_), key=lambda x: x[1], reverse=True
        )
        logger.info("Top 5 features:")
        for feat, importance in feature_importance[:5]:
            logger.info(f"  {feat}: {importance:.3f}")

        return rf

    def train_xgboost(
        self, features_train: np.ndarray, labels_train: np.ndarray
    ) -> Optional[xgb.XGBClassifier]:
        """Train XGBoost classifier."""
        if not XGBOOST_AVAILABLE:
            logger.warning("XGBoost not available, skipping")
            return None

        logger.info("Training XGBoost...")

        xgb_model = xgb.XGBClassifier(
            n_estimators=100,
            max_depth=6,
            learning_rate=0.1,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=42,
            n_jobs=-1,
        )

        xgb_model.fit(features_train, labels_train)

        return xgb_model

    def train(self, dataset_path: Path, test_size: float = 0.2) -> Dict[str, ModelMetrics]:
        """
        Train model(s) on dataset.

        Args:
            dataset_path: Path to training data JSON
            test_size: Fraction of data for testing

        Returns:
            Dict mapping model name to metrics
        """
        logger.info(f"Loading dataset from {dataset_path}...")
        features, labels = self.load_dataset(dataset_path)

        logger.info(
            f"Dataset: {len(features)} examples "
            f"({sum(labels == 0)} clean, {sum(labels == 1)} slop)"
        )

        # Split data
        features_train, features_test, labels_train, labels_test = train_test_split(
            features, labels, test_size=test_size, random_state=42, stratify=labels
        )

        logger.info(f"Train: {len(features_train)}, Test: {len(features_test)}")

        metrics = {}

        # Train RandomForest
        self.rf_model = self.train_random_forest(features_train, labels_train)
        rf_metrics = self.evaluate(self.rf_model, features_test, labels_test)
        metrics["random_forest"] = rf_metrics
        logger.info(f"RandomForest: {rf_metrics}")

        # Train XGBoost
        if self.model_type in ["xgboost", "ensemble"] and XGBOOST_AVAILABLE:
            self.xgb_model = self.train_xgboost(features_train, labels_train)
            if self.xgb_model:
                xgb_metrics = self.evaluate(self.xgb_model, features_test, labels_test)
                metrics["xgboost"] = xgb_metrics
                logger.info(f"XGBoost: {xgb_metrics}")

        # Evaluate ensemble
        if self.model_type == "ensemble" and self.xgb_model:
            ensemble_metrics = self.evaluate_ensemble(features_test, labels_test)
            metrics["ensemble"] = ensemble_metrics
            logger.info(f"Ensemble: {ensemble_metrics}")

        self.is_trained = True
        logger.info("Training complete!")

        return metrics

    def evaluate(self, model, features_test: np.ndarray, labels_test: np.ndarray) -> ModelMetrics:
        """Evaluate model on test set."""
        labels_pred = model.predict(features_test)

        return ModelMetrics(
            accuracy=accuracy_score(labels_test, labels_pred),
            precision=precision_score(labels_test, labels_pred, zero_division=0),
            recall=recall_score(labels_test, labels_pred, zero_division=0),
            f1_score=f1_score(labels_test, labels_pred, zero_division=0),
        )

    def evaluate_ensemble(self, features_test: np.ndarray, labels_test: np.ndarray) -> ModelMetrics:
        """Evaluate ensemble (voting) on test set."""
        rf_pred = self.rf_model.predict(features_test)
        xgb_pred = self.xgb_model.predict(features_test)

        # Voting: majority wins
        ensemble_pred = ((rf_pred + xgb_pred) >= 1).astype(int)

        return ModelMetrics(
            accuracy=accuracy_score(labels_test, ensemble_pred),
            precision=precision_score(labels_test, ensemble_pred, zero_division=0),
            recall=recall_score(labels_test, ensemble_pred, zero_division=0),
            f1_score=f1_score(labels_test, ensemble_pred, zero_division=0),
        )

    def predict(self, features: Dict[str, float]) -> Tuple[float, float]:
        """
        Predict slop probability for a file.

        Args:
            features: Dictionary of feature name -> value

        Returns:
            (slop_probability, confidence)
        """
        if not self.is_trained:
            raise RuntimeError("Model not trained. Call train() first.")

        # Convert features to vector
        x = np.array([[features[feat] for feat in self.FEATURE_NAMES]])

        if self.model_type == "random_forest":
            proba = self.rf_model.predict_proba(x)[0]
            return proba[1], max(proba)

        elif self.model_type == "xgboost":
            if not self.xgb_model:
                raise RuntimeError("XGBoost model not available")
            proba = self.xgb_model.predict_proba(x)[0]
            return proba[1], max(proba)

        elif self.model_type == "ensemble":
            rf_proba = self.rf_model.predict_proba(x)[0]
            xgb_proba = self.xgb_model.predict_proba(x)[0] if self.xgb_model else rf_proba

            # Weighted average
            ensemble_proba = 0.5 * rf_proba + 0.5 * xgb_proba

            return ensemble_proba[1], max(ensemble_proba)

        else:
            raise ValueError(f"Unknown model type: {self.model_type}")

    def save(self, output_path: Path):
        """Save trained model to disk.

        Writes an HMAC-signed envelope so that :meth:`load` can detect
        corruption or tampering before deserializing the payload.
        """
        if not self.is_trained:
            raise RuntimeError("Model not trained")

        model_data = {
            "model_type": self.model_type,
            "rf_model": self.rf_model,
            "xgb_model": self.xgb_model,
            "feature_names": self.FEATURE_NAMES,
        }

        payload = pickle.dumps(model_data)
        envelope = {
            "format": _MODEL_FORMAT,
            "signature": _sign_model(payload),
            "payload": payload,
        }
        with open(output_path, "wb") as f:
            pickle.dump(envelope, f)

        logger.info(f"Model saved to {output_path}")

    def load(self, model_path: Path):
        """Load trained model from disk.

        Refuses to deserialize the payload unless its HMAC signature matches,
        and validates the resulting structure. Legacy (unsigned) model files are
        accepted only for backward compatibility after structural validation.
        """
        with open(model_path, "rb") as f:
            data = pickle.load(f)

        legacy = not (isinstance(data, dict) and data.get("format") == _MODEL_FORMAT)
        if legacy:
            logger.warning(
                "Loading legacy unsigned model %s; re-save it to enable "
                "tamper detection.",
                model_path,
            )
            model_data = data
        else:
            expected = _sign_model(data["payload"])
            if not hmac.compare_digest(expected, data["signature"]):
                raise ValueError(
                    f"Model signature mismatch for {model_path}: "
                    "file may be corrupted or tampered with"
                )
            model_data = pickle.loads(data["payload"])

        # Structural validation: reject foreign/broken model files early.
        if not isinstance(model_data, dict):
            raise ValueError("Invalid model file: expected a model dict")
        if set(model_data) != {"model_type", "rf_model", "xgb_model", "feature_names"}:
            raise ValueError("Invalid model file: unexpected structure")
        if model_data["model_type"] not in {"random_forest", "xgboost", "ensemble"}:
            raise ValueError(f"Invalid model type: {model_data['model_type']}")
        if list(model_data["feature_names"]) != list(self.FEATURE_NAMES):
            raise ValueError(
                "Model feature_names do not match this classifier version; "
                "retrain the model"
            )

        self.model_type = model_data["model_type"]
        self.rf_model = model_data["rf_model"]
        self.xgb_model = model_data["xgb_model"]
        self.is_trained = True

        logger.info(f"Model loaded from {model_path}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Example usage
    classifier = SlopClassifier(model_type="ensemble")

    # Train (requires dataset)
    dataset_path = Path("data/training/training_data.json")
    if dataset_path.exists():
        metrics = classifier.train(dataset_path)

        print("\n[+] Training Results:")
        for model_name, model_metrics in metrics.items():
            print(f"  {model_name}: {model_metrics}")

        # Save model
        classifier.save(Path("models/slop_classifier.pkl"))
    else:
        print(f"[-] Dataset not found: {dataset_path}")
        print("Run training_data.py first to collect data")
