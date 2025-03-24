import pytest

from src.main import Category, Product


def test_init_product(test_case_product, test_new_product):
    """Тест для проверки класса Product"""
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
    """Тест для проверки класса Category"""
    assert test_case_category.name == "Смартфоны"
    assert (
        test_case_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert Category.category_count == 1
    assert Category.product_count == 3
    test_case_category.add_product(test_product4)
    assert Category.category_count == 1
    assert Category.product_count == 4
    with pytest.raises(
        TypeError, match="В категорию можно добавлять только объекты класса Product или его наследников"
    ):
        test_case_category.add_product("Не продукт")


def test_get_products_str(test_case_product, test_product4, test_new_product):
    """Тест добавления продуктов в категорию"""
    assert str(test_case_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert (test_case_product + test_product4) == 1761000.0
    with pytest.raises(TypeError):
        test_case_product + test_new_product


def test_get_category_str(test_case_category):
    """Тест для проверки работы метода __str__"""
    assert str(test_case_category) == "Смартфоны, количество продуктов: 27 шт."


def test_class_smartphone(test_smartphone):
    """Тест для проверки класса Smartphone"""
    assert test_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert test_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert test_smartphone.price == 180000.0
    assert test_smartphone.quantity == 5
    assert test_smartphone.efficiency == 95.5
    assert test_smartphone.model == "S23 Ultra"
    assert test_smartphone.memory == 256
    assert test_smartphone.color == "Серый"


def test_class_lawngrass(test_lawngrass):
    """Тест для проверки класса LawnGrass"""
    assert test_lawngrass.name == "Газонная трава"
    assert test_lawngrass.description == "Элитная трава для газона"
    assert test_lawngrass.price == 500.0
    assert test_lawngrass.quantity == 20
    assert test_lawngrass.country == "Россия"
    assert test_lawngrass.germination_period == "7 дней"
    assert test_lawngrass.color == "Зеленый"


def test_repr_product(test_product4, test_smartphone):
    """Тест для проверки работы __repr__"""
    assert repr(test_product4) == "Product('55\" QLED 4K', 'Фоновая подсветка', 123000.0, 7)"
    assert (
        repr(test_smartphone)
        == "Smartphone('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)"
    )


def test_middle_price(test_case_category):
    """Тест подсчета стоимости средней стоимости всех проваров в категории"""
    assert test_case_category.middle_price() == 111629.63


def test_exception_middle_price(capsys, test_category_empty):
    """Тестирование обработки исключения при добавлении категории с пустыми продуктами"""
    Category.category_count = 0
    test_category_empty.middle_price()
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Список продуктов пуст"


def test_quantity_is_zero():
    """Тестирование добавления продукта с нулевым количеством"""
    with pytest.raises(ValueError):
        Product("Iphone 15", "512GB, Gray space", 210000.0, 0)
