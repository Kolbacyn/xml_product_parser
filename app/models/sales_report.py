from sqlalchemy import Column, Integer, String

from app.core.db import Base


class SalesReport(Base):
    '''Модель отчета о продажах.'''
    __tablename__ = 'sales_reports'

    id = Column(Integer, primary_key=True)
    report = Column(String(2000), nullable=False)
    date = Column(String(20), nullable=False)
