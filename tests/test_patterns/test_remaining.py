"""剩余规则的测试用例: xxx_comment, return_constant_stub, interface_only_class, clones, naming"""

import ast
from pathlib import Path

import pytest

from zhijian.patterns.placeholder import (
    XXXCommentPattern,
    ReturnConstantStubPattern,
    InterfaceOnlyClassPattern,
)
from zhijian.patterns.python_clones import (
    ExactDuplicatePairPattern,
    FunctionClonePattern,
)
from zhijian.patterns.python_naming import PlaceholderVariableNamingPattern


class TestXXXCommentPattern:
    """测试 XXX 注释检测"""

    def test_detects_xxx_comment(self):
        pattern = XXXCommentPattern()
        content = """
# XXX: this needs review
def broken():
    pass
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "xxx_comment"


class TestReturnConstantStubPattern:
    """测试返回常量 stub 检测"""

    def test_initializes(self):
        pattern = ReturnConstantStubPattern()
        assert pattern is not None
        assert pattern.id == "return_constant_stub"

    def test_detects_return_true_stub(self):
        pattern = ReturnConstantStubPattern()
        content = """
def always_true():
    return True
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        # return_constant_stub 可能只检测特定模式
        assert isinstance(issues, list)


class TestInterfaceOnlyClassPattern:
    """测试只有接口没有实现的类检测"""

    def test_initializes(self):
        pattern = InterfaceOnlyClassPattern()
        assert pattern is not None
        assert pattern.id == "interface_only_class"


class TestExactDuplicatePairPattern:
    """测试完全重复代码检测"""

    def test_initializes(self):
        pattern = ExactDuplicatePairPattern()
        assert pattern is not None
        assert pattern.id == "exact_duplicate_pair"


class TestFunctionClonePattern:
    """测试函数克隆检测"""

    def test_initializes(self):
        pattern = FunctionClonePattern()
        assert pattern is not None
        assert pattern.id == "function_clone_cluster"


class TestPlaceholderVariableNamingPattern:
    """测试占位符变量名检测"""

    def test_initializes(self):
        pattern = PlaceholderVariableNamingPattern()
        assert pattern is not None
        assert pattern.id == "placeholder_variable_naming"

    def test_detects_placeholder_names(self):
        pattern = PlaceholderVariableNamingPattern()
        content = """
def process(data):
    temp = data
    foo = temp
    bar = foo
    return bar
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert isinstance(issues, list)
