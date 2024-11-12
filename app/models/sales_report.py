from sqlalchemy import Column, Integer, String

from app.core.db import Base
from app.services.constants import Numerics


class SalesReport(Base):
    '''Модель отчета о продажах.'''
    __tablename__ = 'sales_reports'

    id = Column(Integer, primary_key=True)
    report = Column(String(Numerics.ANALYTICS_LENGTH), nullable=False)
    date = Column(String(Numerics.DATE_LENGTH), nullable=False)
