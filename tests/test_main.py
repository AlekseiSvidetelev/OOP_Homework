import pytest

from src.main import Category


def test_init_product(test_case_product, test_new_product):
    assert test_case_product.name == "Samsung Galaxy S23 Ultra"
    assert test_case_product.description == "256GB, Серый цвет, 200MP камера"
    assert test_case_product.price == 180000.0
    assert test_case_product.quantity == 5
    new_product = test_case_product.new_product(test_new_product)
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5
    new_product.price = 800
    assert new_product.price == 800
    new_product.price = -100
    assert new_product.price == 800
    new_product.price = 0
    assert new_product.price == 800


def test_init_category(test_case_category, test_product4):
    assert test_case_category.name == "Смартфоны"
    assert (
        test_case_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert test_case_category.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0
    test_case_category.add_product(test_product4)
    assert Category.category_count == 1
    assert Category.product_count == 1
    with pytest.raises(
        TypeError, match="В категорию можно добавлять только объекты класса Product или его наследников"
    ):
        test_case_category.add_product("Не продукт")


def test_get_products_str(test_case_category, test_product4):
    assert test_case_category.get_products_str == ""
    test_case_category.add_product(test_product4)
    assert test_case_category.get_products_str == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
