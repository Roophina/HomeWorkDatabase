import sqlite3
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import save_data_to_table
from tests.constant_test_cases import PUBLIC_TEST_CASES


def test_save_data_to_table():
    for test_case in PUBLIC_TEST_CASES:
        test_input = test_case.get("test_input")
        expected = test_case.get("expected")
        save_data_to_table(test_input)
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM shops_goods""")
        actual = cursor.fetchall()
        conn.commit()
        conn.close()
        assert actual == expected
        os.remove("mydatabase.db")