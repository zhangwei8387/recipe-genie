# 软件需求规格说明书（SRS） - RecipeGenie

> 版本：v1.0（草案）
> 基于：`docs/requirements/PRODUCT_REQUIREMENTS.md`（v1.0 MVP）
> 作者：@zhangwei8387（协同）
> 最后更新：2025-12-27

## 目录
1. 概述
2. 范围与目标
3. 术语与缩写
4. 相关文档
5. 利益相关者
6. 功能性需求（详细）
7. 非功能性需求（NFR）
8. 接口与数据模型（API stub / schema）
9. 验收标准与测试用例（traceable）
10. 安全、隐私与食品安全审查规则
11. 交付物与里程碑
12. 追溯矩阵（需求 → 用户故事 → 测试）
13. 变更记录

---

## 1. 概述
本 SRS 将 PRD 中的高层需求细化为可交付的、可测试的工程需求（功能性与非功能性），并给出 API contract、数据模型、验收测试用例与安全审查规则。SRS 的目标是为开发、测试与验收提供明确规范。

## 2. 范围与目标
- 本版本覆盖 **MVP 范围**（见 PRD §5.7）：AI 实时交互式菜谱界面（Recipe View）与聊天面板（Chat Panel），以及 Mock Transform API 支持的基本指令（替换食材、调整做法）。
- 不包含：AI 生成图片、真实模型接入（标注为后续迭代）。

## 3. 术语与缩写
- PRD: 产品需求说明书
- SRS: 软件需求规格说明书
- MVP: 最小可行产品
- API: 应用程序编程接口

## 4. 相关文档
- `docs/requirements/PRODUCT_REQUIREMENTS.md`（主 PRD）
- `docs/requirements/user_stories.md`（用户故事）
- `docs/requirements/user_interviews/`（访谈数据）
- `docs/api/openapi.yaml`（API 规范 - 待补全）

## 5. 利益相关者
- 产品：@zhangwei8387
- 设计：@designer
- 开发：@dev
- 测试：@qa
- 安全/合规/运营：@ops

## 6. 功能性需求（详细）
每项需求均分配唯一 ID，后续变更需更新变更记录与 traceability 矩阵。

### FR-1 食材反推搜索
- 描述：用户输入/选择食材，系统在 <=3 秒返回 Top 5 候选食谱（含匹配度、步骤、时长、营养摘要）。
- 输入：食材列表（文本/标签）
- 输出：候选食谱数组（id、title、match_score、estimated_time、nutrition_summary）
- 依赖：样例食谱数据集
- 验收：见测试用例 TC-FR-1

### FR-2 时间限制过滤
- 描述：用户指定时间窗口（例如 20–30 分钟），系统返回在该时间内可执行的食谱。
- 验收：见 TC-FR-2

### FR-3 营养目标过滤
- 描述：用户可以按营养目标（低卡/高蛋白等）过滤或优先排序推荐。
- 验收：见 TC-FR-3（准确性误差 ≤ ±10% 基于营养数据源）

### FR-4 实时对话式修改（Transform）
- 描述：用户通过 Chat Panel 发送自然语言指令（替换食材/调整做法），系统返回修改后的 recipe，并更新页面。
- 支持的操作（MVP）：
  - replace_ingredient (e.g., "replace chicken with tofu")
  - adjust_method (e.g., "reduce oil")
- 输出：modified_recipe, change_summary (what changed & why)
- 性能要求：变更结果在 <=3s（目标 1–2s）内返回（MVP 可容忍短暂延迟）
- 验收：见 TC-FR-4

### FR-5 灵感模式（Random/Quick Suggestions）
- 描述：当用户希望快速得到简易建议时，系统提供“灵感/随机推荐”模式，优先生成步骤简洁、准备材料少的菜谱。
- 验收：见 TC-FR-5

