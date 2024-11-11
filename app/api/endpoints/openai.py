from fastapi import APIRouter, Depends, Request
import openai
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.db import get_session
from app.crud.sales_report import create_sales_report
from app.services.xml import generate_prompt


router = APIRouter()

OPENAI_API_KEY = settings.openai_api_key
OPENAI_API_URL = settings.openai_api_url


@router.post('/generate_analytics')
async def ask_claude(
    request: Request,
    session: AsyncSession = Depends(get_session)
):
    '''
    Отправляет запрос к Openai API для генерации аналитики продуктов.
    '''
    prompt = generate_prompt()
    client = openai.OpenAI(
        api_key=OPENAI_API_KEY,
        base_url='https://api.proxyapi.ru/openai/v1'
    )
    message = client.chat.completions.create(
        model='gpt-3.5-turbo',
        max_tokens=500,
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )
    report = message.choices[0].message.content
    await create_sales_report(report, session)
    return report
