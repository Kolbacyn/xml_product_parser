from fastapi import FastAPI

from app.api import router
from app.core.config import settings

app = FastAPI(
    title=settings.app_title,
    version=settings.app_version
)

app.include_router(router)
