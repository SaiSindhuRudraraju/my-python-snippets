'''
creating a new class based on existing class by adding new features.
or
extending the class by adding new features without disturbing the existing class and dependent application.

all the methods of the existing class(base or parent) can be accessed from child class(derived class)
'''

class Math2024:
    def Sum(self,x,y):
        return x+y
    def Subt(self,x,y):
        return x-y

class Math2025(Math2024):
    def Mult(self,x,y):
        return x*y

m2024 = Math2024()

print("++", m2024)

print(m2024.Sum(100,200))
print(m2024.Subt(200,100))

m2025 = Math2025()

print(m2025.Sum(100,200))
print(m2025.Subt(200,100))
print(m2025.Mult(20,5))
print("***")
x=100
print(x)