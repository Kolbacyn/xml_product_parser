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


@pytest.mark.usefixtures('product')
def test_get_product(test_client):
    response = test_client.get(PRODUCT_URL)

    assert response.status_code == 200, (
        f'При GET-запросе к эндпоинту `{PRODUCT_URL}` должен возвращаться '
        'статус-код 200.'
    )

    content = response.json()
    assert isinstance(content, list), (
        f'При GET-запросе к эндпоинту `{PRODUCT_URL}` должен возвращаться '
        'объект типа `list`.'
    )

    assert len(content) > 0, (
        f'При GET-запросе к эндпоинту `{PRODUCT_URL}` должен возвращаться '
        'список продуктов.'
    )
    first_product = content[0]
    expected_keys = ['id', 'name', 'quantity', 'price', 'category']
    missing_keys = expected_keys - first_product.keys()
    assert not missing_keys, (
        f'В ответе на GET-запрос к эндпоинту `{PRODUCT_URL}` не хватает '
        f'следующих ключей: `{"`, `".join(missing_keys)}`'
    )


@pytest.mark.usefixtures('product', 'product_2')
def test_get_all_products(test_client):
    response = test_client.get(PRODUCT_URL)

    assert response.status_code == 200, (
        f'При GET-запросе к эндпоинту `{PRODUCT_URL}` должен возвращаться '
        'статус-код 200.'
    )

    content = response.json()
    assert isinstance(content, list), (
        f'При GET-запросе к эндпоинту `{PRODUCT_URL}` должен возвращаться '
        'объект типа `list`.'
    )

    assert len(content) == 2, (
        'При GET-запросе к эндпоинту `/product/` должен возвращаться '
        'список продуктов. Должно быть два продукта.'
    )
    first_product = content[0]
    expected_keys = ['id', 'name', 'quantity', 'price', 'category']
    missing_keys = expected_keys - first_product.keys()
    assert not missing_keys, (
        f'В ответе на GET-запрос к эндпоинту `{PRODUCT_URL}` не хватает '
        f'следующих ключей: `{"`, `".join(missing_keys)}`'
    )
    [project.pop('close_date', None) for project in content]
    assert content == [
        {
            'name': 'best product',
            'id': 1,
            'quantity': 10,
            'price': 100.0,
            'category': 'Test_category',
        },
        {
            'name': 'next best product',
            'id': 2,
            'quantity': 40,
            'price': 1000.0,
            'category': 'Test_category',
        },
    ], (
        f'При GET-запросе к эндпоинту `{PRODUCT_URL}` тело ответа API '
        'отличается от ожидаемого.'
    )


def test_create_product(test_client):
    response = test_client.post(
        PRODUCT_URL,
        json={
            'name': 'Product',
            'quantity': 10,
            'price': 100,
            'category': 'Electronics'
        }
    )

    assert response.status_code == 200, (
        f'При POST-запросе к эндпоинту `{PRODUCT_URL}` должен возвращаться '
        'статус-код 200.'
    )


def test_delete_product(test_client, product):
    response = test_client.delete(PRODUCT_URL + f'{product.id}/')

    assert response.status_code == 200, (
        f'При DELETE-запросе к эндпоинту `{PRODUCT_URL}` должен возвращаться '
        'статус-код 200.'
    )
