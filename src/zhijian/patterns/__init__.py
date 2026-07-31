"""智检 (Zhijian) - 检测模式系统

合并 AI-SLOP-Detector 和 sloppylint 的所有检测规则，共 39 个模式。
"""

from __future__ import annotations

from zhijian.patterns.base import Axis, BasePattern, Issue, Severity
from zhijian.patterns.registry import PatternRegistry

__all__ = [
    "BasePattern",
    "Issue",
    "Severity",
    "Axis",
    "PatternRegistry",
    "get_all_patterns",
]


def get_all_patterns(
    god_function_config: dict | None = None,
    nested_complexity_config: dict | None = None,
    phantom_import_allowlist: list | None = None,
) -> list[BasePattern]:
    """获取所有检测规则。

    合并了两个项目的检测能力：
    - AI-SLOP-Detector: 结构、占位符、幻觉、跨语言、复杂度 (27 个)
    - sloppylint: 噪音、风格、假设 (10 个新增)

    Args:
        god_function_config: 上帝函数阈值配置
        nested_complexity_config: 嵌套复杂度配置
        phantom_import_allowlist: 幻觉导入白名单
    """
    # === 来自 AI-SLOP-Detector 的模式 ===
    from zhijian.patterns.cross_language import (
        CSharpLengthPattern,
        GoPrintPattern,
        JavaEqualsPattern,
        JavaScriptPushPattern,
        PHPStrlenPattern,
        RubyEachPattern,
    )
    from zhijian.patterns.placeholder import (
        EllipsisPlaceholderPattern,
        EmptyExceptPattern,
        FixmeCommentPattern,
        HackCommentPattern,
        InterfaceOnlyClassPattern,
        NotImplementedPattern,
        PassPlaceholderPattern,
        ReturnConstantStubPattern,
        ReturnNonePlaceholderPattern,
        TodoCommentPattern,
        XXXCommentPattern,
    )
    from zhijian.patterns.python_clones import (
        ExactDuplicatePairPattern,
        FunctionClonePattern,
    )
    from zhijian.patterns.python_complexity import (
        DeadCodePattern,
        DeepNestingPattern,
        GodFunctionPattern,
        NestedComplexityPattern,
    )
    from zhijian.patterns.python_imports import PhantomImportPattern
    from zhijian.patterns.python_lint import LintEscapePattern
    from zhijian.patterns.python_naming import PlaceholderVariableNamingPattern
    from zhijian.patterns.structural import (
        BareExceptPattern,
        GlobalStatementPattern,
        MutableDefaultArgPattern,
        StarImportPattern,
    )

    # === 来自 sloppylint 的新增模式 ===
    from zhijian.patterns.noise import NOISE_PATTERNS
    from zhijian.patterns.style import STYLE_PATTERNS
    from zhijian.patterns.assumption import ASSUMPTION_PATTERNS

    # === 智检新增的安全检测模式 ===
    from zhijian.patterns.security import SECURITY_PATTERNS

    return [
        # Structural (Critical/High) - 来自 AI-SLOP-Detector
        BareExceptPattern(),
        MutableDefaultArgPattern(),
        StarImportPattern(),
        GlobalStatementPattern(),
        # Placeholder (Critical/High/Medium) - 来自 AI-SLOP-Detector
        EmptyExceptPattern(),
        NotImplementedPattern(),
        PassPlaceholderPattern(),
        EllipsisPlaceholderPattern(),
        HackCommentPattern(),
        ReturnNonePlaceholderPattern(),
        ReturnConstantStubPattern(),
        TodoCommentPattern(),
        FixmeCommentPattern(),
        InterfaceOnlyClassPattern(),
        XXXCommentPattern(),
        # Cross-language (High) - 来自 AI-SLOP-Detector
        JavaScriptPushPattern(),
        JavaEqualsPattern(),
        RubyEachPattern(),
        GoPrintPattern(),
        CSharpLengthPattern(),
        PHPStrlenPattern(),
        # Python Advanced - 来自 AI-SLOP-Detector
        GodFunctionPattern(
            complexity_threshold=int((god_function_config or {}).get("complexity_threshold", 10)),
            lines_threshold=int((god_function_config or {}).get("lines_threshold", 50)),
            domain_overrides=(god_function_config or {}).get("domain_overrides", []),
        ),
        DeadCodePattern(),
        DeepNestingPattern(),
        NestedComplexityPattern(
            depth_threshold=int((nested_complexity_config or {}).get("depth_threshold", 4)),
            cc_threshold=int((nested_complexity_config or {}).get("cc_threshold", 5)),
            domain_overrides=(nested_complexity_config or {}).get("domain_overrides", []),
        ),
        LintEscapePattern(),
        PhantomImportPattern(allowlist=phantom_import_allowlist or []),
        ExactDuplicatePairPattern(),
        FunctionClonePattern(),
        PlaceholderVariableNamingPattern(),
        # === 以下来自 sloppylint，新增 10 个模式 ===
        # 噪音检测 (Noise) - 4 个
        *NOISE_PATTERNS,
        # 风格检测 (Style) - 4 个
        *STYLE_PATTERNS,
        # 假设检测 (Assumption) - 1 个
        *ASSUMPTION_PATTERNS,
        # === 安全检测 (Security) - 2 个，智检新增 ===
        *SECURITY_PATTERNS,
    ]
