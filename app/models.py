from pydantic import BaseModel


class Product(BaseModel):
    """Product model."""
    name: str
    quantity: int
    price: float
    category: str
