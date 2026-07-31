"""跨语言泄漏检测的测试用例"""

import ast
from pathlib import Path

import pytest

from zhijian.patterns.cross_language import (
    JavaScriptPushPattern,
    JavaEqualsPattern,
    RubyEachPattern,
    GoPrintPattern,
    CSharpLengthPattern,
    PHPStrlenPattern,
)


class TestJavaScriptPushPattern:
    """测试 JavaScript .push() 泄漏检测"""

    def test_detects_push_call(self):
        pattern = JavaScriptPushPattern()
        content = """
items = []
items.push(1)
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "js_push"

    def test_ignores_append(self):
        pattern = JavaScriptPushPattern()
        content = """
items = []
items.append(1)
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0


class TestJavaEqualsPattern:
    """测试 Java .equals() 泄漏检测"""

    def test_detects_equals_call(self):
        pattern = JavaEqualsPattern()
        content = """
if a.equals(b):
    pass
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "java_equals"

    def test_ignores_comparison(self):
        pattern = JavaEqualsPattern()
        content = """
if a == b:
    pass
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0


class TestRubyEachPattern:
    """测试 Ruby .each 泄漏检测"""

    def test_detects_each_call(self):
        pattern = RubyEachPattern()
        content = """
items.each(lambda x: print(x))
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "ruby_each"


class TestGoPrintPattern:
    """测试 Go fmt.Println 泄漏检测"""

    def test_detects_fmt_println(self):
        pattern = GoPrintPattern()
        content = """
fmt.Println("hello")
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "go_println"


class TestCSharpLengthPattern:
    """测试 C# .Length 泄漏检测"""

    def test_detects_length_attr(self):
        pattern = CSharpLengthPattern()
        content = """
n = items.Length
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "csharp_length"


class TestPHPStrlenPattern:
    """测试 PHP strlen 泄漏检测"""

    def test_detects_strlen(self):
        pattern = PHPStrlenPattern()
        content = """
n = strlen(text)
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "php_strlen"
