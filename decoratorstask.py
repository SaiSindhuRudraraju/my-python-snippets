def modify_class_variable(new_val):
    def decorator(cls):
        print(f"Changing raise amount value to {new_val}")
        cls.raise_amount = new_val
        return cls
    return decorator

@modify_class_variable(1.30)
class Employee:
    raise_amount = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee = Employee("Ram", 5000)

print(employee.raise_amount)

e1 = Employee("John", 5000)
e2 = Employee("ravi", 6000)

print(e1.raise_amount)  
print(e2.raise_amount)
print(Employee.raise_amount)