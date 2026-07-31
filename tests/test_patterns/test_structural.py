"""结构反模式检测的测试用例"""

import ast
from pathlib import Path

import pytest

from zhijian.patterns.structural import (
    BareExceptPattern,
    MutableDefaultArgPattern,
    StarImportPattern,
    GlobalStatementPattern,
)


class TestBareExceptPattern:
    """测试裸 except 检测"""

    def test_detects_bare_except(self):
        pattern = BareExceptPattern()
        content = """
try:
    risky()
except:
    pass
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "bare_except"
        assert issues[0].severity.value == "critical"

    def test_ignores_specific_except(self):
        pattern = BareExceptPattern()
        content = """
try:
    risky()
except ValueError:
    pass
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0


class TestMutableDefaultArgPattern:
    """测试可变默认参数检测"""

    def test_detects_list_default(self):
        pattern = MutableDefaultArgPattern()
        content = """
def process(items=[]):
    items.append(1)
    return items
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "mutable_default_arg"
        assert issues[0].severity.value == "critical"

    def test_detects_dict_default(self):
        pattern = MutableDefaultArgPattern()
        content = """
def configure(config={}):
    return config
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_ignores_none_default(self):
        pattern = MutableDefaultArgPattern()
        content = """
def process(items=None):
    if items is None:
        items = []
    return items
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0


class TestStarImportPattern:
    """测试 star import 检测"""

    def test_detects_star_import(self):
        pattern = StarImportPattern()
        content = "from os import *"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "star_import"

    def test_ignores_normal_import(self):
        pattern = StarImportPattern()
        content = "from os import path"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0


class TestGlobalStatementPattern:
    """测试 global 语句检测"""

    def test_detects_global_statement(self):
        pattern = GlobalStatementPattern()
        content = """
counter = 0

def increment():
    global counter
    counter += 1
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "global_statement"

    def test_ignores_no_global(self):
        pattern = GlobalStatementPattern()
        content = """
def increment(counter):
    return counter + 1
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0
