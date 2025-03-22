from functools import total_ordering


class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, amount: int):
        if amount > 0:
            self.stock += amount
            print(f"Stock updated.")
        else:
            print(f"Error. Incorrect amount.")

    def __str__(self):
        return f"Name: \t{self.name}.\nPrice: \t{self.price}.\nStock: \t{self.stock}."


class User:
    def __init__(self, username: str):
        self.username = username
        self.cart = Cart()

    def __str__(self):
        return f"Username: \t{self.username}."


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product: Product, quantity: int):
        if product.stock >= quantity:
            product.stock -= quantity
            self.items.append((product, quantity))
            print(f"{quantity} {product.name} added to cart.")
        else:
            print("incorrect quantity.")

    def remove_product(self, product: Product):
        for item in self.items:
            if item[0] == product:
                product.stock += item[1]
                print(f"{item[1]} {item[0].name} returned to stock.")
                self.items.remove(item)
                return

    def get_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

    def checkout(self):
        if self.items:
            order = Order(self.items)
            self.items = []
            return order
        else:
            print("Cart is empty")


class Order:
    def __init__(self, products):
        self.products = products
        self.total = 0
        for product, quantity in self.products:
            self.total += product.price * quantity

    def __str__(self):
        iteme = []
        for product, quantity in self.products:
            iteme.append((f"{product.name} - {quantity} szt."))
        return f"Order: {", ".join(iteme)}"


komurka = Product("Phone", 1000, 10)
laptop = Product("Dell", 2000, 5)

anton = User("Anton")

anton.cart.add_product(komurka, 2)
anton.cart.add_product(laptop, 1)

print(f"Общая сумма: {anton.cart.get_total()}$")

order = anton.cart.checkout()
if order:
    print(order)
