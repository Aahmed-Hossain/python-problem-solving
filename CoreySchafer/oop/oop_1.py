class Employee:
    raise_amount = 1.04
    emp_nums = 0

    def __init__(self, first_name, second_name, pay):
        self.first_name = first_name
        self.second_name = second_name
        self.pay = pay
        self.email = first_name + '.' + second_name + '@gmail.com'

        Employee.emp_nums +=  1

    def full_name(self):
        return '{} {}'.format(self.first_name, self.second_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_str(cls, emp_str):
        first_name, last_name, pay  =emp_str.split('-')
        return cls(first_name, last_name, pay)

emp1 = Employee('Ahmed', 'Hossain', 27000)
emp2 = Employee('Adnan', 'Alam', 100000)

emp_str1 = 'Ahmed-Hossain-27000'
emp_str2 ='Adnan-Alam-100000'

new_emp1 = Employee.from_str(emp_str1)
print(new_emp1.email)
print(new_emp1.pay)

print(new_emp1.email)
print(new_emp1.pay)



# Employee.raise_amount = 1.05
# Employee.set_raise_amount(1.05)
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
