# src/api/main.py
"""
Main entry point for the NextGenHealth FastAPI application.

Configures the FastAPI app, connects to PostgreSQL, and sets up routes.
Follows Clean Architecture: presentation layer depends on application and infrastructure.
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

# ✅ Agora importa router diretamente — sem circular import
from api.routes.user_routes import router as user_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting NextGenHealth API...")
    yield
    logger.info("Shutting down NextGenHealth API...")


app = FastAPI(
    title="NextGenHealth API",
    description="API for the NextGenHealth user management system, built with DDD and Clean Architecture.",
    version="0.1.0",
    lifespan=lifespan
)

# ✅ Injeta dependência compartilhada
from api.dependencies import get_db_session

app.include_router(user_router)
app.dependency_overrides[get_db_session] = get_db_session


@app.get("/")
async def root():
    return {"message": "Welcome to the NextGenHealth API"}