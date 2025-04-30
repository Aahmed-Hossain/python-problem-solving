class Employee:
    company_name = "Ostad Company"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self): # instance Method
        print(f"EMP Name : {self.name}\nSalary : {self.salary}")

    @classmethod
    def change_company_name(cls, name):
        cls.company_name = name

ob1 = Employee("Rahim", 30000)
ob2 = Employee("Karim", 40000)
# ob1.display_info()
Employee.change_company_name("ABC company ltd.")
print(ob1.company_name)
print(ob2.company_name)
