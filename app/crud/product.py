from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductDB
from app.services import exceptions


async def create_product(
        new_product: ProductCreate,
        session: AsyncSession
) -> Product:
    '''Создает новый продукт.'''
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
    '''Возвращает продукт по его имени.'''
    product = await session.execute(
        select(Product.id).where(Product.name == product_name)
    )
    return product.scalars().first()


async def read_all_products(
        session: AsyncSession
) -> list[Product]:
    '''Возвращает список всех продуктов.'''
    products = await session.execute(select(Product))
    return products.scalars().all()


async def get_product_by_id(
        product_id: int,
        session: AsyncSession,
) -> Optional[Product]:
    '''Возвращает продукт по его id.'''
    product = await session.execute(
        select(Product).where(Product.id == product_id)
    )
    return product.scalars().first()


async def delete_product(
        product: Product,
        session: AsyncSession
) -> ProductDB:
    '''Удаляет продукт.'''
    await session.delete(product)
    await session.commit()
    return product


async def check_product_exists(
        product_name: str,
        session: AsyncSession,
) -> Product:
    '''
    Проверяет существование продукта в базе данных.
    '''
    product = await get_product_by_id(product_name, session)
    match product:
        case None:
            raise exceptions.NotFoundException(detail='Продукт не найден')
        case _:
            return product
    return
