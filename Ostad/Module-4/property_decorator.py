class Employee:
    company_name = "Ostad Company Ltd."

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,new_salary):
        self._salary = new_salary

obj1 = Employee('Ahmed Hossain', 40000)
print(obj1._salary)
obj1._salary = 70000

print(obj1._salary)
