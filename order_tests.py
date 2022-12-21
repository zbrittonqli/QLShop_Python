import unittest

from typing import List

from product import Product
from order import Order


class OrderTests(unittest.TestCase):
    def test_calculate_total(self):
        _products: List[Product] = [
            Product(1, "Television", 300.01),
            Product(2, "Couch", 400.01),
            Product(3, "Table", 200.01)
        ]

        _order = Order(_products)
        _order.calculate_total()

        self.assertEqual(900.03, _order.total)

    def test_calculate_total_no_products(self):
        _order = Order()
        _order.calculate_total()

        self.assertEqual(0, len(_order.products))
        self.assertEqual(0, _order.total)

    def test_add_product(self):
        _order = Order()
        _order.add_product(Product(1, "Television", 300.01))

        self.assertEqual(1, len(_order.products))
        self.assertEqual("Television", _order.products[0].name)
        self.assertEqual(300.01, _order.products[0].price)

    def test_add_many_products(self):
        _products: List[Product] = [
            Product(1, "Television", 300.01),
            Product(2, "Couch", 400.01),
            Product(3, "Table", 200.01)
        ]

        _order = Order()
        _order.add_many_products(_products)

        self.assertEqual(3, len(_order.products))
        self.assertEqual("Television", _order.products[0].name)
        self.assertEqual(300.01, _order.products[0].price)
        self.assertEqual("Couch", _order.products[1].name)
        self.assertEqual(400.01, _order.products[1].price)
        self.assertEqual("Table", _order.products[2].name)
        self.assertEqual(200.01, _order.products[2].price)
        self.assertEqual(900.03, _order.total)
