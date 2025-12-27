# 架构概览

## 1. 上下文图（Context Diagram）
- 简要描述系统边界与外部依赖（用户、第三方 API、认证服务等）。

## 2. 容器图（Container Diagram）
- 前端：React / Vue
- 后端：Node.js / Python (FastAPI)
- AI 服务：模型服务或第三方 AI API
- 数据库：Postgres / MongoDB

## 3. 组件图（Component Diagram）
- 推荐服务
- 用户服务
- 食谱数据服务

## 4. 部署图
- 表示生产/测试环境、负载均衡、CDN、缓存层等。

## 5. 决策记录
- 在此记录关键架构决策以及权衡（ADR）。