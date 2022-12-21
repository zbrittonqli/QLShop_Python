from typing import List

from product import Product


class Order:
    products: List[Product]
    total: float

    def __init__(self, products=None, total=0):
        if products is None:
            products = []
        self.products = products
        self.total = total

    def add_product(self, product: Product):
        duplicate: bool = False

        for item in self.products:
            if item.id == product.id:
                duplicate = True
                item.quantity += 1

        if not duplicate:
            self.products.append(product)

        self.calculate_total()

    def add_many_products(self, new_products: list):
        for new_product in new_products:
            self.add_product(new_product)

    def cancel(self):
        self.products.clear()
        self.calculate_total()

    def calculate_total(self):
        self.total = 0

        for product in self.products:
            self.total += product.price
