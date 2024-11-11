from fastapi import APIRouter

from app.api.endpoints.product import router as product_router
from app.api.endpoints.openai import router as openai_router

main_router = APIRouter()
main_router.include_router(
    product_router,
    prefix='/product',
    tags=['Product']
)
main_router.include_router(
    openai_router,
    prefix='/openai',
    tags=['OpenAI']
)
