from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.crud.product import (check_product_exists, create_product,
                              delete_product, get_product_by_name,
                              read_all_products)
from app.schemas.product import ProductCreate, ProductDB
from app.services import constants, exceptions
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
    match await get_product_by_name(product.name, session):
        case None:
            return await create_product(product, session)
        case _:
            raise exceptions.UnprocessableEntityException(
                detail='Продукт с таким именем уже существует'
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
    return await read_all_products(session)


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

        match products:
            case None:
                raise exceptions.NoContentException(
                    detail='В базе данных нет продуктов'
                )

        await generate_xml(products)
        with open(constants.XML_FILE, 'r') as file:
            xml_data = file.read()

        match xml_data:
            case None:
                raise exceptions.InternalServerException(
                    detail='Возникла ошибка во время записи отчета'
                )
        return Response(content=xml_data, media_type="application/xml")

    except FileNotFoundError:
        raise exceptions.InternalServerException(
            detail='Произошла ошибка во время генерации отчета'
        )
    except Exception as e:
        raise exceptions.BadRequestException(detail=str(e))


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
