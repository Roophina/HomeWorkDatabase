# публичные тестовые случаи из текста условия задачи
PUBLIC_TEST_CASES = [
    {"test_input": {'id': 1234, 'name': 'Холодильник', 'package_params': {'width': 30, 'height': 50},
                    'location_and_quantity': [{'location': 'Магазин на Ленина', 'amount': 8},
                                              {'location': 'Магазин в центре', 'amount': 1}]},
     "expected": [(1, 1234, 'Магазин на Ленина', 8), (2, 1234, 'Магазин в центре', 1)]}]
#     {"test_input": [[1, 0], [1, 1]], "expected": 1},
#     {"test_input": [[1, 0], [0, 1]], "expected": 2},
#     {
#         "test_input": [
#             [1, 1, 1, 1, 1],
#             [0, 0, 0, 0, 0],
#             [0, 0, 1, 1, 0],
#             [1, 0, 1, 1, 0],
#         ],
#         "expected": 3,
#     },
#     {"test_input": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "expected": 0},
#     {"test_input": [[1, 1, 1], [1, 1, 1], [1, 1, 1]], "expected": 1},
# ]
#
# # Здесь можно написать свои тестовые случаи
# SECRET_TEST_CASES = []