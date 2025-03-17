from typing import Any


class Product:
    """Класс для представления продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price=None, quantity=None):
        """Инициализация класса"""
        self.name = name
        self.description = description
        self.__price = price if price else 0
        self.quantity = quantity if quantity else 0

    def __str__(self) -> str:
        """Представление информации в виде строки"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> Any:
        """Сложение продуктов и вывод суммы этих товаров на складе"""
        if not isinstance(other, Product):
            raise ValueError("Можно складывать только объекты Products")
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def new_product(cls, product: dict[str, Any]) -> "Product":
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

    def __init__(self, name, description, products=None):
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


if __name__ == "__main__":

    # homework_15_1

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
