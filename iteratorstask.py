class Product:
    pid:int
    pname:str
    price:float

    def __init__(self, pid:int, pname:str, price:float):
        self.pid = pid
        self.pname = pname
        self.price = price
    
    def __str__(self):
        return f"Product ID: {self.pid}, Name: {self.pname}, Price: {self.price}"


class Bag:

    current:int

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __iter__(self):
        self.current = -1
        return self
    
    def __next__(self):
        self.current += 1
        if self.current < len(self.items):
            return self.items[self.current]
        else:
            raise StopIteration

b = Bag()

b.add(Product(1,"product1",100))
b.add(Product(2,"product2",200))
b.add(Product(3,"product3",300))
b.add(Product(4,"product4",400))
b.add(Product(5,"product5",500))

for item in b:
    print(item)

for item in b:
    print(item)