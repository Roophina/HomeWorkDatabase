"""Прототип приложения для выполнения задачи сохранения данных в таблицу."""
import json
import os
from jsonschema import validate
import sqlite3


def read_file(path: str) -> dict:
    """Чтение из файла."""
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def validate_json(data_json: dict) -> None:
    """Валидация входных данных."""
    dir_name_schema = os.path.dirname(__file__)
    filename_schema = os.path.join(dir_name_schema, "goods.schema.json")
    schema = read_file(filename_schema)
    validate(instance=data_json, schema=schema)


def insert_into_goods(data_json: dict, cursor: sqlite3.Cursor) -> None:
    """Запись данных в таблицу goods."""
    params_goods = (
        data_json["id"],
        data_json["name"],
        data_json["package_params"]["height"],
        data_json["package_params"]["width"],
    )
    cursor.execute(
        """INSERT INTO goods (id, name, package_height, package_width)
                           VALUES (?, ?, ?, ?)
                                    """,
        params_goods,
    )


def insert_into_shops_goods(data_json: dict, cursor: sqlite3.Cursor) -> None:
    """Запись данных в таблицу shops_goods."""
    for item in data_json["location_and_quantity"]:
        params_shops_goods = (data_json["id"], item["location"], item["amount"])
        cursor.execute(
            """INSERT INTO shops_goods (id_good, location, amount)
                   VALUES (?, ?, ?)
                                """,
            params_shops_goods,
        )


def update_shops_goods(data_json: dict, cursor: sqlite3.Cursor) -> None:
    """Обновление данных в таблице shops_goods."""
    for item in data_json["location_and_quantity"]:
        product_location = (item["location"],)
        cursor.execute("""SELECT location FROM shops_goods WHERE location = ?""", product_location)
        location_shops_goods = cursor.fetchall()
        if location_shops_goods:
            update_params_shops_goods = (item["amount"], item["location"], data_json["id"])
            cursor.execute(
                """UPDATE shops_goods
                           SET amount = ?
                           WHERE location = ? AND
                           id_good = ?""",
                update_params_shops_goods,
            )
        else:
            params_shops_goods = (data_json["id"], item["location"], item["amount"])
            cursor.execute(
                """INSERT INTO shops_goods (id_good, location, amount)
                                   VALUES (?, ?, ?)
                                                """,
                params_shops_goods,
            )


def save_data_to_table(data_json: dict) -> None:
    """Сохранение данных в таблицу."""
    validate_json(data_json)
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS goods
                               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name varchar NOT NULL,
                                package_height float NOT NULL,
                                package_width float NOT NULL)
                            """
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS shops_goods
                                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    id_good int NOT NULL REFERENCES goods (id),
                                    location varchar NOT NULL,
                                    amount int NOT NULL)
                                """
    )
    product_id = (data_json["id"],)
    cursor.execute("""SELECT id FROM goods WHERE id = ?""", product_id)
    id_goods = cursor.fetchall()
    if not id_goods:
        insert_into_goods(data_json, cursor)
        insert_into_shops_goods(data_json, cursor)
    else:
        update_shops_goods(data_json, cursor)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    dir_name = os.path.dirname(__file__)
    filename = os.path.join(dir_name, "product.json")
    product = read_file(filename)
    save_data_to_table(product)
