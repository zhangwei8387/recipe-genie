# PR 草稿：docs: add SOFTWARE_DEVELOPMENT_PLAN and PRODUCT_REQUIREMENTS

## 标题（建议）
`docs: add SOFTWARE_DEVELOPMENT_PLAN and PRODUCT_REQUIREMENTS`

## 概要
本次 PR 将仓库中的生命周期文档迁移并规范化为正式的软件开发计划，同时补充产品需求说明书与 Copilot 指南，调整 README，创建文档索引与模板，便于后续以“文档优先 / Vibe Coding”流程开展工作。

## 变更清单（重要文件）
- 新增/修改：
  - `docs/plans/SOFTWARE_DEVELOPMENT_PLAN.md`（迁移自 `docs/software-lifecycle.md`，并重命名为软件开发计划）
  - `docs/requirements/PRODUCT_REQUIREMENTS.md`（正式 PRD）
  - `docs/INDEX.md`（更新索引，指向新文档）
  - `README.md`（重构 README，加入 Vibe Coding 原则与快速开始）
  - `.github/copilot-instructions.md`（AI agent 指南）
  - `docs/templates/*`（issue / sprint 任务模板）
  - `docs/sprints/sprint-1.md`（示例 Sprint 任务）
- 说明变更：
  - `docs/software-lifecycle.md`（保留为迁移说明，已标注）

## 变更原因
- 将生命周期文档正式化、分层存放（`docs/plans/`），便于维护和审查。  
- 建立 PRD（`PRODUCT_REQUIREMENTS.md`）作为需求与验收标准的单一事实源（SoR），并把 AI agent 使用规范写入 `.github/copilot-instructions.md`，支持未来的 Vibe Coding 流程。

## 本地验证与检查（请在合并前执行）
- 语法/风格检查：对新增 Markdown 执行 markdownlint（或等价工具）。
- 内容检查：打开以下文件确认链接与相对路径正确：`docs/INDEX.md`、`docs/plans/SOFTWARE_DEVELOPMENT_PLAN.md`、`docs/requirements/PRODUCT_REQUIREMENTS.md`、`README.md`。  
- CI 说明：生成代码或脚手架时，确保生成的代码包含测试并在 CI 上通过（lint + tests）。

## 审查清单（Review checklist）
- [ ] 文档是否覆盖核心验收标准（PRD 中的 KPI 与验收项）
- [ ] README 的 Vibe Coding 指南是否准确反映仓库流程
- [ ] `.github/copilot-instructions.md` 是否满足本仓库对 AI agent 的约束与示例要求
- [ ] 模板文件（`docs/templates/`）是否满足团队流程并易于复制
- [ ] 已移除或迁移的旧文件是否标注清楚以避免断链

## 安全与合规注意点
- 任何与食品安全、营养建议或医疗相关的内容必须在 PR 描述中标注 `Requires human safety review` 并由产品/安全负责人进行审批。

## 推送与创建 PR（网络恢复后执行）
```bash
# 推送当前分支（本地分支名）
git push --set-upstream origin docs/plans-refactor

# 使用 GitHub CLI 创建 PR（示例）
gh pr create \
  --title "docs: add SOFTWARE_DEVELOPMENT_PLAN and PRODUCT_REQUIREMENTS" \
  --body "Add software development plan, product requirements and Copilot instructions. See docs/ for details. Reviewer: @zhangwei8387" \
  --base main --head docs/plans-refactor
```

---

如需我代为在网络恢复后执行推送并创建 PR，我可以在你允许时自动执行（或你也可手动运行上述命令）。如果你希望我将 PR 草稿内容写入 PR 描述并在创建 PR 时附上审查者，请告诉我审查者用户名列表。