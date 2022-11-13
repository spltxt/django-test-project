import pytest

from .models import Product, ProductCategory


@pytest.fixture
def product(db) -> Product:
    return Product.objects.create(
        name='Пепперони',
        price=500,
        category=ProductCategory.PIZZA
    )


def test_product(product):
    assert Product.objects.filter(name='Пепперони').exists()


def test_update_product_name(product):
    product.name = 'Гавайская'
    product.save()
    product_from_db = Product.objects.get(name='Гавайская')
    assert product_from_db.name == 'Гавайская'


def test_update_product_category(product):
    product.category = ProductCategory.DRINKS_AND_SNACKS
    product.save()
    product_from_db = Product.objects.get(name='Пепперони')
    assert product_from_db.category == ProductCategory.DRINKS_AND_SNACKS
