# """
# Main entry point for the NextGenHealth FastAPI application.
#
# Configures the FastAPI app, connects to PostgreSQL, and sets up routes.
# Follows Clean Architecture: presentation layer depends on application and infrastructure.


from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.api.routes.user_routes import router as user_router

import logging

# Adicione esta linha logo após a importação do logging
logging.basicConfig(level=logging.DEBUG) # ou level=logging.INFO para menos detalhes

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(
    title="NextGenHealth API",
    description="API for the NextGenHealth user management system, built with DDD and Clean Architecture.",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the NextGenHealth API"}
