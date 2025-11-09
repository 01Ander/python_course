# Defining a class

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f'The {self.brand} {self.model} engine has started.')


# Creating objects
car_1 = Car('Toyota', 'Corolla')
car_2 = Car('Tesla', 'Model Y')

# print(car_1.brand)
# car_2.start()


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        print(f'"{self.title}", written by {self.author} ({self.year})')


book1 = Book('Origen', 'Dan Brown', '2021')
book2 = Book('Harry Potter', 'J.K. Rolling', '1997')


book1.get_info()
book2.get_info()


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimetre(self):
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        return f"Rectangle dimension {self.width}x{self.height}"


rectangle = Rectangle(5, 8)
print(rectangle.area())
print(rectangle.perimetre())
print(rectangle)


class BankAccount:
    def __init__(self, balance):
        self._balance = 0
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError('Amount must be positive')
        self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Amount must be positive')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Amount must be positive')
        if amount > self.balance:
            raise ValueError("Amount must be greater than the balance")
        self.balance -= amount


account = BankAccount(1200)
print(account.balance)
account.deposit(200)
print(account.balance)
account.withdraw(1000)
print(account.balance)
