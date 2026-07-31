"""安全检测：错误信息泄露检测器

检测将异常信息直接返回给客户端的代码。
攻击者可以利用这些信息了解内部实现细节。

示例：
- return jsonify({"error": str(e)})     ← 危险
- return {"message": str(e), ...}        ← 危险
- return Response(str(e), status=500)    ← 危险
"""

import re
from zhijian.patterns.base import RegexPattern, Severity, Axis


class ErrorLeakagePattern(RegexPattern):
    """检测异常信息泄露给客户端"""

    id = "error_leakage"
    severity = Severity.MEDIUM
    axis = Axis.QUALITY
    message = "Exception details exposed to client — use generic error messages in production"
    pattern = re.compile(
        r"(?:str\s*\(\s*e\s*\)|repr\s*\(\s*e\s*\))",
        re.IGNORECASE,
    )
