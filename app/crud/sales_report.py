from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.sales_report import SalesReport
from app.schemas.sales_report import SalesReportCreate, SalesReportDB
from app.services.xml import get_current_date


async def create_sales_report(
        report: SalesReportCreate,
        session: AsyncSession
) -> SalesReport:
    '''Создает новый отчет о продажах.'''
    report_date = await get_current_date()

    sales_report = SalesReport(
        report=report,
        date=report_date
    )
    session.add(sales_report)
    await session.commit()
    await session.refresh(sales_report)
    return sales_report


async def get_sales_report_by_date(
        report_date: str,
        session: AsyncSession
) -> SalesReportDB:
    report = await session.execute(
        select(SalesReport).where(SalesReport.date == report_date)
    )
    return report.scalars().first()
