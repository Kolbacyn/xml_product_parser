import pytest


@pytest.fixture
def product(mixer):
    return mixer.blend(
        'app.models.product.Product',
        name='best product',
        quantity=10,
        price=100,
        category='Test_category'
    )


@pytest.fixture
def product_2(mixer):
    return mixer.blend(
        'app.models.product.Product',
        name='next best product',
        quantity=40,
        price=1000,
        category='Test_category'
    )
