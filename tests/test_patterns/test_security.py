"""安全检测模式的测试用例"""

import ast
from pathlib import Path

import pytest

from zhijian.patterns.security.timing_attack import TimingAttackPattern
from zhijian.patterns.security.error_leakage import ErrorLeakagePattern


class TestTimingAttackPattern:
    """测试时序攻击漏洞检测"""

    def test_detects_password_comparison(self):
        pattern = TimingAttackPattern()
        content = """
if password == config.PASSWORD:
    return True
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "timing_attack"
        assert issues[0].severity.value == "high"

    def test_detects_secret_comparison(self):
        pattern = TimingAttackPattern()
        content = """
if secret == expected_secret:
    do_something()
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_detects_token_comparison(self):
        pattern = TimingAttackPattern()
        content = """
if token == stored_token:
    return authorized
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_detects_api_key_comparison(self):
        pattern = TimingAttackPattern()
        content = """
if api_key == request.headers.get("X-API-Key"):
    pass
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_ignores_normal_comparison(self):
        pattern = TimingAttackPattern()
        content = """
if x == 42:
    pass
if name == "admin":
    pass
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0

    def test_ignores_secrets_compare_digest(self):
        pattern = TimingAttackPattern()
        content = """
import secrets
if secrets.compare_digest(password, expected):
    pass
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0


class TestErrorLeakagePattern:
    """测试错误信息泄露检测"""

    def test_detects_str_e_in_jsonify(self):
        pattern = ErrorLeakagePattern()
        content = """
try:
    do_something()
except Exception as e:
    return jsonify({"error": str(e)}), 500
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1
        assert issues[0].pattern_id == "error_leakage"

    def test_detects_str_e_in_return(self):
        pattern = ErrorLeakagePattern()
        content = """
try:
    process()
except Exception as e:
    return {"message": str(e)}
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 1

    def test_ignores_generic_error_message(self):
        pattern = ErrorLeakagePattern()
        content = """
try:
    process()
except Exception as e:
    return jsonify({"error": "Internal server error"}), 500
"""
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        assert len(issues) == 0
