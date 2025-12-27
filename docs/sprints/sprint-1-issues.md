# Sprint 1 - Issue 草稿（AI 实时交互菜谱 MVP）

以下是可直接在 GitHub 上创建的 Issue 草稿（标题、描述、验收标准）。网络恢复后我可以代为创建这些 Issue。

---

## Issue 1: feat: add `RecipeView` static component
- 描述：实现菜谱视图组件，包含标题、食材卡片、步骤列表与营养概览，支持从 `/api/recipes/{id}` 获取数据并渲染。
- 验收标准：
  - 页面能渲染 `data/sample_recipe.json` 中的内容。
  - 组件独立且有 Storybook（可选）示例。
- 标签：`frontend`, `feature`, `estimate:2`

---

## Issue 2: feat: implement Mock Transform API
- 描述：后端实现 `POST /api/recipes/{id}/transform` 支持两类操作：`replace_ingredient` 与 `adjust_method`，返回修改后的 recipe 对象与变更摘要。
- 验收标准：
  - 对 `replace_ingredient` 请求返回包含修改后 ingredients 和 recalculated nutrition 的 JSON。
  - 包含单元测试覆盖常见替换场景（鸡肉→豆腐、减少油量）。
- 标签：`backend`, `feature`, `estimate:2`

---

## Issue 3: feat: ChatPanel + integration
- 描述：实现前端聊天面板，支持发送用户指令并调用 Transform API，接收结果后更新 `RecipeView`，同时展示变更摘要并保存 prompt 到 `docs/ai-prompts/`。
- 验收标准：
  - 聊天输入发送后，页面显示变更摘要并更新相应部分（食材/步骤/营养）。
  - 保存 prompt 与响应到 `docs/ai-prompts/` 下的文件。
- 标签：`frontend`, `integration`, `estimate:2`

---

## Issue 4: test: add unit & API tests for transform logic
- 描述：为 Mock Transform 实现添加单元测试，增加 API 层的集成测试，并配置一个简单的 E2E 脚本（替换示例流程）。
- 验收标准：
  - 单元测试覆盖率覆盖转换函数常见路径。
  - E2E 测试能在 CI 环境中运行（本地验证后可在 CI 中集成）。
- 标签：`test`, `estimate:1`

---

## Issue 5: chore: add `docs/ai-prompts/` and prompt templates
- 描述：创建 `docs/ai-prompts/` 目录与模板文件（`prompt.md`, `context.md`, `generated_files.txt`）用于保存生成记录。
- 验收标准：
  - 模板文件齐全，并在示例交互中使用。
- 标签：`docs`, `chore`, `estimate:0.5`

---

## Issue 6: e2e: add simple flow test ("replace chicken with tofu")
- 描述：添加 E2E 测试，模拟用户在 ChatPanel 输入替换命令并断言页面更新。
- 验收标准：
  - 测试通过且能在本地/CI 运行。
- 标签：`e2e`, `test`, `estimate:1`

---

（备注：我可以在网络恢复后为你在 GitHub 上创建这些 Issue，并把每个 Issue 指派给负责人与填写估时标签。）