### FR-6 变更历史与可审计
- 描述：每次用户与 AI 的交互（prompt、上下文快照、结果）被保存为审计日志，格式可用于回放与复核。
- 存放位置：`docs/ai-prompts/`（prompt.md、generated_files.txt 等）或持久化存储。
- 验收：见 TC-FR-6

## 7. 非功能性需求（NFR）
- NFR-1 性能
  - 推荐响应：平均 < 1s（目标），95 百分位 < 3s（示例目标）
  - 对话/Transform 延迟：平均 < 2s（目标）
- NFR-2 可用性
  - 目标可用性：99.9%（生产环境）
- NFR-3 可维护性
  - 代码应包含单元测试并符合仓库的代码风格
- NFR-4 可追溯性与日志
  - 所有生成（prompt/response）需保存且可查询（审计）
- NFR-5 安全与隐私
  - 所有敏感用户数据需使用传输层加密（TLS）并遵循最小权限原则

## 8. 接口与数据模型（API stub / schema）
### 8.1 Recipe JSON（示例）
```json
{
  "id": "recipe-001",
  "title": "Grilled Chicken Salad",
  "ingredients": [
    {"name":"chicken breast","quantity":"200g"},
    {"name":"mixed greens","quantity":"3 cups"}
  ],
  "steps": ["Season chicken","Grill chicken","Toss salad"],
  "nutrition": {"calories":450, "protein":35, "fat":20, "carbs":20}
}
```

### 8.2 API Contract (MVP stubs)
- GET /api/recipes/{id}
  - Response: Recipe JSON
- POST /api/recipes/{id}/transform
  - Request: { "instruction": "replace chicken with tofu", "context": {"recipe": <Recipe JSON>} }
  - Response: { "modified_recipe": <Recipe JSON>, "change_summary": "Replaced chicken with tofu; calories -80kcal" }

> 注：请将以上契约与 `docs/api/openapi.yaml` 同步（优先级：高）

## 9. 验收标准与测试用例
以下示例测试用例需要在 CI 或手动验收中执行并记录结果。

- TC-FR-1: 食材反推
  - 准备：使用已知样例库
  - 操作：请求 /api/recipes?ingredients=chicken,tomato
  - 期望：返回 Top5，Top1 可执行性通过人工抽样 ≥90%

- TC-FR-4: 替换食材（基本）
  - 操作：POST /api/recipes/recipe-001/transform {instruction: "replace chicken with tofu"}
  - 期望：返回 modified_recipe，ingredients 中鸡肉被豆腐替换；nutrition.calories 降低且 change_summary 可读

- TC-FR-5: 灵感模式
  - 操作：调用 Quick Suggest API（或变换参数）
  - 期望：返回步骤≤3，准备材料≤3

## 10. 安全、隐私与食品安全审查规则
- 对于任何可能影响食品安全/健康的建议（例如未煮熟食品、过敏原替换、营养警告），系统应标注 `Requires human safety review`，并在生产流程中强制要求人工确认。审查记录应与交互日志一起保存。
- 明确谁是人工审核者（岗位/人员），并在 PRD/SRS 中记录负责人（示例：@ops）。

## 11. 交付物与里程碑（MVP）
- M1（2 周）：实现 RecipeView + Mock Transform API + ChatPanel，包含 2 个示例指令的演示。
- M2（4 周）：变更历史保存、测试套件与内部验收。

## 12. 追溯矩阵（示例）
| Requirement ID | Source User Story | Test Case ID |
| --- | --- | --- |
| FR-1 | US-001 | TC-FR-1 |
| FR-4 | US-003 | TC-FR-4 |
| FR-5 | US-002 | TC-FR-5 |

## 13. 变更记录
- v1.0（2025-12-27）: SRS 初稿（基于 PRD v1.0）

---

**备注**：初稿完成后建议尽快组织一次 SRS 评审（产品/开发/QA/安全）并在评审中把上表的优先级、测试负责人与验收细节具体化。