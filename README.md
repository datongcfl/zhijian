# 智检 (Zhijian) - AI 代码质量检测工具

> 🛡️ 在 AI 生成的代码进入生产环境之前，捕获那些"看起来对但其实有问题"的代码

**智检** 是一款基于 [AI-SLOP-Detector](https://github.com/flamehaven01/AI-SLOP-Detector) 和 [sloppylint](https://github.com/rsionnach/sloppylint) 合并的 Python 静态分析工具，专注于检测 AI 生成代码中的常见质量问题。

---

## ✨ 为什么需要智检？

AI 生成的代码有独特的"毛病"，传统 linter 抓不到：

| 问题 | 传统 linter | 智检 |
|------|------------|------|
| 空函数但有看起来像真的 body | ❌ | ✅ |
| 导入了不存在的包 | ❌ | ✅ |
| 注释里说"should work"、"hopefully" | ❌ | ✅ |
| 跨语言语法泄漏（JS 的 `.push()` 写到 Python 里） | ❌ | ✅ |
| 文档过度吹嘘代码实际功能 | ❌ | ✅ |
| 只有一个方法的类（应该用函数） | ❌ | ✅ |

---

## 🚀 快速开始

```bash
# 安装
pip install zhijian

# 扫描当前目录
zhijian .

# 输出 JSON 报告到 stdout
zhijian --json

# 导出 JSON 报告
zhijian --output report.json

# CI 报告模式
zhijian --ci-report --ci-mode hard
```

---

## 🔍 检测规则一览 (39 个)

### 🔇 噪音检测 (Noise) - 4 个
| 规则 | 严重度 | 检测内容 |
|------|--------|---------|
| `redundant_comment` | MEDIUM | 注释只是重复代码 |
| `empty_docstring` | MEDIUM | 空文档字符串 |
| `generic_docstring` | LOW | 无信息量的通用文档 |
| `changelog_in_code` | LOW | 代码中写版本历史 |

### 🤥 占位符检测 (Placeholder) - 11 个
| 规则 | 严重度 | 检测内容 |
|------|--------|---------|
| `empty_except` | CRITICAL | 空的 except 块 |
| `not_implemented` | MEDIUM | 只抛 NotImplementedError |
| `pass_placeholder` | HIGH | 只有 pass 的函数 |
| `ellipsis_placeholder` | HIGH | 只有 ... 的函数 |
| `return_none_placeholder` | MEDIUM | 只返回 None |
| `return_constant_stub` | HIGH | 返回固定值的 stub |
| `todo_comment` | MEDIUM | TODO 注释 |
| `fixme_comment` | MEDIUM | FIXME 注释 |
| `hack_comment` | MEDIUM | HACK 注释 |
| `xxx_comment` | LOW | XXX 注释 |
| `interface_only_class` | MEDIUM | 只有接口没有实现的类 |

### 🏗️ 结构反模式 (Structural) - 5 个
| 规则 | 严重度 | 检测内容 |
|------|--------|---------|
| `bare_except` | CRITICAL | 裸 except（捕获所有异常） |
| `mutable_default_arg` | CRITICAL | 可变默认参数 |
| `star_import` | HIGH | `from x import *` |
| `global_statement` | MEDIUM | 使用 global 语句 |
| `single_method_class` | HIGH | 单方法类（应用函数代替） |

### 🌐 跨语言泄漏 (Cross-Language) - 6 个
| 规则 | 严重度 | 检测内容 |
|------|--------|---------|
| `javascript_array_push` | HIGH | JS 的 `.push()` |
| `java_equals_method` | HIGH | Java 的 `.equals()` |
| `ruby_each` | HIGH | Ruby 的 `.each` |
| `go_print` | HIGH | Go 的 `fmt.Println()` |
| `csharp_length` | HIGH | C# 的 `.Length` |
| `php_strlen` | HIGH | PHP 的 `strlen()` |

### 🔍 幻觉检测 (Phantom) - 1 个
| 规则 | 严重度 | 检测内容 |
|------|--------|---------|
| `phantom_import` | CRITICAL | 导入不存在的包 |

### 🐍 Python 高级检测 (Complexity) - 7 个
| 规则 | 严重度 | 检测内容 |
|------|--------|---------|
| `god_function` | HIGH | 上帝函数（太长太复杂） |
| `dead_code` | MEDIUM | 死代码 |
| `deep_nesting` | MEDIUM | 深度嵌套 |
| `lint_escape` | HIGH | 绕过 linter 的写法 |
| `exact_duplicate_pair` | MEDIUM | 完全重复的代码 |
| `function_clone_cluster` | MEDIUM | 克隆函数簇 |
| `placeholder_variable_naming` | LOW | 占位符变量名 |

### 🎨 风格检测 (Style) - 4 个
| 规则 | 严重度 | 检测内容 |
|------|--------|---------|
| `overconfident_comment` | MEDIUM | 过度自信注释（"obviously"、"clearly"） |
| `hedging_comment` | HIGH | 犹豫不决注释（"should work"、"hopefully"） |
| `apologetic_comment` | MEDIUM | 道歉式注释（"sorry"、"hack"） |
| `single_method_class` | HIGH | 单方法类 |

### 🤔 假设检测 (Assumption) - 1 个
| 规则 | 严重度 | 检测内容 |
|------|--------|---------|
| `assumption_comment` | HIGH | 假设性注释（"assuming"、"presumably"） |

---

## 📊 评分体系

智检使用 4 维评分引擎，每个文件得到一个 0-100 的"缺陷分"：

| 维度 | 权重 | 测量内容 |
|------|------|---------|
| **LDR** (逻辑密度) | 40% | 实际代码行 / 总行数 |
| **ICR** (膨胀检测) | 30% | 注释中的空话 vs 实际复杂度 |
| **DDC** (依赖使用) | 20% | 实际使用的导入 / 总导入数 |
| **Purity** (纯度) | 10% | 严重问题的指数衰减 |

**判定等级：**
- ✅ CLEAN (< 30): 健康
- ⚠️ SUSPICIOUS (30-50): 需要关注
- 🔶 INFLATED (50-70): 有水分
- 🚨 CRITICAL (≥ 70): 严重问题

---

## ⚙️ 配置

在项目根目录创建 `.zhijian.yaml`：

```yaml
# 权重调整
weights:
  ldr: 0.40
  inflation: 0.30
  ddc: 0.20
  purity: 0.10

# 忽略的文件
ignore:
  - "tests/**"
  - "**/__init__.py"

# 禁用的规则
disable:
  - "generic_docstring"
  - "changelog_in_code"
```

---

## 🔌 扩展指南

### 添加新的检测规则

1. 在 `src/zhijian/patterns/` 对应子目录创建新文件
2. 继承 `RegexPattern`（正则）或 `ASTPattern`（AST）
3. 在 `__init__.py` 中注册

```python
# 示例：检测调试 print 语句
import re
from zhijian.patterns.base import RegexPattern, Severity, Axis

class DebugPrintPattern(RegexPattern):
    id = "debug_print"
    severity = Severity.MEDIUM
    axis = Axis.NOISE
    message = "Debug print statement - remove before shipping"
    pattern = re.compile(r"^\s*print\s*\(", re.MULTILINE)
```

---

## 🙏 致谢

- [AI-SLOP-Detector](https://github.com/flamehaven01/AI-SLOP-Detector) - 核心架构和评分引擎
- [sloppylint](https://github.com/rsionnach/sloppylint) - 噪音和风格检测
- [KarpeSlop](https://github.com/CodeDeficient/KarpeSlop) - 原始灵感

---

## 📄 许可证

MIT License
