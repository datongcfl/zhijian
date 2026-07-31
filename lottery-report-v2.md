# 彩票系统 - AI 代码质量扫描报告

> 扫描时间: 2026-07-31 16:52:09
> 扫描工具: 智检 (zhijian) v1.0.0

---

## 一、项目概览

| 指标 | 数值 |
|------|------|
| 总文件数 | 129 |
| 干净文件 | 93 |
| 问题文件 | 36 |
| 总体状态 | ✅ CLEAN (健康) |
| 平均缺陷分 | 20.5/100 |
| 加权缺陷分 | 24.4/100 |
| LDR (逻辑密度) | 88.4% |
| DDC (依赖使用率) | 96.5% |

---

## 二、问题类型统计 (272 个问题)

| 问题类型 | 数量 | 严重度 | 说明 |
|---------|------|--------|------|
| phantom_import | 110 | 🔴 critical | 导入了不存在的模块 |
| god_function | 86 | 🟠 high | 函数太长或太复杂 |
| deep_nesting | 20 | 🟠 high | 嵌套太深 |
| nested_complexity | 20 | 🔴 critical | 深嵌套+高复杂度 |
| lint_escape | 10 | 🟢 low | noqa/type:ignore 注释 |
| global_statement | 8 | 🟠 high | 使用 global 语句 |
| function_clone_cluster | 6 | 🟠 high | 克隆函数簇 |
| bare_except | 5 | 🔴 critical | 裸 except 捕获所有异常 |
| pass_placeholder | 3 | 🟠 high | 空函数占位 |
| empty_except | 3 | 🟡 medium | 空 except 块 |
| todo_comment | 1 | 🟡 medium | TODO 注释 |

---

## 三、问题文件详细列表

### 📦 `D:\福昶工作目录\彩票系统\src\cooccurrence.py`

- **状态**: DEP_NOISE (依赖噪音)
- **缺陷分**: 94.2/100
- **LDR**: 100.0%
- **DDC**: 0.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 69 | 🟠 high | global_statement | Global statement makes code harder to test and reason about |
| 80 | 🟠 high | global_statement | Global statement makes code harder to test and reason about |

### 📦 `D:\福昶工作目录\彩票系统\backups\codex-20260608-ensemble-filters-migration\src\cooccurrence.py`

- **状态**: DEP_NOISE (依赖噪音)
- **缺陷分**: 94.2/100
- **LDR**: 100.0%
- **DDC**: 0.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 69 | 🟠 high | global_statement | Global statement makes code harder to test and reason about |
| 80 | 🟠 high | global_statement | Global statement makes code harder to test and reason about |

### 🚨 `D:\福昶工作目录\彩票系统\scripts\fetch_and_update.py`

