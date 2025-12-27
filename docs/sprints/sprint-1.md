# Sprint 1 - AI 实时交互菜谱 MVP（Week 3-4）

## 目标
在两周内交付 AI 实时交互菜谱的最小可行产品（MVP）：包含菜谱视图、侧边 Chat 面板、Mock Transform API 与基本联动，以及测试用例与交互日志保存机制。

## 任务列表（优先级与估时）
1. 前端：静态 `RecipeView`（显示标题、食材卡片、步骤列表、营养概览） — 估时：1.5 天 — 负责人：待定
2. 后端：Mock Transform API（POST `/api/recipes/{id}/transform`）— 估时：1.5 天 — 负责人：待定
3. 前端：`ChatPanel`（输入框、历史、调用 Transform API 并更新视图）— 估时：1 天 — 负责人：待定
4. 集成：前端与后端联动 + sample recipe 数据 — 估时：0.5 天 — 负责人：待定
5. 持久化：交互日志与 prompt 保存到 `docs/ai-prompts/`（prompt.md、generated_files.txt）— 估时：0.5 天 — 负责人：待定
6. 测试：单元测试（转换函数）、API 测试 & 简单 E2E（替换/减少油流程）— 估时：1 天 — 负责人：待定
7. UX：UI 微调（交互高亮、变更摘要、提示信息）— 估时：0.5 天 — 负责人：待定
8. 文档：在 `docs/` 中新增操作说明与使用示例（含 PRD 中的示例用例）— 估时：0.5 天 — 负责人：待定

## 验收标准（每项应可被验证）
- 用户在页面上看到完整的菜谱信息（标题、食材、步骤、营养）。
- 在 ChatPanel 输入 "把鸡肉换成豆腐" 后，页面能在 <=3s 内更新食材、步骤与营养，并显示至少一条搭配提示与营养差异摘要（卡路里/蛋白变化）。
- 在 ChatPanel 输入 "减少油量" 后，步骤文本与营养（卡路里）发生可衡量的变化。
- 每次交互的 prompt、上下文快照与结果保存到 `docs/ai-prompts/`，且可供审查。
- 新增测试用例覆盖关键转换逻辑和一个 E2E 流程。

## 可交付物
- 前端组件代码（`src/components/RecipeView`, `src/components/ChatPanel`）
- 后端 Mock Transform 服务与 API 文档
- 示例数据（`data/sample_recipe.json`）与 prompt 保存样例
- 测试套件（单元+API+E2E）

## 备注
- 初期使用 Mock 规则引擎验证交互 UX，后续替换为真实 AI 模型（需 API Key 与安全评审）。
- 我可以把每一项拆成独立 Issue（草稿已生成 `sprint-1-issues.md`）。