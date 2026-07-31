"""风格检测：单方法类检测器

检测只有一个公开方法的类，这类类通常应该用函数代替。
这是 AI 生成代码中常见的过度工程化模式。
"""

from __future__ import annotations

import ast
from pathlib import Path
from typing import Optional

from zhijian.patterns.base import ASTPattern, Issue, Severity, Axis


class SingleMethodClass(ASTPattern):
    """检测只有一个公开方法的类"""

    id = "single_method_class"
    severity = Severity.HIGH
    axis = Axis.STRUCTURE
    message = "Single-method class could be a function instead"

    SPECIAL_METHODS = {"__init__", "__new__", "__del__", "__repr__", "__str__"}

    # 接口/协议基类，单方法在这些类中是有效的
    INTERFACE_BASES = {
        "Protocol",
        "ABC",
        "ABCMeta",
        "Interface",
        "Generic",
        "TypedDict",
        "NamedTuple",
        "Enum",
        "IntEnum",
        "StrEnum",
        "Flag",
        "IntFlag",
        "Exception",
        "BaseException",
    }

    # 特殊装饰器，使单方法类变得合理
    SPECIAL_DECORATORS = {
        "dataclass",
        "dataclasses.dataclass",
        "attrs",
        "attr.s",
        "attr.attrs",
        "define",
        "attr.define",
        "frozen",
        "attr.frozen",
        "runtime_checkable",
        "typing.runtime_checkable",
        "final",
        "typing.final",
    }

    def check_node(
        self,
        node: ast.AST,
        file: Path,
        content: str,
    ) -> Optional[Issue | list[Issue]]:
        if not isinstance(node, ast.ClassDef):
            return None

        # 跳过 Protocol/ABC/接口类
        if self._is_interface_class(node):
            return None

        # 跳过有特殊装饰器的类
        if self._has_special_decorator(node):
            return None

        # 跳过有非平凡基类的类（属于继承体系）
        if self._has_significant_base(node):
            return None

        # 统计非特殊方法
        methods = [
            n
            for n in node.body
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
            and n.name not in self.SPECIAL_METHODS
            and not n.name.startswith("_")
        ]

        # 统计特殊方法
        special = [
            n
            for n in node.body
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
            and n.name in self.SPECIAL_METHODS
        ]

        # 如果只有一个公开方法（除 __init__ 外），标记
        if len(methods) == 1 and len(special) <= 1:
            return self.create_issue_from_node(
                node,
                file,
                code=f"class {node.name}: # single method: {methods[0].name}",
                message=f"Class '{node.name}' has only one method '{methods[0].name}' - consider using a function",
            )

        return None

    def _is_interface_class(self, node: ast.ClassDef) -> bool:
        """检查类是否继承自 Protocol、ABC 或类似的接口基类。"""
        for base in node.bases:
            base_name = self._get_base_name(base)
            if base_name in self.INTERFACE_BASES:
                return True
        # 检查关键字参数（如 class Foo(metaclass=ABCMeta)）
        for keyword in node.keywords:
            if keyword.arg == "metaclass":
                meta_name = self._get_base_name(keyword.value)
                if meta_name in self.INTERFACE_BASES:
                    return True
        return False

    def _has_significant_base(self, node: ast.ClassDef) -> bool:
        """检查类是否继承自非平凡基类（属于继承体系）。"""
        if not node.bases:
            return False
        for base in node.bases:
            base_name = self._get_base_name(base)
            # 如果有任何非 object 的基类，说明它属于继承体系
            if base_name and base_name not in ("object",):
                return True
        return False

    def _get_base_name(self, base: ast.AST) -> Optional[str]:
        """从 AST 节点提取基类名称。"""
        if isinstance(base, ast.Name):
            return base.id
        elif isinstance(base, ast.Attribute):
            return base.attr
        elif isinstance(base, ast.Subscript):
            # 对于 Generic[T]、Protocol[T] 等
            return self._get_base_name(base.value)
        return None

    def _has_special_decorator(self, node: ast.ClassDef) -> bool:
        """检查类是否有使单方法变得合理的装饰器。"""
        for dec in node.decorator_list:
            dec_name = self._get_decorator_name(dec)
            if dec_name in self.SPECIAL_DECORATORS:
                return True
        return False

    def _get_decorator_name(self, dec: ast.AST) -> Optional[str]:
        """从 AST 节点提取装饰器名称。"""
        if isinstance(dec, ast.Name):
            return dec.id
        elif isinstance(dec, ast.Attribute):
            # 对于 dataclasses.dataclass 等
            parts = []
            current = dec
            while isinstance(current, ast.Attribute):
                parts.append(current.attr)
                current = current.value
            if isinstance(current, ast.Name):
                parts.append(current.id)
            return ".".join(reversed(parts))
        elif isinstance(dec, ast.Call):
            return self._get_decorator_name(dec.func)
        return None
