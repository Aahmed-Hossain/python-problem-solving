class Employee:
    company_name = "Ostad High School"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name} \n Salary: {self.salary}")

    @classmethod
    def change_company_name(cls,name):
        cls.company_name = name

object1 = Employee("Rahim Vai", 20000)
object1.display_info()

Employee.change_company_name('ABC High School')
print(object1.company_name)
