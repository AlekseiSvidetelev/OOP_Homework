import json
import os
from typing import Any

from config import DATA_DIR


def load_products_json(path_file: str) -> Any:
    """Загружает данные из файла data.products.json"""
    try:
        with open(os.path.join(DATA_DIR, path_file), "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Ошибка {Exception}: {e}")
        return []


if __name__ == "__main__":
    print(load_products_json("products.json"))
