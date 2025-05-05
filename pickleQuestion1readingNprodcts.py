import pickle

class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def __str__(self):
        return f"{{pid = {self.pid}, name = {self.name}, price = {self.price}}}"

n = int(input("Enter number of products you want to store in file : "))
with open("products.pickle", "wb") as fp:
    i = 1
    while(i<=n):
        pid = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))
        pickle.dump(Product(pid, name, price), fp)
        i = i+1

val = int(input("Enter pid to search: "))

with open("products.pickle", "rb") as fp:
    found = False
    while True:
        try:
            product = pickle.load(fp)
            if product.pid == val:
                print("Product found:", product)
                found = True
                break
        except EOFError:
            break

if not found:
    print("Product not found.")