

class Product:
    id: int
    name: str
    price: float
    quantity: int

    def __init__(self, _id: int, name: str, price: float, quantity: int = 1):
        self.id = _id
        self.name = name
        self.price = price
        self.quantity = quantity
