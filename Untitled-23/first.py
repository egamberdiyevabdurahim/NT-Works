from abc import ABC, abstractmethod
from collections import defaultdict


class Product(ABC):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    @abstractmethod
    def print_info(self):
        pass

    def update_quantity(self, quantity):
        raise NotImplementedError("It is a Parent class")
    
    def calculate_cost(self):
        raise NotImplementedError("It is a Parent class")


class Product_kg(Product):
    def __init__(self, name, price, quantity, kg):
        super().__init__(name, price, quantity)
        self.kg = kg
    
    def print_info(self):
        print(f'Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}\nWeight: {self.kg}kg')
    
    def update_quantity(self, quantity):
        if quantity < 0:
            self.quantity -= quantity
            print(f'Quantity minused: {quantity}')
        elif quantity > 0:
            self.quantity += quantity
            print(f'Quantity added: {quantity}')
    
    def calculate_cost(self):
        print(self.price * self.quantity)


class SecondProduct(Product):
    def __init__(self, name, price, quantity, height, width):
        super().__init__(name, price, quantity)
        self.height = height
        self.width = width
    
    def print_info(self):
        print(f'Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}\nHeight: {self.height}cm\nWidth: {self.width}cm')
    
    def update_quantity(self, quantity):
        if quantity < 0:
            self.quantity -= quantity
            print(f'Quantity minused: {quantity}')
        elif quantity > 0:
            self.quantity += quantity
            print(f'Quantity added: {quantity}')
    
    def calculate_cost(self):
        print(self.price * self.quantity)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

class Supplier(Person):
    def __init__(self, name, age, od_of, salary):
        super().__init__(name, age)
        self.od_of = od_of
        self.salary = salary
        self.history = []
    

class Card:
    def __init__(self, card_number: int, name: str, pin: str, date: str):
        self.card_number = card_number
        self.name = name
        self.__pin = pin
        self._date = date
        self.balance = 0
        self.history = defaultdict(list)
    
    @property
    def get_date(self):
        return self._date
    
    def set_date(self, date):
        self._date = date
        print(f"Date Changed To: {self._date}")
    
    @property
    def get_pin(self):
        return self.__pin
    
    def set_pin(self, pin):
        if pin != self.__pin:
            self.__pin = pin
            print(f"Pin Changed To: {self.__pin}")
        else:
            print("Pin Didn't Change!")
    
    def transaction(self, transaction):
        transaction = int(transaction)
        if transaction > 0:
            self.balance += transaction
            self.history['+'].append(transaction)
            print(f"Minused From Card: {transaction}, Balance: {self.balance}")
        elif transaction < 0:
            if self.balance > transaction:
                self.balance -= transaction
                self.history['-'].append(transaction)
                print(f"Added To Card: {transaction}, Balance: {self.balance}")


class Customer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.purchase_history = []
        self.cards = []
    
    def add_card(self, card: Card):
        self.cards.append(card)
        print(f"{card.name}'s {card.card_number} Card Added Successfully!")


class Shop:
    def __init__(self):
        self.products = []
        self.suppliers = []
        self.customers = []
        self.sales = []
        self.inventory = []
        self.money = 0
    
    def add_product(self, product: Product):
        self.products.append(product)
        self.inventory.append(product)
        print(f"{product.name} Added Successfully!")
    
    def add_supplier(self, supplier: Supplier):
        self.suppliers.append(supplier)
        print(f"{supplier.name} Added Successfully!")
    
    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"{customer.name} Added Successfully!")
    
    def sell_product(self, customer: Customer, product: Product, card: Card, quantity: int):
        if product in self.inventory and product.quantity >= quantity:
            if card in customer.cards:
                product.quantity -= quantity
                self.money += product.price * quantity
                self.inventory.remove(product)
                self.sales.append((product, quantity))
                card.transaction(f"-{product.price * quantity}")
                customer.purchase_history.append((product, quantity))
                print(f"{product.name} Sold {quantity} Successfully!")
            else:
                print("Bu Karta Ushbu Haridorniki Emas!")
        else:
            print("Not enough stock or product not found!")
    
    def get_inventory(self):
        for product in self.inventory:
            product.print_info()
            print("---------------------")
        print(f"Total Inventory: {len(self.inventory)}")
    
    def get_sales(self):
        for sale in self.sales:
            print(f"Product: {sale[0].name}, Quantity: {sale[1]}")
        print(f"Total Sales: {len(self.sales)}")
    
    def get_money(self):
        print(f"Money: {self.money}")
    
    def get_customers(self):
        for customer in self.customers:
            print(f"Name: {customer.name}, Age: {customer.age}")
        print(f"Total Customers: {len(self.customers)}")
    
    def get_suppliers(self):
        for supplier in self.suppliers:
            print(f"Name: {supplier.name}, Age: {supplier.age}, OD of: {supplier.od_of}, Salary: {supplier.salary}")
        print(f"Total Suppliers: {len(self.suppliers)}")
    
    def print_info(self):
        print("Shop Info:")
        print(f"Money: {self.money}")
        print(f"Total Inventory: {len(self.inventory)}")
        print(f"Total Sales: {len(self.sales)}")
        print(f"Total Customers: {len(self.customers)}")
        print(f"Total Suppliers: {len(self.suppliers)}")
        print("---------------------")
        self.get_inventory()
        self.get_sales()
        self.get_money()
        self.get_customers()
        self.get_suppliers()


shop = Shop()


product1 = Product_kg("Apple", 10, 100, 0.5)
product2 = Product_kg("Banana", 5, 200, 0.2)
product3 = SecondProduct("Tahta", 4, 50, 5, 20)
product4 = SecondProduct("Material", 6, 150, 3, 15)

shop.add_product(product1)
shop.add_product(product2)

shop.add_product(product3)
shop.add_product(product4)   

product1.update_quantity(-1)
product1.update_quantity(2)

product2.update_quantity(-11)
product2.update_quantity(22)

product3.update_quantity(-13)
product3.update_quantity(24)

product4.update_quantity(-15)
product4.update_quantity(26)

for x in [product1, product2, product3, product4]:
    x.calculate_cost()


supplier1 = Supplier("John Doe", 30, "OD-001", 5000)
supplier2 = Supplier("Jane Smith", 25, "OD-002", 4500)

shop.add_supplier(supplier1)
shop.add_supplier(supplier2)


customer1 = Customer("Alice", 28)
customer2 = Customer("Bob", 32)

shop.add_customer(customer1)
shop.add_customer(customer2)


card1 = Card(1234567890, "Alice", "1234", "01/22")
card2 = Card(9876543210, "Bob", "5678", "02/23")

customer1.add_card(card1)
customer2.add_card(card2)


shop.sell_product(customer1, product1, card1, 5)
shop.sell_product(customer2, product2, card2, 10)
shop.sell_product(customer1, product3, card1, 2)
shop.sell_product(customer2, product4, card2, 3)


for x in [product1, product2, product3, product4, shop]:
    x.print_info()