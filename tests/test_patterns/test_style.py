"""风格检测模式的测试用例"""

import ast
from pathlib import Path

import pytest

from zhijian.patterns.style.overconfident_comment import OverconfidentComment
from zhijian.patterns.style.hedging_comment import HedgingComment
from zhijian.patterns.style.apologetic_comment import ApologeticComment
from zhijian.patterns.style.single_method_class import SingleMethodClass


class TestOverconfidentComment:
    """测试过度自信注释检测"""

    def test_detects_obviously(self):
        pattern = OverconfidentComment()
        content = "# obviously this works\nx = 1"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "overconfident_comment"

    def test_detects_clearly(self):
        pattern = OverconfidentComment()
        content = "# clearly the answer\nreturn 42"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_ignores_normal_comment(self):
        pattern = OverconfidentComment()
        content = "# calculate the result\nx = compute()"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0


class TestHedgingComment:
    """测试犹豫不决注释检测"""

    def test_detects_should_work(self):
        pattern = HedgingComment()
        content = "# should work\nx = do_something()"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].severity.value == "high"

    def test_detects_hopefully(self):
        pattern = HedgingComment()
        content = "# hopefully this fixes it\nfix_bug()"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_detects_i_think(self):
        pattern = HedgingComment()
        content = "# i think this is correct\nreturn val"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_ignores_normal_comment(self):
        pattern = HedgingComment()
        content = "# validate input\ncheck(data)"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0


class TestApologeticComment:
    """测试道歉式注释检测"""

    def test_detects_sorry(self):
        pattern = ApologeticComment()
        content = "# sorry for the hack\nx = workaround()"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_detects_hack(self):
        pattern = ApologeticComment()
        content = "# hack: temporary fix\nfix_it()"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_ignores_normal_comment(self):
        pattern = ApologeticComment()
        content = "# implement the algorithm\ncompute()"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0


class TestSingleMethodClass:
    """测试单方法类检测"""

    def test_detects_single_method_class(self):
        pattern = SingleMethodClass()
        content = """
class Processor:
    def __init__(self):
        self.data = []

    def process(self):
        return self.data
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert "Processor" in issues[0].message

    def test_ignores_multi_method_class(self):
        pattern = SingleMethodClass()
        content = """
class Processor:
    def __init__(self):
        self.data = []

    def process(self):
        return self.data

    def validate(self):
        return True
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0

    def test_ignores_protocol_class(self):
        pattern = SingleMethodClass()
        content = """
from typing import Protocol

class MyProtocol(Protocol):
    def method(self) -> None:
        ...
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0

    def test_ignores_dataclass(self):
        pattern = SingleMethodClass()
        content = """
from dataclasses import dataclass

@dataclass
class Config:
    name: str

    def validate(self):
        return bool(self.name)
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0
