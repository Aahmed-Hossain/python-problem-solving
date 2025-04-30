
        # self ei class er object ke indicate kore.
        # self is a reference to the current instance of the class. It’s used to access variables and methods that belong to the class. When you define a method inside a class, the first parameter is always self, which allows you to refer to the object’s properties and methods within that method.
        # __init__() is a constructor method that runs when a new instance of Car is created.constructor - who made something. here contructing object.  and it also called Dunder methode  - Double underscore method.
        # 1. Default constructor
        # 2. Parameterized constructor
        # 3. Default value constructor.

 # 1. Default constructor
class Car:
    def __init__(self):
        self.brand = ""
        self.model = ""
car1 = Car()
car1.brand = "Toyota"
car1.model = "Corola"
print(car1)
print(car1.brand, car1.model)
# An instance is a specific object created from a class. A class acts as a blueprint, and an instance is a unique object built using that blueprint, with its own data and behavior.
# car1 is an instance of the Car class, representing a Toyota Corolla.
# car2 is another instance, representing a Honda Civic.


# 2. Parameterized constructor
class Bike:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
bike1 = Bike('Suzuki', 'gixser')
print(bike1.model, bike1.brand)

# 3. Default value constructor.
class Cycle:
    def __init__(self,brand =  'Phonix', model= 'Phonki-raj'):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Cycle Brand: {self.brand}\nCycle Model: {self.model}")
cycle1 = Cycle()
cycle2 = Cycle('Duronto', 'GenZ-7712')
# print(cycle1.brand, cycle1.model)
cycle1.display_info()
cycle2.display_info()
