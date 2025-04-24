class Math:
    def __init__(self, data:int):
        self.data = data
    
    def sum(self, m):
        t = Math(0)
        t.data = self.data + m.data;
        return t
    
    def print(self):
        print(self.data)

    def __str__(self):
        return str(self.data)

m1 = Math(100)
m2 = Math(200)
m3 = m1.sum(m2)
print(m3)
m3.print()