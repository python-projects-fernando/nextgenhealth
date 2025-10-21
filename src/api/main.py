# """
# Main entry point for the NextGenHealth FastAPI application.
#
# Configures the FastAPI app, connects to PostgreSQL, and sets up routes.
# Follows Clean Architecture: presentation layer depends on application and infrastructure.


from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.api.routes.patient_profile_routes import patient_router
from src.api.routes.user_routes import router as user_router

import logging

from user_management.infrastructure.database.postgres_config import engine
from user_management.infrastructure.models.user_model import Base as UserBase
from user_management.infrastructure.models.user_credentials_model import Base as CredentialsBase
from user_management.infrastructure.models.patient_profile_model import Base as PatientProfileBase

# Adicione esta linha logo após a importação do logging
logging.basicConfig(level=logging.DEBUG) # ou level=logging.INFO para menos detalhes

logger = logging.getLogger(__name__)



@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan manager for the FastAPI app.
    Handles startup and shutdown events.
    """
    logger.info("Starting NextGenHealth API...")
    # async with engine.begin() as conn:
    #     await conn.run_sync(UserBase.metadata.create_all)
    #     await conn.run_sync(CredentialsBase.metadata.create_all)
    #     await conn.run_sync(PatientProfileBase.metadata.create_all)
    yield
    logger.info("Shutting down NextGenHealth API...")


app = FastAPI(
    title="NextGenHealth API",
    description="API for the NextGenHealth user management system, built with DDD and Clean Architecture.",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(user_router)
app.include_router(patient_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the NextGenHealth API"}
