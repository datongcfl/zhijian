"""噪音检测模式的测试用例"""

import ast
from pathlib import Path

import pytest

from zhijian.patterns.noise.redundant_comment import RedundantComment
from zhijian.patterns.noise.empty_docstring import EmptyDocstring
from zhijian.patterns.noise.generic_docstring import GenericDocstring
from zhijian.patterns.noise.changelog_comment import ChangelogComment


class TestRedundantComment:
    """测试冗余注释检测"""

    def test_detects_increment_comment(self):
        pattern = RedundantComment()
        content = "# increment counter\nx += 1"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "redundant_comment"

    def test_detects_return_comment(self):
        pattern = RedundantComment()
        content = "# return value\nreturn x"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_ignores_normal_comment(self):
        pattern = RedundantComment()
        content = "# this is a helpful comment\nx += 1"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0


class TestEmptyDocstring:
    """测试空文档字符串检测"""

    def test_detects_empty_docstring(self):
        pattern = EmptyDocstring()
        content = '""""""'
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_detects_todo_docstring(self):
        pattern = EmptyDocstring()
        content = '"""TODO: add docs"""'
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_ignores_real_docstring(self):
        pattern = EmptyDocstring()
        content = '"""This function does something useful."""'
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0


class TestGenericDocstring:
    """测试通用文档字符串检测"""

    def test_detects_generic_docstring(self):
        pattern = GenericDocstring()
        content = '"""This function does stuff."""'
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_ignores_specific_docstring(self):
        pattern = GenericDocstring()
        content = '"""Calculate the sum of two numbers."""'
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0


class TestChangelogComment:
    """测试版本历史注释检测"""

    def test_detects_changelog_comment(self):
        pattern = ChangelogComment()
        content = "# v1.2.3 - added new feature"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_ignores_normal_comment(self):
        pattern = ChangelogComment()
        content = "# This is a regular comment"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0
