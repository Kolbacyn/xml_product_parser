from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.crud.product import (create_product, delete_product,
                              get_product_by_id, get_product_by_name,
                              read_all_products)
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductDB
from app.services.xml import generate_xml

router = APIRouter()


@router.post(
        '/',
        response_model=ProductDB,
        response_model_exclude_none=True
)
async def create_new_product(
    product: ProductCreate,
    session: AsyncSession = Depends(get_session),
):
    '''
    Создает новый продукт.
    '''
    room_id = await get_product_by_name(product.name, session)
    match room_id:
        case None:
            new_product = await create_product(product, session)
            return new_product
        case _:
            raise HTTPException(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                detail='Product already exists'
            )


@router.get(
    '/',
    response_model=list[ProductDB],
    response_model_exclude_none=True
)
async def get_all_products(
    session: AsyncSession = Depends(get_session)
):
    '''
    Возвращает список продуктов.
    '''
    products = await read_all_products(session)
    return products


@router.get(
    '/sales_report/',
    response_model=ProductDB,
    response_model_exclude_none=True
)
async def get_product_report(
    session: AsyncSession = Depends(get_session)
):
    '''
    Генерирует отчет о продуктах.
    '''
    try:
        products = await read_all_products(session)
        if products is None:
            raise HTTPException(
                status_code=HTTPStatus.NO_CONTENT,
                detail='No products found'
            )
        if not products:
            raise HTTPException(
                status_code=HTTPStatus.NO_CONTENT,
                detail='No products found'
            )
        await generate_xml(products)
        with open('report.xml', 'r') as file:
            xml_data = file.read()
        if xml_data is None:
            raise HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail='Failed to generate the report'
            )
        return Response(content=xml_data, media_type="application/xml")
    except FileNotFoundError:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail='Failed to generate the report'
        )
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=str(e)
        )


@router.delete(
    '/{product_id}',
    response_model=ProductDB,
    response_model_exclude_none=True
)
async def remove_product(
    product_id: int,
    session: AsyncSession = Depends(get_session)
):
    '''
    Удаляет продукт.
    '''
    product = await check_product_exists(product_id, session)
    await delete_product(product, session)
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
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail='Product not found'
            )
        case _:
            return product
