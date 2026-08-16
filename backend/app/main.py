from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db
from app.api.auth import router as auth_router

app = FastAPI(
    title=settings.app_name,
    description="AI-powered personal finance assistant API",
    version="0.1.0",
)

app.include_router(auth_router)

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    """
    Liveness check that also verifies database connectivity.
    """
    db_status = "ok"
    try:
        db.execute(text("SELECT 1"))
    except Exception:
        db_status = "unreachable"

    return {
        "status": "ok",
        "app": settings.app_name,
        "environment": settings.environment,
        "database": db_status,
    }