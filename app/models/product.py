from sqlalchemy import Column, Integer, String, Float

from app.core.db import Base


class Product(Base):
    """Product model."""
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    quantity = Column(Integer)
    price = Column(Float)
    category = Column(String)
