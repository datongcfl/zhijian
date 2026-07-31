"""噪音检测：通用文档字符串检测器

检测无信息量的通用文档字符串。
"""

import re
from zhijian.patterns.base import RegexPattern, Severity, Axis


class GenericDocstring(RegexPattern):
    """检测无信息量的通用文档字符串"""

    id = "generic_docstring"
    severity = Severity.LOW
    axis = Axis.NOISE
    message = "Generic docstring provides no useful information"
    pattern = re.compile(
        r'"""(This (function|method|class) (does|is|handles?|returns?|takes?) (stuff|things|something|it|the)\.?)"""',
        re.IGNORECASE,
    )
