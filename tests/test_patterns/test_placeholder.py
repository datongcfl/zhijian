"""占位符检测的测试用例"""

import ast
from pathlib import Path

import pytest

from zhijian.patterns.placeholder import (
    EmptyExceptPattern,
    PassPlaceholderPattern,
    EllipsisPlaceholderPattern,
    NotImplementedPattern,
    ReturnNonePlaceholderPattern,
    TodoCommentPattern,
    FixmeCommentPattern,
    HackCommentPattern,
)


class TestEmptyExceptPattern:
    """测试空 except 块检测"""

    def test_detects_empty_except(self):
        pattern = EmptyExceptPattern()
        content = """
try:
    risky()
except ValueError:
    pass
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "empty_except"

    def test_ignores_except_with_code(self):
        pattern = EmptyExceptPattern()
        content = """
try:
    risky()
except ValueError as e:
    logger.error(e)
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0


class TestPassPlaceholderPattern:
    """测试 pass 占位符检测"""

    def test_detects_pass_function(self):
        pattern = PassPlaceholderPattern()
        content = """
def validate(data):
    pass
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "pass_placeholder"

    def test_detects_pass_with_docstring(self):
        pattern = PassPlaceholderPattern()
        content = '''
def validate(data):
    """Validate the input data."""
    pass
'''
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_ignores_implementation(self):
        pattern = PassPlaceholderPattern()
        content = """
def validate(data):
    return bool(data)
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0


class TestEllipsisPlaceholderPattern:
    """测试省略号占位符检测"""

    def test_detects_ellipsis_function(self):
        pattern = EllipsisPlaceholderPattern()
        content = """
def process(data):
    ...
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "ellipsis_placeholder"

    def test_ignores_implementation(self):
        pattern = EllipsisPlaceholderPattern()
        content = """
def process(data):
    return data.transform()
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0


class TestNotImplementedPattern:
    """测试 NotImplementedError 检测"""

    def test_detects_not_implemented(self):
        pattern = NotImplementedPattern()
        content = """
def abstract_method(self):
    raise NotImplementedError
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "not_implemented"

    def test_detects_not_implemented_with_msg(self):
        pattern = NotImplementedPattern()
        content = '''
def abstract_method(self):
    raise NotImplementedError("Subclass must implement")
'''
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1


class TestReturnNonePlaceholderPattern:
    """测试 return None 占位符检测"""

    def test_detects_return_none(self):
        pattern = ReturnNonePlaceholderPattern()
        content = """
def get_value():
    return None
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "return_none_placeholder"


class TestTodoCommentPattern:
    """测试 TODO 注释检测"""

    def test_detects_todo(self):
        pattern = TodoCommentPattern()
        content = """
# TODO: implement this
def process():
    pass
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "todo_comment"

    def test_detects_todo_with_description(self):
        pattern = TodoCommentPattern()
        content = """
# TODO: add error handling
x = risky_call()
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1


class TestFixmeCommentPattern:
    """测试 FIXME 注释检测"""

    def test_detects_fixme(self):
        pattern = FixmeCommentPattern()
        content = """
# FIXME: this is broken
def broken():
    pass
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "fixme_comment"


class TestHackCommentPattern:
    """测试 HACK 注释检测"""

    def test_detects_hack(self):
        pattern = HackCommentPattern()
        content = """
# HACK: temporary workaround
def workaround():
    pass
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "hack_comment"
