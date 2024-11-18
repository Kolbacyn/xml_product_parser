import pytest

PRODUCT_URL = '/product/'


@pytest.mark.parametrize(
    'invalid_name',
    [
        '',
        None,
        'a' * 256
    ],
    ids=[
        'empty_name',
        'None_name',
        'long_name'
    ]
)
def test_create_product_invalid_name(
    test_client,
    invalid_name
):
    response = test_client.post(
        PRODUCT_URL,
        json={
            'name': invalid_name,
            'quantity': 10,
            'price': 100,
            'category': 'Electronics'
        }
    )

    assert response.status_code == 422, (
        'Создание продукта с невалидным именем или именем '
        'больше 255 символов запрещено.'
    )


@pytest.mark.parametrize(
    'invalid_quantity',
    [
        -1,
        0
    ],
    ids=[
        'negative_quantity',
        'zero_quantity'
    ]
)
def test_create_product_invalid_quantity(
    test_client,
    invalid_quantity
):
    response = test_client.post(
        PRODUCT_URL,
        json={
            'name': 'Product',
            'quantity': invalid_quantity,
            'price': 100,
            'category': 'Electronics'
        }
    )

    assert response.status_code == 422, (
        'Создание продукта с невалидным количеством запрещено.'
    )


@pytest.mark.parametrize(
    'invalid_price',
    [
        -1,
    ],
    ids=[
        'negative_price',
    ]
)
def test_create_product_invalid_price(
    test_client,
    invalid_price
):
    response = test_client.post(
        PRODUCT_URL,
        json={
            'name': 'Product',
            'quantity': 10,
            'price': invalid_price,
            'category': 'Electronics'
        }
    )

    assert response.status_code == 422, (
        'Создание продукта с невалидной ценой запрещено.'
    )


@pytest.mark.parametrize(
    'invalid_category',
    [
        '',
        None,
    ],
    ids=[
        'empty_category',
        'None_category',
    ]
)
def test_create_product_invalid_category(
    test_client,
    invalid_category
):
    response = test_client.post(
        PRODUCT_URL,
        json={
            'name': 'Product',
            'quantity': 10,
            'price': 100,
            'category': invalid_category
        }
    )

    assert response.status_code == 422, (
        'Создание продукта с невалидной категорией запрещено.'
    )
