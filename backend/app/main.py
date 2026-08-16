from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="AI-powered personal finance assistant API",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    """
    Basic liveness check. Returns app status and environment.
    Will later be extended to check database connectivity.
    """
    return {
        "status": "ok",
        "app": settings.app_name,
        "environment": settings.environment,
    }