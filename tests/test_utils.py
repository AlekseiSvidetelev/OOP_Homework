from unittest.mock import patch, mock_open

from src.utils import load_products_json


@patch(
    "builtins.open",
    mock_open(
        read_data='[{"name": "Смартфоны", "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"}]'
    ),
)
def test_load_products_json() -> None:
    """Функция для проверки как выполняется преобразования JSON файла в объект Python"""
    path_file = "mocked_file.json"
    result = load_products_json(path_file)
    assert result == [
        {
            "description": "Смартфоны, как средство не только коммуникации, но и "
            "получение дополнительных функций для удобства жизни",
            "name": "Смартфоны",
        }
    ]


def test_exception_load_products_json(test_json_file):
    """Функция для проверки, как выполняется преобразование JSON файла в объект Python"""
    path_file = "mocked_file.txt"
    result = load_products_json(path_file)
    assert result == []
