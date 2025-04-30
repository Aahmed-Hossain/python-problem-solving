class Car:
    def __init__(self):
        self.brand = ''
        self.model = ''

car1 = Car()

car1.brand = 'Honda'
car1.model = 'CRCP 787'
print(car1.brand)
print(car1.model)


class Bike:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

bike1 = Bike("Honda", "civic")
print(bike1.brand, bike1.model)
