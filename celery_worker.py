from celery import Celery
from celery.schedules import crontab
from sqlalchemy.ext.asyncio import AsyncSession
import openai

from app.api.endpoints.sales_report import generate_prompt
from app.crud.sales_report import create_sales_report
from app.core.db import get_session
from app.services import constants

from app.core.config import settings

celery = Celery(__name__)
celery.conf.broker_url = settings.celery_broker_url
celery.conf.result_backend = settings.celery_result_backend
celery.conf.broker_connection_retry_on_startup = True
celery.conf.beat_schedule = {
    'generate_daily_analytics': {
        'task': 'celery_worker.generate_daily_analytics',
        'schedule': crontab(hour=21, minute=50)
    }
}


@celery.task
async def generate_daily_analytics():
    """
    Функция, выполняемая Celery раз в сутки.
    """
    async with AsyncSession(get_session()) as session:
        prompt = generate_prompt()
        client = openai.OpenAI(
            api_key=settings.openai_api_key,
            base_url='https://api.proxyapi.ru/openai/v1'
        )
        message = client.chat.completions.create(
            model=constants.LLL_MODEL,
            max_tokens=constants.Numerics.TOKENS_QUANTITY,
            messages=[
                {'role': 'user', 'content': prompt}
            ]
        )
        report = message.choices[0].message.content
        await create_sales_report(report, session)
