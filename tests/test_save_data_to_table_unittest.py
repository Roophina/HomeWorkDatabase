import unittest
from tests.constant_test_cases import PUBLIC_TEST_CASES
from main import save_data_to_table
import sys
import os
import sqlite3

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class SaveDataToTableTestCase(unittest.TestCase):
    """Такие же тестовые случаи, но реализованные через unittest."""

    def setUp(self):
        """Начальные условия для тестов."""
        self.all_test_cases = PUBLIC_TEST_CASES

    def test_calculate(self):
        """Тесирование функции сохранения данных в таблицу."""
        for test_case in self.all_test_cases:
            test_input = test_case.get("test_input")
            expected = test_case.get("expected")
            save_data_to_table(test_input)
            conn = sqlite3.connect("mydatabase.db")
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM shops_goods""")
            actual = cursor.fetchall()
            conn.commit()
            conn.close()
            self.assertEqual(actual, expected)
            os.remove("mydatabase.db")
