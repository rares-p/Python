import math


def ex1():
    class Shape:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def get_area(self):
            pass

        def get_perimeter(self):
            pass

        def get_center_of_gravity(self):
            pass

    class Circle(Shape):
        def __init__(self, x, y, radius):
            if radius < 0:
                raise Exception("Circle radius must be a positive number")
            super().__init__(x, y)
            self.radius = radius

        def get_area(self):
            return math.pi * self.radius ** 2

        def get_perimeter(self):
            return 2 * math.pi * self.radius

        def get_center_of_gravity(self):
            return self.x, self.y

    class Rectangle(Shape):
        def __init__(self, x, y, x1, y1, x2, y2):
            if x1 == x2 or y1 == y2:
                raise Exception("Invalid vertices for rectangle")
            super().__init__(x, y)
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2

        def area(self):
            return abs(self.x1 - self.x2) * abs(self.y1 - self.y2)

        def perimeter(self):
            return (abs(self.x1 - self.x2) + abs(self.y1 - self.y2)) * 2

        def get_center_of_gravity(self):
            x = (self.x1 + self.x2) / 2
            y = (self.y1 + self.y2) / 2
            return x + self.x, y + self.y

    class Triangle(Shape):
        def __init__(self, x, y, x1, y1, x2, y2, x3, y3):  # "vertices" relative to center
            super().__init__(x, y)
            self.x1 = x1
            self.x2 = x2
            self.x3 = x3
            self.y1 = y1
            self.y2 = y2
            self.y3 = y3
            a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            b = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
            c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

            if a + b <= c or a + c <= b or b + c <= a:
                raise Exception("Invalid triangle vertices provided")

        def get_area(self):
            a = ((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5
            b = ((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2) ** 0.5
            c = ((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) ** 0.5

            return (self.get_perimeter() / 2 *
                    (self.get_perimeter() / 2 - a) *
                    (self.get_perimeter() / 2 - b) *
                    (self.get_perimeter() / 2 - c)) ** 0.5

        def get_perimeter(self):
            a = ((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5
            b = ((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2) ** 0.5
            c = ((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) ** 0.5

            return a + b + c

        def get_center_of_gravity(self):
            x = (self.x1 + self.x2 + self.x3) / 3
            y = (self.y1 + self.y2 + self.y3) / 3

            return x + self.x, y + self.y


def ex2():
    class BaseAccount:
        def __init__(self, account_id, name, balance):
            self.account_id = account_id
            self.name = name
            self.balance = balance

        def deposit(self, amount):
            if amount > 0:
                self.balance += amount
            else:
                raise Exception("Invalid deposit amount")

        def withdraw(self, amount):
            if 0 < amount <= self.balance:
                self.balance -= amount
            else:
                raise Exception("Invalid withdrawal amount or insufficient balance")

        def calculate_interest(self):
            pass

        def __str__(self):
            return f"Account ID: {self.account_id}, Account Holder: {self.name}, Balance: ${self.balance:.2f}"

    class SavingsAccount(BaseAccount):
        def __init__(self, account_id, name, balance, interest_rate):
            super().__init__(account_id, name, balance)
            self.interest_rate = interest_rate

        def calculate_interest(self):
            return self.balance * (self.interest_rate / 100)

    class CheckingAccount(BaseAccount):
        def __init__(self, account_id, name, balance, overdraft_limit):
            super().__init__(account_id, name, balance)
            self.overdraft_limit = overdraft_limit

        def withdraw(self, amount):
            if 0 < amount <= (self.balance + self.overdraft_limit):
                self.balance -= amount
            else:
                raise Exception("Invalid withdrawal amount or overdraft limit exceeded")


def ex3():
    class Vehicle:
        def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year

        def __str__(self):
            print(f"{self.year} {self.make} {self.model}")

    class Car(Vehicle):
        def __init__(self, make, model, year, fuel_efficiency):
            super().__init__(make, model, year)
            self.fuel_efficiency = fuel_efficiency

        def calculate_mileage(self, distance):
            return distance / self.fuel_efficiency

    class Motorcycle(Vehicle):
        def __init__(self, make, model, year, fuel_efficiency):
            super().__init__(make, model, year)
            self.fuel_efficiency = fuel_efficiency

        def calculate_mileage(self, distance):
            return distance / self.fuel_efficiency

    class Truck(Vehicle):
        def __init__(self, make, model, year, towing_capacity):
            super().__init__(make, model, year)
            self.towing_capacity = towing_capacity

        def calculate_towing_capacity(self):
            return self.towing_capacity


def ex4():
    class Employee:
        def __init__(self, name, employee_id, department):
            self.name = name
            self.employee_id = employee_id
            self.department = department
            self.title = None

        def __str__(self):
            return f"Employee ID: {self.employee_id}, Name: {self.name}, Department: {self.department}"

    class Manager(Employee):
        def __init__(self, name, employee_id, department, salary, team_size):
            super().__init__(name, employee_id, department)
            self.salary = salary
            self.team_size = team_size
            self.title = "Manager"

        def calculate_bonus(self):
            return self.salary * 0.1

    class Engineer(Employee):
        def __init__(self, name, employee_id, department, salary, programming_language, role):
            super().__init__(name, employee_id, department)
            self.salary = salary
            self.programming_language = programming_language
            self.title = role

        def __str__(self):
            return f"{super().__str__()} | Coding in {self.programming_language}"

    class Salesperson(Employee):
        def __init__(self, name, employee_id, department, salary, sales_target):
            super().__init__(name, employee_id, department)
            self.salary = salary
            self.sales_target = sales_target
            self.title = "Salesperson"

        def meet_sales_expectations(self, actual_sales):
            return actual_sales >= self.sales_target

    manager = Manager("John Doe", 1001, "Management", 80000, 5)
    engineer = Engineer("Alice Smith", 2001, "Engineering", 70000, "Python", "Software Engineer")
    salesperson = Salesperson("Bob Johnson", 3001, "Sales", 60000, 100000)

    print(manager)
    print(engineer)
    print(salesperson)

    print(f"Manager Bonus: ${manager.calculate_bonus()}")
    print(f"{engineer.name}'s Role: {engineer.title}")
    print(f"{salesperson.name} Met Sales Target: {salesperson.meet_sales_expectations(110000)}")


def ex5():
    import random

    class Animal:
        def __init__(self, name, species, sound):
            self.name = name
            self.species = species
            self.sound = sound

        def make_sound(self):
            print(f"{self.__class__.__name__} {self.name} of species {self.species} says {self.sound}")

        def sleep(self):
            print(f"{self.__class__.__name__} {self.name} goes to sleep")

    class Mammal(Animal):
        def __init__(self, name, species, sound, fur_color):
            super().__init__(name, species, sound)
            self.fur_color = fur_color

        def give_birth(self):
            print(f"Mammal {self.name} gives birth")

        def produce_milk(self):
            print(f"Mammal {self.name} produces milk")

    class Bird(Animal):
        def __init__(self, name, species, sound, feather_color, beak_shape):
            super().__init__(name, species, sound)
            self.feather_color = feather_color
            self.beak_shape = beak_shape

        def lay_eggs(self):
            print(f"Bird {self.name} lays eggs")

        def fly(self):
            print(f"Bird {self.name} flies")

    class Fish(Animal):
        def __init__(self, name, species, sound, color, average_speed):
            super().__init__(name, species, sound)
            self.color = color
            self.average_speed = average_speed

        def lay_eggs(self):
            print(f"Fish {self.name} lays {random.randint(100, 1000)} eggs")

        def swim(self):
            print(f"Fish {self.name} swims at {self.average_speed * random.uniform(0.9, 1.1):.2f} km/h")

    lion = Mammal("Simba", "African Lion", "Roar", "Golden")
    eagle = Bird("Baldy", "Bald Eagle", "Cra Cra", "White and Brown", "Hooked")
    shark = Fish("Jaws", "Great White Shark", "Chomp", "Gray", 50)

    lion.make_sound()
    eagle.sleep()
    eagle.make_sound()

    lion.give_birth()
    eagle.fly()
    shark.lay_eggs()
    shark.swim()


def ex6():
    class LibraryItem:
        def __init__(self, title, item_id):
            self.title = title
            self.item_id = item_id
            self.checked_out = False

        def check_out(self):
            if not self.checked_out:
                self.checked_out = True
                return f"{self.__class__.__name__} '{self.title}' checked out successfully."
            else:
                return f"{self.__class__.__name__} '{self.title}' is already checked out."

        def return_item(self):
            if self.checked_out:
                self.checked_out = False
                return f"{self.__class__.__name__} '{self.title}' returned successfully."
            else:
                return f"{self.__class__.__name__} '{self.title}' is not checked out."

        def __str__(self):
            status = "checked out" if self.checked_out else "available"
            return f"{self.__class__.__name__} Title: '{self.title}', Item ID: {self.item_id}, Status: {status}"

    class Book(LibraryItem):
        def __init__(self, title, item_id, author, page_count, genre):
            super().__init__(title, item_id)
            self.author = author
            self.page_count = page_count
            self.genre = genre

        def __str__(self):
            return f"{super().__str__()}, Author: {self.author}, Page Count: {self.page_count}, Genre: {self.genre}"

    class DVD(LibraryItem):
        def __init__(self, title, item_id, director, run_time, language):
            super().__init__(title, item_id)
            self.director = director
            self.run_time = run_time
            self.language = language

        def __str__(self):
            return f"{super().__str__()}, Director: {self.director}, Run Time: {self.run_time} minutes, Language: {self.language}"

    class Magazine(LibraryItem):
        def __init__(self, title, item_id, issuer, publication_date):
            super().__init__(title, item_id)
            self.issuer = issuer
            self.publication_date = publication_date

        def __str__(self):
            return f"{super().__str__()}, Issuer: {self.issuer}, Publication Date: {self.publication_date}"

    book1 = Book("The Great Gatsby", 1001, "F. Scott Fitzgerald", 180, "Classic Fiction")
    dvd1 = DVD("Inception", 2001, "Christopher Nolan", 148, "English")
    magazine1 = Magazine("National Geographic", 3001, "Ziarul de Buzau","October 2023")

    print(book1)
    print(dvd1)
    print(magazine1)

    print(book1.check_out())
    print(dvd1.check_out())
    print(magazine1.return_item())

    print(book1.check_out())

    print(book1)
    print(dvd1)
    print(magazine1)


if __name__ == '__main__':
    ex6()
