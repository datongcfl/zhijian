"""假设检测模式集合

这些模式检测 AI 生成代码中的假设性问题：
- 假设性注释（未经验证的假设）
"""

from zhijian.patterns.assumption.assumption_comment import AssumptionComment

ASSUMPTION_PATTERNS = [
    AssumptionComment(),
]

__all__ = [
    "AssumptionComment",
    "ASSUMPTION_PATTERNS",
]
