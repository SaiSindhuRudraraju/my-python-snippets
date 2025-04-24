class Employee:
    raise_amount = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_raise_amount(cls, amount):
        print("Setting raise amount to: ", amount)
        cls.raise_amount = amount

# Using the class method


employee = Employee("John", 5000)
employee2 = Employee("John", 5000)

print(employee.raise_amount)

Employee.set_raise_amount(1.10)
print(Employee.raise_amount)  

employee3 = Employee("John", 5000)

print(employee.raise_amount)
print(employee2.raise_amount)
print(employee3.raise_amount)
