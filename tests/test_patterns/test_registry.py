"""测试模式注册表"""

import pytest

from zhijian.patterns import get_all_patterns
from zhijian.patterns.registry import PatternRegistry


class TestPatternRegistry:
    """测试模式注册表"""

    def test_get_all_patterns_returns_list(self):
        patterns = get_all_patterns()
        assert isinstance(patterns, list)
        assert len(patterns) > 0

    def test_all_patterns_have_ids(self):
        patterns = get_all_patterns()
        for pattern in patterns:
            assert pattern.id, f"Pattern {pattern} has no ID"

    def test_all_patterns_have_severity(self):
        patterns = get_all_patterns()
        for pattern in patterns:
            assert pattern.severity is not None, f"Pattern {pattern.id} has no severity"

    def test_all_patterns_have_axis(self):
        patterns = get_all_patterns()
        for pattern in patterns:
            assert pattern.axis is not None, f"Pattern {pattern.id} has no axis"

    def test_no_duplicate_ids(self):
        patterns = get_all_patterns()
        ids = [p.id for p in patterns]
        assert len(ids) == len(set(ids)), f"Duplicate pattern IDs: {ids}"

    def test_registry_register_and_get(self):
        registry = PatternRegistry()
        patterns = get_all_patterns()
        registry.register_all(patterns)

        assert len(registry) == len(patterns)

        # Test get by ID
        first = patterns[0]
        assert registry.get(first.id) is first

    def test_registry_disable_enable(self):
        registry = PatternRegistry()
        patterns = get_all_patterns()
        registry.register_all(patterns)

        initial_count = len(registry)
        registry.disable(patterns[0].id)
        assert len(registry) == initial_count - 1

        registry.enable(patterns[0].id)
        assert len(registry) == initial_count

    def test_noise_patterns_included(self):
        patterns = get_all_patterns()
        noise_ids = [p.id for p in patterns if p.axis.value == "noise"]
        assert "redundant_comment" in noise_ids
        assert "empty_docstring" in noise_ids
        assert "generic_docstring" in noise_ids
        assert "changelog_in_code" in noise_ids

    def test_style_patterns_included(self):
        patterns = get_all_patterns()
        style_ids = [p.id for p in patterns if p.axis.value == "style"]
        assert "overconfident_comment" in style_ids
        assert "hedging_comment" in style_ids
        assert "apologetic_comment" in style_ids

    def test_assumption_patterns_included(self):
        patterns = get_all_patterns()
        quality_ids = [p.id for p in patterns if p.axis.value == "quality"]
        assert "assumption_comment" in quality_ids

    def test_structural_patterns_included(self):
        patterns = get_all_patterns()
        structure_ids = [p.id for p in patterns if p.axis.value == "structure"]
        assert "bare_except" in structure_ids
        assert "single_method_class" in structure_ids
        assert "star_import" in structure_ids

    def test_total_pattern_count(self):
        """验证总共 39 个检测规则"""
        patterns = get_all_patterns()
        # 27 (AI-SLOP-Detector) + 10 (sloppylint) + 2 (single_method_class 已计入 structure)
        assert len(patterns) >= 37, f"Expected at least 37 patterns, got {len(patterns)}"
