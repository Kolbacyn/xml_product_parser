import asyncio

from celery import Celery
from celery.schedules import crontab

import openai

from app.api.endpoints.sales_report import generate_prompt, get_current_date
from app.core.config import settings
from app.core.db import AsyncSessionLocal
from app.models.sales_report import SalesReport
from app.schemas.sales_report import SalesReportCreate
from app.services import constants
from app.services.constants import Numerics

celery = Celery(__name__)
celery.conf.broker_url = settings.celery_broker_url
celery.conf.result_backend = settings.celery_result_backend
celery.conf.timezone = constants.TIMEZONE
celery.conf.broker_connection_retry_on_startup = True
celery.conf.beat_schedule = {
    'everyday_task': {
        'task': 'celery_worker.generate_daily_analytics',
        'schedule': crontab(
            hour=Numerics.TASK_HOURS,
            minute=Numerics.TASK_MINUTES
        ),
    }
}


@celery.task
def generate_daily_analytics():
    '''
    Функция, выполняемая Celery раз в сутки.
    '''
    asyncio.run(async_task())


async def async_task():
    '''
    Асинхронная функция для передачи в задачи Celery.
    '''
    prompt = generate_prompt()
    match prompt:
        case None:
            raise ValueError('Промпт не может быть None')
    client = openai.OpenAI(
        api_key=settings.openai_api_key,
        base_url='https://api.proxyapi.ru/openai/v1'
    )
    match client:
        case None:
            raise ValueError('Ошибка при попытке создания экземпляра OpenAI')
    try:
        message = client.chat.completions.create(
            model=constants.LLL_MODEL,
            max_tokens=constants.Numerics.TOKENS_QUANTITY,
            messages=[
                {'role': 'user', 'content': prompt}
            ]
        )
    except Exception as e:
        raise Exception(f'Ошибка при обращении к API {e}') from e
    match message:
        case None:
            raise ValueError('Ошибка при обращении к API OpenAI')
    try:
        async with AsyncSessionLocal() as session:
            date = get_current_date()
            match date:
                case None:
                    raise ValueError('Дата не может быть None')
            report = message.choices[0].message.content
            match report:
                case None:
                    raise ValueError('Отчет не может быть None')
            to_base = SalesReport(report=report, date=date)
            match to_base:
                case None:
                    raise ValueError('SalesReport не может быть None')
            session.add(to_base)
            await session.commit()
            await session.refresh(to_base)
    except Exception as e:
        print(f'Ошибка: {e}')
    return SalesReportCreate(report=report, date=date)
