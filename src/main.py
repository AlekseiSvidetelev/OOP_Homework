from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Базовый абстрактный класс для класса Product"""

    name: str
    description: str
    price: float
    quantity: int

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class MixinLog(BaseProduct):
    """Печатает в консоль информацию о том, от какого класса и с какими параметрами был создан объект"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """ """
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"


class Product(MixinLog, BaseProduct):
    """Класс для представления продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация класса"""
        self.__price = price if price else 0
        super().__init__(name, description, price, quantity if quantity else 0)
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

    def __str__(self) -> str:
        """Представление информации в виде строки"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> Any:
        """Сложение продуктов и вывод суммы этих товаров на складе"""
        if type(self) is not type(other):
            raise TypeError
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def new_product(cls, product: dict[str, Any]) -> "Product":
        """Добавление нового продукта в категорию"""
        return cls(
            name=product.get("name", ""),
            description=product.get("description", ""),
            price=product.get("price", ""),
            quantity=product.get("quantity", ""),
        )

    @property
    def price(self) -> Any:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Изменение цены товара"""
        try:
            if new_price <= 0:
                print("Цена не должна быть нулевая или отрицательная")
                raise ValueError("Цена не должна быть нулевая или отрицательная")
            else:
                self.__price = new_price
        except Exception as e:
            print(f"Ошибка {Exception}: {e}")


class Category:
    """Класс для представления категорий"""

    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int

    def __init__(self, name, description, products=None) -> None:
        """Инициализация класса"""

        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count = len(products)

    def __str__(self) -> str:
        """Представление информации в виде строки"""
        sum_quantity = 0
        for product in self.__products:
            sum_quantity += product.quantity
        return f"{self.name}, количество продуктов: {sum_quantity} шт."

    @property
    def products(self) -> Any:
        return self.__products

    def add_product(self, product: Any) -> None:
        """Добавление новой продукта в категорию"""
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавлять только объекты класса Product или его наследников")
        self.products.append(product)
        Category.product_count += 1

    def middle_price(self) -> Any:
        """Подсчет средней стоимости всех товаров в категории"""
        try:
            if not self.category_count or self.product_count == 0:
                raise ValueError("Список продуктов пуст")
            else:
                sum_price = sum(product.price * product.quantity for product in self.products)
                sum_quantity = sum(product.quantity for product in self.products)
                return round(sum_price / sum_quantity, 2)
        except Exception as e:
            print(f"{e}")


class Smartphone(Product, MixinLog):
    """Класс для определения категории товаров "Смартфоны" """

    name: str
    description: str
    price: float
    quantity: int
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product, MixinLog):
    """Класс для определения категории товаров "Трава газонная" """

    name: str
    description: str
    price: float
    quantity: int
    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


if __name__ == "__main__":

    # homework_17_1

    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
