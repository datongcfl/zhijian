"""风格检测模式集合

这些模式检测 AI 生成代码中的风格问题：
- 过度自信注释
- 犹豫不决注释
- 道歉式注释
- 单方法类（应该用函数代替）
"""

from zhijian.patterns.style.overconfident_comment import OverconfidentComment
from zhijian.patterns.style.hedging_comment import HedgingComment
from zhijian.patterns.style.apologetic_comment import ApologeticComment
from zhijian.patterns.style.single_method_class import SingleMethodClass

STYLE_PATTERNS = [
    OverconfidentComment(),
    HedgingComment(),
    ApologeticComment(),
    SingleMethodClass(),
]

__all__ = [
    "OverconfidentComment",
    "HedgingComment",
    "ApologeticComment",
    "SingleMethodClass",
    "STYLE_PATTERNS",
]
