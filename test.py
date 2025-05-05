import pickle
import os

class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def __str__(self):
        return f"{{pid = {self.pid}, name = {self.name}, price = {self.price}}}"

# Step 1: Write products to file
n = int(input("Enter number of products: "))
index = {}

with open("products.pickle", "wb") as fp:
    for _ in range(n):
        pid = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))
        p = Product(pid, name, price)
        index[pid] = fp.tell()  # Storing byte offset for each product
        pickle.dump(p, fp)

# Step 2: Use index for direct access
search_pid = int(input("Enter Product ID to search: "))

try:
    with open("products.pickle", "rb") as fp:
        if search_pid in index:
            fp.seek(index[search_pid])  # Move directly to the correct position
            product = pickle.load(fp)  # Load the exact product
            print("Product found:", product)
        else:
            print("Product not found.")

except (EOFError, OSError):
    print("Error accessing product.")
