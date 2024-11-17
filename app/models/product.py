from sqlalchemy import Column, Float, Integer, String

from app.core.db import Base


class Product(Base):
    '''Модель продукта.'''
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(
        255),
        unique=True,
        nullable=False
    )
    quantity = Column(Integer)
    price = Column(Float)
    category = Column(String)
