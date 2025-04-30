class Employee:
    company_name = "Ostad Company Ltd."

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def get_salary(self, password):
        if password == 'Admin':
            print(self._salary)
        else:
            print('invalid access!!!')

    def set_salary(self, password, salary):
        if password == 'Admin':
            self._salary = salary
            print(f"Updated salary:{self._salary}")
        else:
            print('invalid access!!!')

obj1 = Employee("Rahim", 50000)
obj2 = Employee("Karim", 60000)

obj1.get_salary('admin')
obj1.set_salary('Admin', 90000)

print(obj1._salary)
