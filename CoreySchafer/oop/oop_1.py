class Employee:

    def __init__(self, first_name, second_name, pay):
        self.first_name = first_name
        self.second_name = second_name
        self.pay = pay
        self.email = first_name + '.' + second_name + '@gmail.com'

    def full_name(self):
        return self.first_name + self.second_name

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

emp1 = Employee('Ahmed', 'Hossain', 27000)
emp2 = Employee('Adnan', 'Alam', 100000)

print(emp1)
print(emp2)
