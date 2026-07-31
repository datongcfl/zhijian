"""智检 MCP 服务端 - 通过 stdio 协议提供代码质量检测功能。

使用方式:
    zhijian mcp

MCP 客户端配置:
    {
      "command": "zhijian",
      "args": ["mcp"]
    }
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def run_stdio_server() -> int:
    """启动 MCP stdio 服务。

    实现基本的 JSON-RPC 2.0 协议，支持以下工具:
    - zhijian.scan: 扫描文件或目录
    - zhijian.scan_file: 扫描单个文件
    - zhijian.list_patterns: 列出所有检测规则
    """
    from zhijian.core import SlopDetector
    from zhijian.patterns import get_all_patterns

    detector = None

    def get_detector():
        nonlocal detector
        if detector is None:
            detector = SlopDetector()
        return detector

    def handle_request(request: dict) -> dict:
        """处理 JSON-RPC 请求。"""
        method = request.get("method", "")
        params = request.get("params", {})
        req_id = request.get("id")

        try:
            if method == "initialize":
                result = {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {"listChanged": False}},
                    "serverInfo": {"name": "zhijian", "version": "1.0.0"},
                }
            elif method == "tools/list":
                result = {
                    "tools": [
                        {
                            "name": "zhijian.scan",
                            "description": "扫描文件或目录，返回代码质量报告",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "path": {"type": "string", "description": "要扫描的文件或目录路径"},
                                    "severity": {"type": "string", "enum": ["low", "medium", "high", "critical"], "description": "最低严重度过滤"},
                                },
                                "required": ["path"],
                            },
                        },
                        {
                            "name": "zhijian.list_patterns",
                            "description": "列出所有可用的检测规则",
                            "inputSchema": {"type": "object", "properties": {}},
                        },
                    ]
                }
            elif method == "tools/call":
                tool_name = params.get("name", "")
                tool_args = params.get("arguments", {})

                if tool_name == "zhijian.scan":
                    path = tool_args.get("path", ".")
                    d = get_detector()
                    if Path(path).is_dir():
                        result_data = d.analyze_project(path)
                    else:
                        result_data = d.analyze_file(path)
                    # 转换为可序列化的字典
                    from zhijian.cli import _result_to_dict
                    result = {"content": [{"type": "text", "text": json.dumps(_result_to_dict(result_data), ensure_ascii=False, indent=2)}]}
                elif tool_name == "zhijian.list_patterns":
                    patterns = get_all_patterns()
                    pattern_list = [
                        {"id": p.id, "severity": p.severity.value, "axis": p.axis.value}
                        for p in patterns
                    ]
                    result = {"content": [{"type": "text", "text": json.dumps(pattern_list, ensure_ascii=False, indent=2)}]}
                else:
                    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Unknown tool: {tool_name}"}}
            elif method == "notifications/initialized":
                return {}  # 通知不需要响应
            else:
                return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Unknown method: {method}"}}

            return {"jsonrpc": "2.0", "id": req_id, "result": result}

        except Exception as e:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32603, "message": str(e)}}

    # 主循环：从 stdin 读取 JSON-RPC 请求
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            request = json.loads(line)
        except json.JSONDecodeError:
            response = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error"}}
            print(json.dumps(response), flush=True)
            continue

        response = handle_request(request)
        if response:
            print(json.dumps(response), flush=True)

    return 0


if __name__ == "__main__":
    sys.exit(run_stdio_server())
