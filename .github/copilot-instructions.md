# GitHub Copilot 指南 — RecipeGenie

目的：帮助 AI 编码代理（Copilot / CodeGen agents）在此仓库以“Vibe Coding”方式高效、安全地生成可合并代码和文档。

## 一览（大局）
- 目前仓库以 **文档优先**（docs/）为主：所有功能先在 `docs/requirements/PRODUCT_REQUIREMENTS.md` 中定义验收标准后再实现。
- 建议技术栈（见 `docs/architecture/architecture_overview.md`）：前端 React/Vue，后端 Node.js / Python (FastAPI)，数据库 Postgres / MongoDB，AI 服务（模型或第三方 API）。
- 关键集成点（在 PRD/架构文档中列出）：营养数据 API、图像生成模型、AI 推荐/对话服务。

## 发现的关键文件和约定（立即可用）
- 需求与验收：`docs/requirements/PRODUCT_REQUIREMENTS.md`（必须遵循的验收条件，如响应时延、样本通过率等）。
- API 起点：`docs/api/openapi.yaml`（空模板，优先补全端点描述）
- Sprint/任务模板：`docs/templates/sprint_task_template.md`、`docs/sprints/sprint-1.md`（把自动生成任务写入此处）。
- Issue / PR 模板参考：`docs/templates/issue_template.md`（用于生成标准化 PR 描述）。
- 视觉/组件参考：`docs/design/design_system.md`。

## 工作流规则（必须遵守）
1. **文档优先**：在生成任何功能代码前，确认相关 PRD/用户故事与验收标准已在 `docs/` 中明确。PR 必须在描述中引用相关文档条目（例如：`PRODUCT_REQUIREMENTS.md#5.4`）。
2. **代码质量门**：生成代码必须包含相应测试（单元/集成）并通过 CI（lint + tests），并至少由一名人类审查者批准后才能合并。
3. **提交规范**：使用 Conventional Commits（例如：`feat: add recipe recommendation endpoint`）。分支命名遵循 `feature/*` / `fix/*`。
4. **记录生成痕迹**：把用于生成的 prompts、参数与审查备注保存到 `docs/ai-prompts/`（新建），包含字段：`prompt.md`（prompt 文本）、`context.md`（相关文件/PRD 链接）、`generated_files.txt`、`reviewer`、`tests_passed`。
5. **食品/营养/安全相关内容**：任何影响健康或包含安全建议的改动必须有人工签核，且在 PR 描述中明确标注“Requires human safety review”。

## 可执行示例（task templates for AI agents）
- 生成 OpenAPI endpoints（优先级高）：
  - 创建 `paths`：`/recipes`、`/recommendations`、`/recipes/{id}`、`/users/{id}/preferences`；在 `docs/api/openapi.yaml` 中补全示例请求/响应与 schema。
  - 在同一 PR 中，生成后端路由（FastAPI 或 Express）与基础测试用例（pytest 或 jest）。
- 生成前端组件（展示食谱）示例：
  - `RecipeCard` 组件：显示**标题、主要食材、步骤摘要、营养概览、图片**，并提供“替换食材/调整份量”交互入口。
  - 提供 Storybook 示例或基于 `docs/design/design_system.md` 的 CSS 变量映射。
- 将 PRD 验收条件自动转化为测试用例：例如 `input 食材 -> top 5 推荐 <= 3s` 可转为集成测试（模拟数据 + 时间断言）。

## 生成/审查建议（对 Copilot 的具体提示）
- 始终在 PR 描述里包含：**(1)** 用到的 prompt（或引用 `docs/ai-prompts/`），**(2)** 变更的文件列表，**(3)** 测试说明与运行命令。示例描述模板参见 `docs/templates/issue_template.md`。
- 当生成 API 时，引用 `PRODUCT_REQUIREMENTS.md` 中的“验收标准”字段并把对应断言写入测试。
- 对于复杂的替换/对话逻辑（例如："把鸡肉换成豆腐"），生成单元测试覆盖：食谱变体生成、营养重新计算、过敏项提示。

## 限制与不可做的事
- 不要直接修改 `docs/requirements/PRODUCT_REQUIREMENTS.md` 的核心验收条目，除非 PR 明确指出并由产品负责人批准。
- 不要修改安全/隐私策略（如加密或密钥管理）而不先在 PR 中声明风险与审核人。

## PR 格式（快速模板）
- 标题：`feat|fix: 简短描述 (#issue)`
- 描述：
  - 变更点摘要
  - 关联 PRD 条目（链接）
  - 生成 prompt 或脚手架说明（若使用 AI 生成）
  - 测试说明（包括如何在本地运行）
  - 审查清单（CI 通过、测试覆盖、审查者）

## 额外资源与下一步
- 新增目录：请将生成的 prompts 与验证记录放入 `docs/ai-prompts/`（我可以帮你创建此目录并放置模板）。

---

请检查上述指南是否覆盖了你希望 Copilot 遵守的要点，或告诉我需要补充的具体规则或示例（例如：你希望我们支持哪种测试框架或前端库）。我会据此更新并提交 `.github/copilot-instructions.md` 的迭代版本。