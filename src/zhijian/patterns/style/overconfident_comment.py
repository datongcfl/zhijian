"""风格检测：过度自信注释检测器

检测 AI 生成的过度自信注释，这类注释往往暗示代码未经充分验证。
例如：
- # obviously, this works
- # clearly the answer is 42
- # simply do X
"""

import re
from zhijian.patterns.base import RegexPattern, Severity, Axis


class OverconfidentComment(RegexPattern):
    """检测过度自信的注释"""

    id = "overconfident_comment"
    severity = Severity.MEDIUM
    axis = Axis.STYLE
    message = "Overconfident comment - verify claim before shipping"
    pattern = re.compile(
        r"#\s*(obviously|clearly|simply|just|easy|trivial|basically|of course|naturally)\b",
        re.IGNORECASE,
    )
