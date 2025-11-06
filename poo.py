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
