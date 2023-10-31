import unittest

from sales import calculate_total_sales  # Pastikan kode fungsi ada dalam file 'sales.py'

class TestSalesCalculator(unittest.TestCase):

    def test_empty_items_list(self):
        items = []
        result = calculate_total_sales(items)
        self.assertEqual(result, 0)

    def test_single_item(self):
        items = [{"price": 10, "quantity": 5}]
        result = calculate_total_sales(items)
        self.assertEqual(result, 50)

    def test_multiple_items(self):
        items = [{"price": 10, "quantity": 5}, {"price": 20, "quantity": 3}]
        result = calculate_total_sales(items)
        self.assertEqual(result, 110)

    def test_items_with_missing_fields(self):
        items = [{"price": 10}, {"quantity": 3}]
        result = calculate_total_sales(items)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
