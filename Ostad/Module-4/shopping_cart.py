# Product - name, pric, stock.
# Customer - name.
# CartItems - product, quatity.
# Cart - Customer, CartItems.

# Payment method.

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Product Name: {self.name}, Product Price: ${self.price} and Remaining Quatity: {self.stock}"

class Customer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Customer Name: {self.name}"

class CartItems:
    def __init__(self, product, quatity):
        self.product = product
        self.quatity = quatity

    def get_total_price(self):
        return self.product.price * self.quatity

class Cart:
    def __init__(self, customer):
        self.customer = customer
        self.cart = []
    def add_to_cart(self, product, quatity):
        self.cart.append(CartItems(product, quatity))

    def calculate_total(self):
        total_price = 0
        for item in self.cart:
            total_price += item.get_total_price()
        return total_price

    def display_cart(self):
        print(f"Shopping cart of {self.customer} ")

        for item in self.cart:
            print(f"Product Name: {item.product.name}, Quantity {item.quatity} and Total ${item.get_total_price()}")

        print(f"Total Price: ${self.calculate_total()}")

    def checkout(self, payment_method):
        total = self.calculate_total()
        payment_method.pay(total)

#payment mehtod
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} in cash.")


class CardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paid ${amount} using card ending with {self.card_number[-4:]}.")


laptop = Product('Hp elite book g5', 50000, 5)
phone = Product('iPhone 13 pro max', 80000, 25)

customer = Customer('Adnan Alam')
adnan_cart = Cart(customer)
adnan_cart.add_to_cart(laptop,3)
adnan_cart.add_to_cart(phone,6)
adnan_cart.display_cart()
card = CardPayment("1234567890123456")
adnan_cart.checkout(card)

# print(laptop)
# print(phone)
# print(customer)
# print(adnan_cart.calculate_total())
