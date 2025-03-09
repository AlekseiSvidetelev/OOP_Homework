from src.main import Category, new_product, add_product
from src.main import Product


def test_init_product(test_case_product):
    assert test_case_product.name == "Samsung Galaxy S23 Ultra"
    assert test_case_product.description == "256GB, Серый цвет, 200MP камера"
    assert test_case_product.price == 180000.0
    assert test_case_product.quantity == 5


def test_init_category(test_case_category):
    assert test_case_category.name == "Смартфоны"
    assert (
        test_case_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert test_case_category.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_add_product(test_case_product, test_product4):

    assert test_init_category.add_product(test_product4) == 123

