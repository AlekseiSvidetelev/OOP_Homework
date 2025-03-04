import pytest

from src.main import Product
from src.main import Category

@pytest.fixture
def test_case_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

@pytest.fixture
def test_case_category():
    return Category("Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                    [])

def test_init_product(test_case_product):
    assert test_case_product.name == "Samsung Galaxy S23 Ultra"
    assert test_case_product.description == "256GB, Серый цвет, 200MP камера"
    assert test_case_product.price == 180000.0
    assert test_case_product.quantity == 5
    assert Product.product_count == 1


def test_init_category(test_case_category):
    assert test_case_category.name == "Смартфоны"
    assert test_case_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert test_case_category.products == []
    assert Category.category_count == 1
