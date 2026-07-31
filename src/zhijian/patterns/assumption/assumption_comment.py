"""假设检测：假设性注释检测器

检测 AI 生成的假设性注释，这类注释暗示代码基于未验证的假设。
例如：
- # assuming the input is valid
- # presumably this works
- # apparently this is the right way
"""

import re
from zhijian.patterns.base import RegexPattern, Severity, Axis


class AssumptionComment(RegexPattern):
    """检测假设性的注释"""

    id = "assumption_comment"
    severity = Severity.HIGH
    axis = Axis.QUALITY
    message = "Assumption in code - verify before shipping"
    pattern = re.compile(
        r"#\s*(assuming|assumes?|presumably|apparently|i think|we think|should be|might be)\b",
        re.IGNORECASE,
    )
