class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __eq__(self, prod):
        return self.name == prod.name and self.price == prod.price

    def __str__(self):
        return f"{self.name}, {self.price}"

    def __repr__(self):
        return f"name: {self.name}, price: {self.price}"
    
class ProductList:
    def __init__(self):
        self.productsList = []
    
    def __iadd__(self, product):
        self.productsList.append(product)
        print("Product added to list")
        return self
        
    def __isub__(self, product):
        if(len(self.productsList) >= 1):
            self.productsList.remove(product)
        print("Product removed from list")
        return self

    def __ge__(self, price):
        temp = ProductList()
        temp.productsList = []
        for p in self.productsList:
            if p.price >= price:
                temp.productsList.append(p)
        return temp

    def __iter__(self):
        return iter(self.productsList)

    def __repr__(self):
        return f"{self.productsList}"

p1 = Product("Laptop", 1000)
p2=Product("Phone", 500)
p3=Product("Tablet", 300)
p4=Product("Camera", 500)
p5 = Product("Laptop", 1000)

plist=ProductList()
plist+=p1
plist+=p2
plist+=p3
plist-=p2
plist+=p4

p6=plist>=500
print("All oproducts whose price is >= 500 are: ")
for p in p6:
    print(p)

print(p6)

print(f"result of p1==p3: {p1 == p3}")
print(f"result of p1 == p5: {p1 == p5}")

print("All products: ")
for prod in plist:
    print(prod)