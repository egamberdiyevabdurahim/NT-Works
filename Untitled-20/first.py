class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def get_price(self):
        raise NotImplementedError("BU Parent Claass Niki Bunda Ishlamaydi.")

    def get_info(self):
        raise NotImplementedError("BU Parent Claass Niki Bunda Ishlamaydi.")


class Book(Product):
    def __init__(self, price: int, name: str, author: str):
        super().__init__(name, price)
        self.author = author

    def get_price(self):
        return self.price

    def get_info(self):
        return f"Book: {self.name} by {self.author}"


class Electronics(Product):
    def __init__(self, price: int, name: str, model: str):
        super().__init__(name, price)
        self.model = model

    def get_price(self):
        return self.price

    def get_info(self):
        return f"Electronics: {self.name} {self.model}"


products = [Book(10, "Dictionary", "Kimdur"),
            Electronics(300, "Apple", "iPhone")]
