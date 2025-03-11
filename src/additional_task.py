from typing import Any

from src.main import Category, Product
from src.utils import load_products_json


def get_information_product(list_product: list[dict[str, Any]]) -> list:
    categories = []
    for get_category in list_product:
        products = []
        for product_ in get_category["products"]:
            products.append(
                Product(
                    name=product_["name"],
                    description=product_["description"],
                    price=product_["price"],
                    quantity=product_["quantity"],
                )
            )
        category = Category(name=get_category["name"], description=get_category["description"], products=products)
        categories.append(category)
    return categories


if __name__ == "__main__":
    test_list = load_products_json("products.json")
    print(test_list)
    print(get_information_product(test_list))
