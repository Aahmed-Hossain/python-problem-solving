class Laptop:
    def __init__(self, brand):
        self.brand = brand

class Student:
    def __init__(self, name, laptop_obj):
        self.name = name
        self.laptop_var = laptop_obj
    def show_laptop_info(self):
        print(f"{self.name} has a laptop named - {self.laptop_var.brand}")

laptop1 = Laptop("HP EliteBook")
student1 = Student("Ahmed Hossain", laptop1)
student1.show_laptop_info()

# aggregation
class School:
    def __init__(self, name):
        self.name = name

class StudentName:
    def __init__(self, name, school):
        self.name = name
        self.school = school # This is aggregation

    def show_details(self):
        print(f"{self.name} studies at {self.school.name}")

school1 = School("Greenhill School")
student1 = StudentName("Aisha", school1)
student1.show_details()



#composition
class Engine:
    def __init__(self, power):
        self.power = power

class Car:
    def __init__(self, brand, power):
        self.brand = brand
        self.enginee = Engine(power)
    def show_car_details(self):
        print(f"{self.brand} has an enginee with {self.enginee.power} Horse Power")

car1 = Car("Prado", 100)
car1.show_car_details()
