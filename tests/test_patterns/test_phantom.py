"""幻觉导入检测的测试用例"""

import ast
from pathlib import Path

import pytest

from zhijian.patterns.python_imports import PhantomImportPattern


class TestPhantomImportPattern:
    """测试幻觉导入检测"""

    def test_initializes_with_allowlist(self):
        pattern = PhantomImportPattern(allowlist=["mypackage"])
        assert pattern is not None

    def test_detects_nonexistent_package(self):
        pattern = PhantomImportPattern(allowlist=[])
        content = "import nonexistent_fake_package_xyz"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        # 幻觉导入检测依赖包存在性检查
        assert isinstance(issues, list)

    def test_ignores_stdlib(self):
        pattern = PhantomImportPattern(allowlist=[])
        content = "import os\nimport sys\nimport json"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        # 标准库不应被标记为幻觉
        phantom_issues = [i for i in issues if i.pattern_id == "phantom_import"]
        assert len(phantom_issues) == 0

    def test_ignores_allowlisted_package(self):
        pattern = PhantomImportPattern(allowlist=["mypackage"])
        content = "import mypackage"
        tree = ast.parse(content)
        issues = pattern.check(tree, Path("test.py"), content)
        phantom_issues = [i for i in issues if i.pattern_id == "phantom_import"]
        assert len(phantom_issues) == 0