- **状态**: CRITICAL (严重问题)
- **缺陷分**: 75.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 137 | 🟠 high | god_function | God function '_auto_lock_for_next_draw': 64 logic lines (lim |
| 211 | 🟠 high | god_function | God function 'fetch_and_update': 98 logic lines (limit 50),  |
| 14 | 🔴 critical | phantom_import | Phantom import: 'src.fetcher' cannot be resolved (not in std |
| 15 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 16 | 🔴 critical | phantom_import | Phantom import: 'src.learning' cannot be resolved (not in st |
| 19 | 🔴 critical | phantom_import | Phantom import: 'settle' cannot be resolved (not in stdlib,  |
| 139 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |
| 140 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 280 | 🟡 medium | phantom_import | Undeclared optional dependency: 'src.ab_testing' is guarded  |

### 🚨 `D:\福昶工作目录\彩票系统\backups\codex-20260609-before-auto-lock-v0.11.8\fetch_and_update.py`

- **状态**: CRITICAL (严重问题)
- **缺陷分**: 75.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 137 | 🟠 high | god_function | God function '_auto_lock_for_next_draw': 64 logic lines (lim |
| 211 | 🟠 high | god_function | God function 'fetch_and_update': 98 logic lines (limit 50),  |
| 14 | 🔴 critical | phantom_import | Phantom import: 'src.fetcher' cannot be resolved (not in std |
| 15 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 16 | 🔴 critical | phantom_import | Phantom import: 'src.learning' cannot be resolved (not in st |
| 19 | 🔴 critical | phantom_import | Phantom import: 'settle' cannot be resolved (not in stdlib,  |
| 139 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |
| 140 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 280 | 🟡 medium | phantom_import | Undeclared optional dependency: 'src.ab_testing' is guarded  |

### 🚨 `D:\福昶工作目录\彩票系统\controllers\bets.py`

- **状态**: CRITICAL (严重问题)
- **缺陷分**: 72.1/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 5 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 7 | 🔴 critical | phantom_import | Phantom import: 'settle' cannot be resolved (not in stdlib,  |
| 86 | 🔴 critical | phantom_import | Phantom import: 'src.auto_run' cannot be resolved (not in st |
| 94 | 🔴 critical | phantom_import | Phantom import: 'src.persistence' cannot be resolved (not in |
| 101 | 🔴 critical | phantom_import | Phantom import: 'src.persistence' cannot be resolved (not in |

### 🚨 `D:\福昶工作目录\彩票系统\services\recommend_ui.py`

- **状态**: CRITICAL (严重问题)
- **缺陷分**: 72.1/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 6 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |
| 7 | 🔴 critical | phantom_import | Phantom import: 'src.ab_testing' cannot be resolved (not in  |
| 8 | 🔴 critical | phantom_import | Phantom import: 'src.ensemble_recommender' cannot be resolve |
| 9 | 🔴 critical | phantom_import | Phantom import: 'src.strategy_rules' cannot be resolved (not |
| 14 | 🔴 critical | phantom_import | Phantom import: 'hit_rate_helpers' cannot be resolved (not i |

### 🚨 `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\controllers\dashboard.py`

- **状态**: CRITICAL (严重问题)
- **缺陷分**: 72.1/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 17 | 🟠 high | deep_nesting | Function '_compute_missing' has nesting depth 5 (limit 4) |
| 17 | 🔴 critical | nested_complexity | Function '_compute_missing' has both deep nesting (depth=5)  |
| 4 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 8 | 🔴 critical | phantom_import | Phantom import: 'src.learning' cannot be resolved (not in st |
| 9 | 🔴 critical | phantom_import | Phantom import: 'settle' cannot be resolved (not in stdlib,  |
| 12 | 🔴 critical | phantom_import | Phantom import: 'src.strategy_rules' cannot be resolved (not |

### 🚨 `D:\福昶工作目录\彩票系统\backups\codex-20260606-before-sync-vps-0.8.8\app.py`

- **状态**: CRITICAL (严重问题)
- **缺陷分**: 72.1/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 119 | 🟠 high | god_function | God function '_ai_entertainment_ssq': 66 logic lines (limit  |
| 320 | 🟠 high | deep_nesting | Function 'signup' has nesting depth 6 (limit 4) |
| 646 | 🟠 high | deep_nesting | Function '_compute_missing' has nesting depth 5 (limit 4) |
| 320 | 🔴 critical | nested_complexity | Function 'signup' has both deep nesting (depth=6) and high c |
| 646 | 🔴 critical | nested_complexity | Function '_compute_missing' has both deep nesting (depth=5)  |
| 6 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |
| 7 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 8 | 🔴 critical | phantom_import | Phantom import: 'src.learning' cannot be resolved (not in st |

### 🚨 `D:\福昶工作目录\彩票系统\backups\codex-20260606-restore-missing-modules\app.py`

- **状态**: CRITICAL (严重问题)
- **缺陷分**: 72.1/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 119 | 🟠 high | god_function | God function '_ai_entertainment_ssq': 66 logic lines (limit  |
| 320 | 🟠 high | deep_nesting | Function 'signup' has nesting depth 6 (limit 4) |
| 646 | 🟠 high | deep_nesting | Function '_compute_missing' has nesting depth 5 (limit 4) |
| 320 | 🔴 critical | nested_complexity | Function 'signup' has both deep nesting (depth=6) and high c |
| 646 | 🔴 critical | nested_complexity | Function '_compute_missing' has both deep nesting (depth=5)  |
| 6 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |
| 7 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 8 | 🔴 critical | phantom_import | Phantom import: 'src.learning' cannot be resolved (not in st |

### 🚨 `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\settle.py`

- **状态**: CRITICAL (严重问题)
- **缺陷分**: 71.8/100
- **LDR**: 100.0%
- **DDC**: 40.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 25 | 🔴 critical | bare_except | Bare except catches everything including SystemExit and Keyb |
| 44 | 🔴 critical | bare_except | Bare except catches everything including SystemExit and Keyb |
| 62 | 🔴 critical | bare_except | Bare except catches everything including SystemExit and Keyb |
| 5 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |

### 🔶 `D:\福昶工作目录\彩票系统\controllers\dashboard.py`

- **状态**: INFLATED (有水分)
- **缺陷分**: 63.1/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 17 | 🟠 high | deep_nesting | Function '_compute_missing' has nesting depth 5 (limit 4) |
| 17 | 🔴 critical | nested_complexity | Function '_compute_missing' has both deep nesting (depth=5)  |
| 4 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 9 | 🔴 critical | phantom_import | Phantom import: 'src.learning' cannot be resolved (not in st |
| 12 | 🔴 critical | phantom_import | Phantom import: 'src.strategy_rules' cannot be resolved (not |

### 🔶 `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\src\backtest\optimizer_fast.py`

- **状态**: INFLATED (有水分)
- **缺陷分**: 63.1/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 19 | 🔴 critical | phantom_import | Phantom import: 'src.backtest.engine' cannot be resolved (no |
| 20 | 🔴 critical | phantom_import | Phantom import: 'src.backtest.metrics' cannot be resolved (n |
| 195 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |
| 205 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |
| 1 | 🟠 high | function_clone_cluster | 4 structurally similar functions detected (AST JSD < 0.05):  |

### 🔶 `D:\福昶工作目录\彩票系统\src\backtest\optimizer_fast.py`

- **状态**: INFLATED (有水分)
- **缺陷分**: 63.1/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 19 | 🔴 critical | phantom_import | Phantom import: 'src.backtest.engine' cannot be resolved (no |
| 20 | 🔴 critical | phantom_import | Phantom import: 'src.backtest.metrics' cannot be resolved (n |
| 195 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |
| 205 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |
| 1 | 🟠 high | function_clone_cluster | 4 structurally similar functions detected (AST JSD < 0.05):  |

### 🔶 `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\scripts\fetch_and_update.py`

- **状态**: INFLATED (有水分)
- **缺陷分**: 60.1/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 137 | 🟡 medium | god_function | God function 'fetch_and_update': 55 logic lines (limit 50) |
| 14 | 🔴 critical | phantom_import | Phantom import: 'src.fetcher' cannot be resolved (not in std |
| 15 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 16 | 🔴 critical | phantom_import | Phantom import: 'src.learning' cannot be resolved (not in st |
| 19 | 🔴 critical | phantom_import | Phantom import: 'settle' cannot be resolved (not in stdlib,  |

### 🔶 `D:\福昶工作目录\彩票系统\scripts\create_prediction_snapshot.py`

- **状态**: INFLATED (有水分)
- **缺陷分**: 58.1/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 12 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |
| 13 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 14 | 🔴 critical | phantom_import | Phantom import: 'src.learning' cannot be resolved (not in st |
| 15 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |

### 🔶 `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\scripts\create_prediction_snapshot.py`

- **状态**: INFLATED (有水分)
- **缺陷分**: 58.1/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 12 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |
| 13 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 14 | 🔴 critical | phantom_import | Phantom import: 'src.learning' cannot be resolved (not in st |
| 15 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |

### 🔶 `D:\福昶工作目录\彩票系统\backups\codex-20260606-before-sync-vps-0.8.8\scripts\create_prediction_snapshot.py`

- **状态**: INFLATED (有水分)
- **缺陷分**: 58.1/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 12 | 🔴 critical | phantom_import | Phantom import: 'app' cannot be resolved (not in stdlib, bui |
| 13 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 14 | 🔴 critical | phantom_import | Phantom import: 'src.learning' cannot be resolved (not in st |
| 15 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |

### 🔶 `D:\福昶工作目录\彩票系统\controllers\auth.py`

- **状态**: INFLATED (有水分)
- **缺陷分**: 53.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 101 | 🟠 high | deep_nesting | Function 'login' has nesting depth 5 (limit 4) |
| 146 | 🟠 high | deep_nesting | Function 'signup' has nesting depth 7 (limit 4) |
| 101 | 🔴 critical | nested_complexity | Function 'login' has both deep nesting (depth=5) and high cy |
| 146 | 🔴 critical | nested_complexity | Function 'signup' has both deep nesting (depth=7) and high c |
| 4 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |

### 🔶 `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\controllers\auth.py`

- **状态**: INFLATED (有水分)
- **缺陷分**: 53.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 101 | 🟠 high | deep_nesting | Function 'login' has nesting depth 5 (limit 4) |
| 146 | 🟠 high | deep_nesting | Function 'signup' has nesting depth 7 (limit 4) |
| 101 | 🔴 critical | nested_complexity | Function 'login' has both deep nesting (depth=5) and high cy |
| 146 | 🔴 critical | nested_complexity | Function 'signup' has both deep nesting (depth=7) and high c |
| 4 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |

### 🔶 `D:\福昶工作目录\彩票系统\src\auto_run.py`

- **状态**: INFLATED (有水分)
- **缺陷分**: 52.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 63 | 🟠 high | god_function | God function 'auto_lock_next': 72 logic lines (limit 50), co |
| 12 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 13 | 🔴 critical | phantom_import | Phantom import: 'settle' cannot be resolved (not in stdlib,  |
| 14 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |
| 24 | 🟡 medium | phantom_import | Undeclared optional dependency: 'src.fetcher' is guarded wit |
| 25 | 🟡 medium | phantom_import | Undeclared optional dependency: 'src.db' is guarded with Imp |

### ⚠️ `D:\福昶工作目录\彩票系统\scripts\score_prediction_snapshot.py`

- **状态**: SUSPICIOUS (可疑)
- **缺陷分**: 47.9/100
- **LDR**: 99.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 74 | 🟠 high | god_function | God function '_prize_ssq': complexity=14 (limit 10) |
| 92 | 🟠 high | god_function | God function '_prize_dlt': complexity=32 (limit 10) |
| 156 | 🟡 medium | god_function | God function 'score_latest_snapshot': 63 logic lines (limit  |
| 92 | 🟠 high | deep_nesting | Function '_prize_dlt' has nesting depth 6 (limit 4) |
| 92 | 🔴 critical | nested_complexity | Function '_prize_dlt' has both deep nesting (depth=6) and hi |
| 13 | 🟢 low | lint_escape | Lint suppression: # noqa: E402 |
| 13 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |

### ⚠️ `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\scripts\score_prediction_snapshot.py`

- **状态**: SUSPICIOUS (可疑)
- **缺陷分**: 47.9/100
- **LDR**: 99.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 74 | 🟠 high | god_function | God function '_prize_ssq': complexity=14 (limit 10) |
| 92 | 🟠 high | god_function | God function '_prize_dlt': complexity=32 (limit 10) |
| 156 | 🟡 medium | god_function | God function 'score_latest_snapshot': 63 logic lines (limit  |
| 92 | 🟠 high | deep_nesting | Function '_prize_dlt' has nesting depth 6 (limit 4) |
| 92 | 🔴 critical | nested_complexity | Function '_prize_dlt' has both deep nesting (depth=6) and hi |
| 13 | 🟢 low | lint_escape | Lint suppression: # noqa: E402 |
| 13 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |

### ⚠️ `D:\福昶工作目录\彩票系统\backups\codex-20260606-before-sync-vps-0.8.8\scripts\fetch_and_update.py`

- **状态**: SUSPICIOUS (可疑)
- **缺陷分**: 45.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 136 | 🟡 medium | god_function | God function 'fetch_and_update': 53 logic lines (limit 50) |
| 14 | 🔴 critical | phantom_import | Phantom import: 'src.fetcher' cannot be resolved (not in std |
| 15 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 16 | 🔴 critical | phantom_import | Phantom import: 'src.learning' cannot be resolved (not in st |

### ⚠️ `D:\福昶工作目录\彩票系统\src\recommender.py`

- **状态**: SUSPICIOUS (可疑)
- **缺陷分**: 44.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 121 | 🟠 high | god_function | God function 'recommend_ssq': 71 logic lines (limit 50), com |
| 207 | 🟠 high | god_function | God function 'recommend_dlt': complexity=12 (limit 10) |
| 272 | 🟠 high | god_function | God function 'entertainment_ssq': 68 logic lines (limit 50), |
| 369 | 🟠 high | god_function | God function 'recommend_ssq_from_draws': complexity=19 (limi |
| 423 | 🟠 high | god_function | God function 'recommend_dlt_from_draws': complexity=15 (limi |
| 73 | 🔴 critical | phantom_import | Phantom import: 'src.weight_config' cannot be resolved (not  |
| 1 | 🟠 high | function_clone_cluster | 4 structurally similar functions detected (AST JSD < 0.05):  |

### ⚠️ `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\services\recommend_ui.py`

- **状态**: SUSPICIOUS (可疑)
- **缺陷分**: 43.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 6 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |
| 7 | 🔴 critical | phantom_import | Phantom import: 'src.strategy_rules' cannot be resolved (not |
| 12 | 🔴 critical | phantom_import | Phantom import: 'hit_rate_helpers' cannot be resolved (not i |

### ⚠️ `D:\福昶工作目录\彩票系统\backups\codex-20260608-ensemble-filters-migration\src\recommender.py`

- **状态**: SUSPICIOUS (可疑)
- **缺陷分**: 43.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 149 | 🟡 medium | empty_except | Empty handler for 'Exception' silently discards the exceptio |
| 379 | 🟡 medium | empty_except | Empty handler for 'Exception' silently discards the exceptio |
| 121 | 🟠 high | god_function | God function 'recommend_ssq': 62 logic lines (limit 50), com |
| 196 | 🟠 high | god_function | God function 'recommend_dlt': complexity=12 (limit 10) |
| 261 | 🟠 high | god_function | God function 'entertainment_ssq': 68 logic lines (limit 50), |
| 358 | 🟠 high | god_function | God function 'recommend_ssq_from_draws': complexity=19 (limi |
| 412 | 🟠 high | god_function | God function 'recommend_dlt_from_draws': complexity=15 (limi |
| 73 | 🔴 critical | phantom_import | Phantom import: 'src.weight_config' cannot be resolved (not  |

### ⚠️ `D:\福昶工作目录\彩票系统\src\backtest\local_optimizer.py`

- **状态**: SUSPICIOUS (可疑)
- **缺陷分**: 41.5/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 528 | 🟠 high | god_function | God function 'main': 75 logic lines (limit 50), complexity=1 |
| 528 | 🟠 high | deep_nesting | Function 'main' has nesting depth 5 (limit 4) |
| 528 | 🔴 critical | nested_complexity | Function 'main' has both deep nesting (depth=5) and high cyc |
| 596 | 🟡 medium | phantom_import | Undeclared optional dependency: 'src.weight_config' is guard |
| 1 | 🔴 critical | function_clone_cluster | 6 structurally near-identical functions detected (AST JSD <  |

### ⚠️ `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\utils\rate_limit.py`

- **状态**: SUSPICIOUS (可疑)
- **缺陷分**: 40.4/100
- **LDR**: 84.6%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 31 | 🔴 critical | bare_except | Bare except catches everything including SystemExit and Keyb |
| 24 | 🔴 critical | bare_except | Bare except catches everything including SystemExit and Keyb |
| 11 | 🟠 high | pass_placeholder | Empty function with only pass - placeholder not implemented |

### ⚠️ `D:\福昶工作目录\彩票系统\controllers\api.py`

- **状态**: SUSPICIOUS (可疑)
- **缺陷分**: 36.6/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 25 | 🟠 high | god_function | God function 'hit_rate': complexity=11 (limit 10) |
| 20 | 🔴 critical | phantom_import | Phantom import: 'src.backtest' cannot be resolved (not in st |
| 87 | 🔴 critical | phantom_import | Phantom import: 'src.weight_config' cannot be resolved (not  |

### ⚠️ `D:\福昶工作目录\彩票系统\scripts\fetch_all.py`

- **状态**: SUSPICIOUS (可疑)
- **缺陷分**: 34.5/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 50 | 🟠 high | god_function | God function 'main': 53 logic lines (limit 50), complexity=1 |
| 14 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 15 | 🔴 critical | phantom_import | Phantom import: 'src.fetcher' cannot be resolved (not in std |

### ⚠️ `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\scripts\fetch_all.py`

- **状态**: SUSPICIOUS (可疑)
- **缺陷分**: 34.5/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 50 | 🟠 high | god_function | God function 'main': 53 logic lines (limit 50), complexity=1 |
| 14 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 15 | 🔴 critical | phantom_import | Phantom import: 'src.fetcher' cannot be resolved (not in std |

### ⚠️ `D:\福昶工作目录\彩票系统\src\weight_config.py`

- **状态**: SUSPICIOUS (可疑)
- **缺陷分**: 32.3/100
- **LDR**: 100.0%
- **DDC**: 66.7%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 43 | 🟠 high | global_statement | Global statement makes code harder to test and reason about |
| 141 | 🟠 high | deep_nesting | Function 'validate_config' has nesting depth 6 (limit 4) |
| 141 | 🔴 critical | nested_complexity | Function 'validate_config' has both deep nesting (depth=6) a |

### ⚠️ `D:\福昶工作目录\彩票系统\backups\codex-20260608-ensemble-filters-migration\src\weight_config.py`

- **状态**: SUSPICIOUS (可疑)
- **缺陷分**: 32.3/100
- **LDR**: 100.0%
- **DDC**: 66.7%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 43 | 🟠 high | global_statement | Global statement makes code harder to test and reason about |
| 141 | 🟠 high | deep_nesting | Function 'validate_config' has nesting depth 6 (limit 4) |
| 141 | 🔴 critical | nested_complexity | Function 'validate_config' has both deep nesting (depth=6) a |

### ⚠️ `D:\福昶工作目录\彩票系统\scripts\update_learning_profile.py`

- **状态**: SUSPICIOUS (可疑)
- **缺陷分**: 31.5/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 9 | 🟢 low | lint_escape | Lint suppression: # noqa: E402 |
| 10 | 🟢 low | lint_escape | Lint suppression: # noqa: E402 |
| 9 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 10 | 🔴 critical | phantom_import | Phantom import: 'src.learning' cannot be resolved (not in st |

### ⚠️ `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\scripts\update_learning_profile.py`

- **状态**: SUSPICIOUS (可疑)
- **缺陷分**: 31.5/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 9 | 🟢 low | lint_escape | Lint suppression: # noqa: E402 |
| 10 | 🟢 low | lint_escape | Lint suppression: # noqa: E402 |
| 9 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 10 | 🔴 critical | phantom_import | Phantom import: 'src.learning' cannot be resolved (not in st |

### ⚠️ `D:\福昶工作目录\彩票系统\backups\codex-20260606-before-sync-vps-0.8.8\scripts\update_learning_profile.py`

- **状态**: SUSPICIOUS (可疑)
- **缺陷分**: 31.5/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 9 | 🟢 low | lint_escape | Lint suppression: # noqa: E402 |
| 10 | 🟢 low | lint_escape | Lint suppression: # noqa: E402 |
| 9 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 10 | 🔴 critical | phantom_import | Phantom import: 'src.learning' cannot be resolved (not in st |

### ✅ `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\src\backtest\local_optimizer.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 29.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 513 | 🟠 high | god_function | God function 'main': 55 logic lines (limit 50), complexity=1 |
| 513 | 🟠 high | deep_nesting | Function 'main' has nesting depth 5 (limit 4) |
| 513 | 🔴 critical | nested_complexity | Function 'main' has both deep nesting (depth=5) and high cyc |
| 1 | 🟠 high | function_clone_cluster | 5 structurally similar functions detected (AST JSD < 0.05):  |

### ✅ `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\controllers\bets.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 29.5/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 5 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |
| 7 | 🔴 critical | phantom_import | Phantom import: 'settle' cannot be resolved (not in stdlib,  |

### ✅ `D:\福昶工作目录\彩票系统\src\backtest\math_observation.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 29.5/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 7 | 🔴 critical | phantom_import | Phantom import: 'src.signals_distribution' cannot be resolve |
| 8 | 🔴 critical | phantom_import | Phantom import: 'src.time_decay' cannot be resolved (not in  |

### ✅ `D:\福昶工作目录\彩票系统\src\scorer.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 29.0/100
- **LDR**: 99.6%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 127 | 🟡 medium | god_function | God function '_compute_ssq': 87 logic lines (limit 50) |
| 237 | 🟡 medium | god_function | God function '_compute_dlt': 57 logic lines (limit 50) |
| 448 | 🟠 high | god_function | God function '_compute_dlt_from_draws_weighted': 110 logic l |
| 572 | 🟠 high | deep_nesting | Function '_compute_pl3_from_draws_weighted' has nesting dept |
| 572 | 🔴 critical | nested_complexity | Function '_compute_pl3_from_draws_weighted' has both deep ne |

### ✅ `D:\福昶工作目录\彩票系统\src\ensemble_recommender.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 27.2/100
- **LDR**: 97.9%
- **DDC**: 80.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 368 | 🟠 high | pass_placeholder | Empty function with only pass - placeholder not implemented |
| 374 | 🟡 medium | todo_comment | TODO comment - incomplete implementation |
| 21 | 🟠 high | god_function | God function 'recommend_ssq_ensemble': 85 logic lines (limit |
| 151 | 🟠 high | god_function | God function 'recommend_dlt_ensemble': 86 logic lines (limit |
| 270 | 🟠 high | god_function | God function 'recommend_pl3_ensemble': 58 logic lines (limit |

### ✅ `D:\福昶工作目录\彩票系统\backups\codex-20260608-ensemble-filters-migration\src\scorer.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 26.1/100
- **LDR**: 99.5%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 124 | 🟢 low | god_function | God function '_compute_ssq': 81 logic lines (limit 50) |
| 400 | 🟠 high | god_function | God function '_compute_dlt_from_draws_weighted': 72 logic li |
| 479 | 🟠 high | deep_nesting | Function '_compute_pl3_from_draws_weighted' has nesting dept |
| 479 | 🔴 critical | nested_complexity | Function '_compute_pl3_from_draws_weighted' has both deep ne |

### ✅ `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\src\scorer.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 25.1/100
- **LDR**: 99.4%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 290 | 🟠 high | god_function | God function '_compute_dlt_from_draws_weighted': 72 logic li |
| 369 | 🟠 high | deep_nesting | Function '_compute_pl3_from_draws_weighted' has nesting dept |
| 369 | 🔴 critical | nested_complexity | Function '_compute_pl3_from_draws_weighted' has both deep ne |

### ✅ `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\src\recommender.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 25.0/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 34 | 🟠 high | god_function | God function 'recommend_ssq': complexity=12 (limit 10) |
| 90 | 🟠 high | god_function | God function 'recommend_dlt': complexity=12 (limit 10) |
| 183 | 🟠 high | god_function | God function 'entertainment_ssq': 68 logic lines (limit 50), |
| 280 | 🟠 high | god_function | God function 'recommend_ssq_from_draws': complexity=14 (limi |
| 312 | 🟠 high | god_function | God function 'recommend_dlt_from_draws': complexity=14 (limi |

### ✅ `D:\福昶工作目录\彩票系统\app.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 24.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 9 | 🟠 high | god_function | God function 'create_app': 84 logic lines (limit 50), comple |
| 72 | 🟠 high | god_function | God function '_check_auth': complexity=12 (limit 10) |
| 32 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |

### ✅ `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\app.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 24.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 9 | 🟠 high | god_function | God function 'create_app': 66 logic lines (limit 50), comple |
| 53 | 🟠 high | god_function | God function '_check_auth': complexity=11 (limit 10) |
| 32 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |

### ✅ `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\controllers\api.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 23.6/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 27 | 🟠 high | god_function | God function 'hit_rate': complexity=11 (limit 10) |
| 103 | 🟢 low | lint_escape | Lint suppression: # noqa: E402 |
| 22 | 🔴 critical | phantom_import | Phantom import: 'src.backtest' cannot be resolved (not in st |

### ✅ `D:\福昶工作目录\彩票系统\settle.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 22.3/100
- **LDR**: 100.0%
- **DDC**: 66.7%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 4 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |

### ✅ `D:\福昶工作目录\彩票系统\src\strategy_rules.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 20.2/100
- **LDR**: 99.6%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 44 | 🟠 high | god_function | God function '_pl3_group6': complexity=12 (limit 10) |
| 128 | 🟠 high | god_function | God function 'ssq_blue_lock': 55 logic lines (limit 50), com |
| 212 | 🟠 high | god_function | God function 'dlt_back_lock': 58 logic lines (limit 50), com |
| 290 | 🟠 high | god_function | God function 'get_miss_streak': complexity=12 (limit 10) |

### ✅ `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\src\strategy_rules.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 20.2/100
- **LDR**: 99.6%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 44 | 🟠 high | god_function | God function '_pl3_group6': complexity=12 (limit 10) |
| 128 | 🟠 high | god_function | God function 'ssq_blue_lock': 55 logic lines (limit 50), com |
| 212 | 🟠 high | god_function | God function 'dlt_back_lock': 58 logic lines (limit 50), com |
| 290 | 🟠 high | god_function | God function 'get_miss_streak': complexity=12 (limit 10) |

### ✅ `D:\福昶工作目录\彩票系统\backups\codex-20260608-ensemble-filters-migration\src\strategy_rules.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 20.2/100
- **LDR**: 99.6%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 44 | 🟠 high | god_function | God function '_pl3_group6': complexity=12 (limit 10) |
| 128 | 🟠 high | god_function | God function 'ssq_blue_lock': 55 logic lines (limit 50), com |
| 212 | 🟠 high | god_function | God function 'dlt_back_lock': 58 logic lines (limit 50), com |
| 290 | 🟠 high | god_function | God function 'get_miss_streak': complexity=12 (limit 10) |

### ✅ `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\src\backtest\metrics.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 19.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 71 | 🟠 high | deep_nesting | Function 'aggregate_generic_results' has nesting depth 5 (li |
| 71 | 🔴 critical | nested_complexity | Function 'aggregate_generic_results' has both deep nesting ( |

### ✅ `D:\福昶工作目录\彩票系统\backups\codex-20260606-before-sync-vps-0.8.8\scripts\score_prediction_snapshot.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 18.5/100
- **LDR**: 98.4%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 81 | 🟡 medium | god_function | God function 'score_latest_snapshot': 60 logic lines (limit  |
| 13 | 🟢 low | lint_escape | Lint suppression: # noqa: E402 |
| 13 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |

### ✅ `D:\福昶工作目录\彩票系统\scripts\generate_performance_report.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 16.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 91 | 🟡 medium | god_function | God function 'generate_text_report': 71 logic lines (limit 5 |
| 29 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |

### ✅ `D:\福昶工作目录\彩票系统\check_auto_snapshot.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 14.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 1 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |

### ✅ `D:\福昶工作目录\彩票系统\check_learning_render.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 14.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 2 | 🔴 critical | phantom_import | Phantom import: 'src.learning' cannot be resolved (not in st |

### ✅ `D:\福昶工作目录\彩票系统\scripts\cron_settle.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 14.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 17 | 🔴 critical | phantom_import | Phantom import: 'settle' cannot be resolved (not in stdlib,  |

### ✅ `D:\福昶工作目录\彩票系统\scripts\recommend.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 14.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 9 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |

### ✅ `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\scripts\recommend.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 14.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 9 | 🔴 critical | phantom_import | Phantom import: 'src.recommender' cannot be resolved (not in |

### ✅ `D:\福昶工作目录\彩票系统\backups\codex-20260606-before-sync-vps-0.8.8\check_auto_snapshot.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 14.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 1 | 🔴 critical | phantom_import | Phantom import: 'src.db' cannot be resolved (not in stdlib,  |

### ✅ `D:\福昶工作目录\彩票系统\backups\codex-20260606-before-sync-vps-0.8.8\check_learning_render.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 14.9/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 2 | 🔴 critical | phantom_import | Phantom import: 'src.learning' cannot be resolved (not in st |

### ✅ `D:\福昶工作目录\彩票系统\src\learning.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 12.0/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 226 | 🟠 high | global_statement | Global statement makes code harder to test and reason about |
| 22 | 🟡 medium | god_function | God function 'build_learning_profile': 67 logic lines (limit |
| 112 | 🟠 high | god_function | God function 'get_learning_bias': complexity=14 (limit 10) |

### ✅ `D:\福昶工作目录\彩票系统\backups\codex-20260608-ensemble-filters-migration\src\learning.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 12.0/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 224 | 🟠 high | global_statement | Global statement makes code harder to test and reason about |
| 22 | 🟡 medium | god_function | God function 'build_learning_profile': 67 logic lines (limit |
| 112 | 🟠 high | god_function | God function 'get_learning_bias': complexity=14 (limit 10) |

### ✅ `D:\福昶工作目录\彩票系统\utils\rate_limit.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 11.5/100
- **LDR**: 84.6%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 11 | 🟠 high | pass_placeholder | Empty function with only pass - placeholder not implemented |

### ✅ `D:\福昶工作目录\彩票系统\src\ab_testing.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 10.6/100
- **LDR**: 100.0%
- **DDC**: 83.3%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 21 | 🟠 high | god_function | God function 'create_ab_snapshot': 94 logic lines (limit 50) |
| 242 | 🟡 medium | god_function | God function 'generate_ab_report': 58 logic lines (limit 50) |

### ✅ `D:\福昶工作目录\彩票系统\src\smart_filters.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 10.0/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 225 | 🟠 high | god_function | God function 'apply_smart_filters_ssq': complexity=13 (limit |
| 277 | 🟠 high | god_function | God function 'apply_smart_filters_dlt': complexity=17 (limit |

### ✅ `D:\福昶工作目录\彩票系统\backups\codex-20260606-restore-missing-modules\src\recommender.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 10.0/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 51 | 🟠 high | god_function | God function 'recommend_ssq': complexity=12 (limit 10) |
| 105 | 🟠 high | god_function | God function 'recommend_dlt': complexity=12 (limit 10) |

### ✅ `D:\福昶工作目录\彩票系统\backups\codex-20260606-before-sync-vps-0.8.8\src\recommender.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 10.0/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 51 | 🟠 high | god_function | God function 'recommend_ssq': complexity=12 (limit 10) |
| 105 | 🟠 high | god_function | God function 'recommend_dlt': complexity=12 (limit 10) |

### ✅ `D:\福昶工作目录\彩票系统\src\persistence.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 7.3/100
- **LDR**: 99.2%
- **DDC**: 85.7%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 102 | 🟡 medium | empty_except | Empty handler for 'Exception' silently discards the exceptio |
| 50 | 🟡 medium | phantom_import | Undeclared optional dependency: 'qcloud_cos' is guarded with |

### ✅ `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\src\learning.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 7.0/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 22 | 🟡 medium | god_function | God function 'build_learning_profile': 67 logic lines (limit |
| 112 | 🟠 high | god_function | God function 'get_learning_bias': complexity=14 (limit 10) |

### ✅ `D:\福昶工作目录\彩票系统\backups\codex-20260606-restore-missing-modules\src\learning.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 7.0/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 22 | 🟡 medium | god_function | God function 'build_learning_profile': 59 logic lines (limit |
| 100 | 🟠 high | god_function | God function 'get_learning_bias': complexity=14 (limit 10) |

### ✅ `D:\福昶工作目录\彩票系统\backups\codex-20260606-before-sync-vps-0.8.8\src\learning.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 7.0/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 22 | 🟡 medium | god_function | God function 'build_learning_profile': 59 logic lines (limit |
| 100 | 🟠 high | god_function | God function 'get_learning_bias': complexity=14 (limit 10) |

### ✅ `D:\福昶工作目录\彩票系统\src\signals_dlt.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 5.0/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 1 | 🟠 high | function_clone_cluster | 5 structurally similar functions detected (AST JSD < 0.05):  |

### ✅ `D:\福昶工作目录\彩票系统\hit_rate_helpers.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 2.0/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 39 | 🟡 medium | god_function | God function 'recent_hit_summary': 58 logic lines (limit 50) |

### ✅ `D:\福昶工作目录\彩票系统\src\db.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 2.0/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 606 | 🟡 medium | god_function | God function 'get_pool_stats': 58 logic lines (limit 50) |

### ✅ `D:\福昶工作目录\彩票系统\VERSION_RECORDS\V0.10.0-20260606\source-snapshot\hit_rate_helpers.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 2.0/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 40 | 🟡 medium | god_function | God function 'recent_hit_summary': 58 logic lines (limit 50) |

### ✅ `D:\福昶工作目录\彩票系统\src\backtest\random_baseline.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 2.0/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 75 | 🟡 medium | god_function | God function 'run_random_backtest': 70 logic lines (limit 50 |

### ✅ `D:\福昶工作目录\彩票系统\src\backtest\engine.py`

- **状态**: CLEAN (健康)
- **缺陷分**: 1.0/100
- **LDR**: 100.0%
- **DDC**: 100.0%

| 行号 | 严重度 | 规则 | 问题描述 |
|------|--------|------|----------|
| 43 | 🟢 low | god_function | God function 'backtest_ssq': 51 logic lines (limit 50) |

---

## 四、修复建议

### 🔴 P0 (必须修复)

1. **nested_complexity** (20处) — 深嵌套+高复杂度
   - 修复: 提取子函数、使用 early return、减少嵌套
2. **bare_except** (5处) — 裸 except 捕获所有异常
   - 修复: 改为 `except Exception:` 或捕获具体异常

### 🟠 P1 (建议修复)

1. **phantom_import** (110处) — 导入了不存在的模块
   - 修复: 添加 src 到 packages 配置，或使用相对导入
2. **god_function** (86处) — 函数太长或太复杂
   - 修复: 拆分为多个职责单一的小函数
3. **deep_nesting** (20处) — 嵌套太深
   - 修复: 使用 guard clause、提取子函数
4. **global_statement** (8处) — 使用 global 语句
   - 修复: 改为函数参数或类属性

### 🟡 P2 (可选优化)

1. **function_clone_cluster** (6处) — 克隆函数簇
   - 修复: 提取公共逻辑到基类或工具函数
2. **pass_placeholder** (3处) — 空函数占位
   - 修复: 实现函数或标记为 abstract
3. **empty_except** (3处) — 空 except 块
   - 修复: 至少记录日志: `except Exception as e: logger.error(e)`

---

## 五、评分说明

| 维度 | 权重 | 说明 |
|------|------|------|
| LDR (逻辑密度) | 40% | 代码行占比，越高越好 |
| ICR (膨胀检测) | 30% | 注释空话 vs 实际复杂度 |
| DDC (依赖使用) | 20% | 实际使用的导入占比 |
| Purity (纯度) | 10% | 严重问题的指数衰减 |

**判定等级**: CLEAN (<30) → SUSPICIOUS (30-50) → INFLATED (50-70) → CRITICAL (≥70)

---
*报告由智检 (zhijian) v1.0.0 自动生成 — 2026-07-31 16:52:09*