from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductDB


async def create_product(
        new_product: ProductCreate,
        session: AsyncSession
) -> Product:
    new_product_data = new_product.model_dump()
    product = Product(**new_product_data)
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product


async def get_product_by_name(
        product_name: str,
        session: AsyncSession,
) -> Product:
    product = await session.execute(
        select(Product.id).where(Product.name == product_name)
    )
    product_id = product.scalars().first()
    return product_id


async def read_all_products(
        session: AsyncSession
) -> list[Product]:
    products = await session.execute(select(Product))
    return products.scalars().all()


async def get_product_by_id(
        product_id: int,
        session: AsyncSession,
) -> Optional[Product]:
    product = await session.execute(
        select(Product).where(Product.id == product_id)
    )
    return product.scalars().first()


async def delete_product(
        product: Product,
        session: AsyncSession
) -> ProductDB:
    await session.delete(product)
    await session.commit()
    return product
