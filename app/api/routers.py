from fastapi import APIRouter

from app.api.endpoints.product import router as product_router
from app.api.endpoints.sales_report import router as sales_report_router

main_router = APIRouter()
main_router.include_router(
    product_router,
    prefix='/product',
    tags=['Product']
)
main_router.include_router(
    sales_report_router,
    prefix='/openai',
    tags=['OpenAI']
)
