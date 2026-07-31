"""风格检测：道歉式注释检测器

检测 AI 生成的道歉式注释，这类注释暗示代码质量有问题。
例如：
- # sorry for the hack
- # this is ugly but it works
- # bad code, I know
"""

import re
from zhijian.patterns.base import RegexPattern, Severity, Axis


class ApologeticComment(RegexPattern):
    """检测道歉式的注释"""

    id = "apologetic_comment"
    severity = Severity.MEDIUM
    axis = Axis.STYLE
    message = "Apologetic comment - fix the issue instead of apologizing"
    pattern = re.compile(
        r"#\s*(sorry|hack|hacky|ugly|bad|terrible|awful|gross|yuck|forgive)\b", re.IGNORECASE
    )
