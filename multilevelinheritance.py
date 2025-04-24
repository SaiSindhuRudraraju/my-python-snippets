class Math2024:
    def __init__(self):
        print("In 2024 init")

    def Sum(self,x,y):
        return x+y

class Math2025(Math2024):
    def __init__(self):
        super().__init__()
        print("In 2025 init")

    def Subt(self,x,y):
        print("In subt 2026")
        return x-y

class Math2026(Math2025):
    def __init__(self):
        print("In 2026 init")
        super().__init__()

    def Mult(self,x,y):
        return x*y

    def Subt(self,x,y):
        print("IN math 2026")
        return super().Subt(x,y)

m2026 = Math2026()

print(m2026.Sum(100,200))
print(m2026.Subt(200,100))
print(m2026.Mult(20,5))
