# 系统架构概览 (System Architecture Overview)

## 1. 架构愿景
RecipeGenie 旨在构建一个基于多智能体（Multi-Agent）协作的智能食谱生成与助手平台。系统采用前后端分离架构，前端使用 **Angular** 构建响应式单页应用（SPA），后端采用 **FastAPI** 提供高性能 RESTful API，并集成 **Microsoft AutoGen** 作为多智能体编排框架。数据持久化在 MVP 阶段使用 **SQLite**。

## 2. 技术栈 (Technology Stack)

| 组件 | 技术选型 | 说明 |
| :--- | :--- | :--- |
| **Frontend** | **Angular** (Latest) | 强类型、模块化、适合构建复杂交互的 SPA。使用 RxJS 处理异步流。 |
| **Backend** | **Python 3.10+** / **FastAPI** | 高性能、易于集成 AI 库、原生支持异步 (AsyncIO)。 |
| **AI Framework** | **Microsoft AutoGen** | 支持多智能体对话、任务编排与协作。 |
| **Database** | **SQLite** (MVP) | 轻量级、零配置，适合 MVP 快速迭代。未来可迁移至 PostgreSQL。 |
| **ORM** | **SQLModel** (or SQLAlchemy) | 结合 Pydantic 与 SQLAlchemy，完美契合 FastAPI。 |
| **Task Queue** | (Optional for MVP) | 暂不引入复杂 MQ，利用 Python `asyncio` 处理并发，必要时引入 Redis + Celery。 |

## 3. 系统容器图 (Container Diagram)

```mermaid
graph TD
    User[用户 (Web Browser)]
    
    subgraph "Frontend (Angular)"
        UI[Web App]
        AuthService[Auth Service]
        RecipeService[Recipe Service]
        ChatService[Chat Service]
    end
    
    subgraph "Backend (FastAPI)"
        API[API Gateway / Router]
        
        subgraph "Application Layer"
            UserManager[User Manager]
            RecipeManager[Recipe Manager]
            ChatManager[Chat Manager]
        end
        
        subgraph "AI Agent Layer (AutoGen)"
            Orchestrator[User Proxy / Orchestrator Agent]
            ChefAgent[Chef Agent (Recipe Gen)]
            NutritionistAgent[Nutritionist Agent]
            ReviewerAgent[Reviewer Agent]
        end
        
        DB_Adapter[Database Adapter (SQLModel)]
    end
    
    subgraph "Data Persistence"
        SQLite[(SQLite Database)]
    end
    
    subgraph "External Services"
        LLM_API[LLM API (OpenAI/Azure)]
    end

    User -->|HTTPS| UI
    UI -->|REST / WebSocket| API
    API --> UserManager
    API --> RecipeManager
    API --> ChatManager
    
    ChatManager <-->|Task Handoff| Orchestrator
    Orchestrator <-->|Conversation| ChefAgent
    Orchestrator <-->|Conversation| NutritionistAgent
    Orchestrator <-->|Conversation| ReviewerAgent
    
    ChefAgent -.->|API Call| LLM_API
    NutritionistAgent -.->|API Call| LLM_API
    
    UserManager --> DB_Adapter
    RecipeManager --> DB_Adapter
    DB_Adapter --> SQLite
```

## 4. 核心模块设计

### 4.1 前端 (Angular)
- **Core Module**: 单例服务（Auth, Logger, Config）。
- **Shared Module**: 通用组件（UI Kit, Pipes, Directives）。
- **Features Modules**:
  - `RecipeModule`: 食谱列表、详情、收藏。
  - `ChatModule`: 智能助手对话界面，流式消息展示。
  - `UserModule`: 个人中心、偏好设置。

### 4.2 后端 (FastAPI)
- **Routers**: 定义 RESTful 接口 (`/api/v1/recipes`, `/api/v1/chat`, `/api/v1/auth`)。
- **Models**: Pydantic 模型用于请求/响应验证，SQLModel 用于数据库映射。
- **Dependencies**: 依赖注入（DB Session, Current User）。

### 4.3 多智能体架构 (Multi-Agent System)
利用 AutoGen 构建协作流：
1.  **User Proxy Agent**: 接收用户输入，作为会话管理者。
2.  **Chef Agent (主厨)**: 负责根据需求生成食谱步骤和配料。
3.  **Nutritionist Agent (营养师)**: 分析食谱营养成分，提出健康建议。
4.  **Reviewer Agent (审核员)**: 检查食谱的合理性与安全性（如过敏原）。

**工作流示例**:
用户输入: "我想吃低脂的鸡肉晚餐" -> `User Proxy` -> `Chef Agent` (生成草稿) -> `Nutritionist Agent` (计算卡路里并建议减少油量) -> `Chef Agent` (修改食谱) -> `User Proxy` (返回最终结果)。

## 5. 数据模型 (Data Schema - MVP)

- **User**: `id`, `username`, `email`, `preferences` (JSON)
- **Recipe**: `id`, `title`, `ingredients` (JSON), `steps` (JSON), `nutrition_info` (JSON), `created_by`
- **ChatSession**: `id`, `user_id`, `created_at`
- **ChatMessage**: `id`, `session_id`, `role` (user/assistant/agent_name), `content`, `timestamp`

## 6. 部署架构 (Deployment)
- **Local Dev**: Docker Compose 编排 Frontend (Nginx/Node) + Backend (Python) + (Optional) Redis.
- **Production**: 
  - Frontend: 静态资源托管 (S3/CDN/Nginx).
  - Backend: Docker 容器化部署 (K8s/Docker Swarm/Cloud Run).
  - Database: 挂载持久化卷 (Volume) 或迁移至云数据库。
