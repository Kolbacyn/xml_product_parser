from typing import Optional

from pydantic import BaseModel, Field, NonNegativeFloat, PositiveInt


class ProductBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    quantity: PositiveInt
    price: NonNegativeFloat
    category: str = Field(..., min_length=1, max_length=100)


class ProductCreate(ProductBase):
    name: str = Field(..., min_length=1, max_length=100)


class ProductUpdate(ProductBase):
    pass


class ProductDB(ProductCreate):
    id: PositiveInt

    class Config:
        from_attribute = True
