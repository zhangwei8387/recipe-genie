# 1. 采用 Angular + FastAPI + AutoGen 技术栈

日期: 2025-12-27

## 状态

已接受 (Accepted)

## 背景

项目需要构建一个智能食谱生成应用，核心需求包括：
1.  富交互的前端界面（SPA）。
2.  高性能后端，需支持异步操作。
3.  复杂的 AI 交互逻辑，需要多智能体协作（Multi-Agent）。
4.  快速迭代 MVP，初期数据量不大。

## 决策

我们决定采用以下技术栈：

1.  **前端框架**: **Angular**
    *   理由: 团队（或用户）偏好，强类型 (TypeScript) 支持完善，适合构建大型企业级应用，内置依赖注入和模块化管理。
2.  **后端框架**: **FastAPI (Python)**
    *   理由: Python 是 AI 领域的首选语言；FastAPI 性能优异，原生支持异步 (AsyncIO)，方便与 AI 库集成，且自动生成 OpenAPI 文档。
3.  **AI 框架**: **Microsoft Agent Framework**
    *   理由: 微软最新推出的统一智能体框架（AutoGen 与 Semantic Kernel 的继任者），结合了 AutoGen 的智能体抽象与 Semantic Kernel 的企业级特性，支持强类型的多智能体工作流编排。
4.  **数据库**: **SQLite** (MVP 阶段)
    *   理由: 零配置，单文件存储，极低运维成本，适合 MVP 快速验证。使用 SQLModel/SQLAlchemy 可在未来无缝迁移至 PostgreSQL。

## 后果

### 积极影响
*   前后端分离，开发解耦。
*   Python 后端能直接调用 AI 模型和工具，无需跨语言桥接。
*   AutoGen 提供了现成的 Agent 抽象，减少了从头开发多智能体系统的成本。
*   SQLite 降低了初期部署复杂度。

### 消极影响/风险
*   Angular 学习曲线相对较陡（相比 Vue/React）。
*   AutoGen 相对较新，API 可能发生变化，需关注版本更新。
*   SQLite 在高并发写操作下有锁限制（但在 MVP 阶段可接受）。
