from sqlalchemy import Column, Integer, String, Float

from app.core.db import Base
from app.services.constants import Numerics


class Product(Base):
    '''Модель продукта.'''
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(
        Numerics.PRODUCT_NAME_LENGTH),
        unique=True,
        nullable=False
    )
    quantity = Column(Integer)
    price = Column(Float)
    category = Column(String)
