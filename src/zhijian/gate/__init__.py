"""SNP-compatible gate module for slop analysis."""

from zhijian.gate.models import (
    GateMode,
    GateResult,
    GateThresholds,
    GateVerdict,
    QuarantineRecord,
)
from zhijian.gate.slop_gate import SlopGate, SlopGateDecision

__all__ = [
    "SlopGate",
    "SlopGateDecision",
    "GateMode",
    "GateVerdict",
    "GateThresholds",
    "QuarantineRecord",
    "GateResult",
]
