"""假设检测模式的测试用例"""

import ast
from pathlib import Path

import pytest

from zhijian.patterns.assumption.assumption_comment import AssumptionComment


class TestAssumptionComment:
    """测试假设性注释检测"""

    def test_detects_assuming(self):
        pattern = AssumptionComment()
        content = "# assuming input is valid\nprocess(data)"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "assumption_comment"
        assert issues[0].severity.value == "high"

    def test_detects_presumably(self):
        pattern = AssumptionComment()
        content = "# presumably this works\nresult = compute()"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_detects_i_think(self):
        pattern = AssumptionComment()
        content = "# i think this is right\nreturn value"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_detects_should_be(self):
        pattern = AssumptionComment()
        content = "# should be correct\nx = 42"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_ignores_normal_comment(self):
        pattern = AssumptionComment()
        content = "# validate the input\ncheck(data)"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0
