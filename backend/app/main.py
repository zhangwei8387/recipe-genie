from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="RecipeGenie API",
    description="Backend for RecipeGenie - 食谱精灵",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# CORS Configuration
origins = [
    "http://localhost:4200",  # Angular default port
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
async def health_check():
    """
    Health check endpoint to verify backend status.
    """
    return {"status": "ok", "message": "RecipeGenie Backend is running"}

# Placeholder for AG-UI integration
# In a real implementation, we would import the agent router and mount it.
# Example:
# from app.api.agent_router import agent_router
# app.include_router(agent_router, prefix="/api/v1/agent")
