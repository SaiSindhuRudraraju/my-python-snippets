class Product:
    def __init__(self, name, category, brand, price, rating, stock, availability, discount):
        self.name = name
        self.category = category
        self.brand = brand
        self.price = price
        self.rating = rating
        self.stock = stock
        self.availability = availability
        self.discount = discount

    #def __str__(self):
        #return f"Product: \n Name: {self.name}, Category: {self.category}, Brand: {self.brand}, Price: {self.price}, Rating: {self.rating}, Stock: {self.stock}, Available: {self.availability} Discount: {self.discount}\n"

    def __repr__(self):
        return f"Product: \n Name: {self.name}, Category: {self.category}, Brand: {self.brand}, Price: {self.price}, Rating: {self.rating}, Stock: {self.stock}, Available: {self.availability} Discount: {self.discount}\n"



class ProductList:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def filter(self, condition):
        result = []
        for p in self.products:
            if condition(p):
                result.append(p)
        return result

    def filterwithPrice(self, price): 
        return self.filter(lambda p: p.price <= price)

    def filterwithname(self, name): 
        return self.filter(lambda p: p.name == name)

    def filterwithcategory(self, category): 
        return self.filter(lambda p: p.category == category)

    def filterwithbrand(self, brand): 
        return self.filter(lambda p: p.brand == brand)

    def filterwithrating(self, rating): 
        return self.filter(lambda p: p.rating >= rating)

p1 = Product("Laptop", "smart devices", "thinkpad", 8000, 4.5, 10, True, 10)
p2 = Product("Phone", "smart devices", "apple", 3000, 4.4, 20, True, 15)
p3 = Product("TV", "smart devices", "samsung", 4500, 4.3, 30, False, 20)
p4 = Product("Shirt", "clothes", "Puma", 15, 4.2, 40, True, 25)
p5 = Product("Pant", "clothes", "gap", 15, 4.2, 40, True, 25)
p6 = Product("bottle", "plastic", "tupperware", 15, 4.2, 40, True, 25)

plist = ProductList()
plist.add(p1)
plist.add(p2)
plist.add(p3)
plist.add(p4)
plist.add(p5)
plist.add(p6)

print("\nProducts who's price is above 5000 are:")
print(plist.filterwithPrice(5000))
print("\nProducts who's name is  Pant are:")
print(plist.filterwithname("Pant"))
print("\nProducts who's brand is  apple are:")
print(plist.filterwithbrand("apple"))
print("\nProducts who's catogery is clothes are:")
print(plist.filterwithcategory("clothes"))