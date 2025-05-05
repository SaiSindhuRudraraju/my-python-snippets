'''
# Question 2: without reading all the products in the file, you need to directly go to that particular product object based on pid.
note: pid's are in sequence.

i think based on memory or the 
'''

import os
import pickle
import sys

class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def __str__(self):
        return f"{{pid = {self.pid}, name = {self.name}, price = {self.price}}}"

sizeofeachProducts = 0
n = int(input("Enter number of products you want to store in file : "))
'''
for i in range(n):
    fp = open("products.pickle", "wb")
    pid = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    pickle.dump(Product(pid, name, price), fp)
    fp.close
    sizeofFile = os.path.getsize('products.pickle')
    sizeofeachProducts = sys.getsizeof(Product(pid, name, price))
    print(sizeofFile)
    print(sizeofeachProducts)

print(sizeofFile)
'''
fp = open("products.pickle", "rb")
sizeofFile = os.path.getsize('products.pickle')
print(sizeofFile)
fp.seek(48)
print(pickle.load(fp))
'''''
with open("products.pickle", "wb") as fp:
    i = 1
    while(i<=n):
        pid = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))
        pickle.dump(Product(pid, name, price), fp)

        #print("Object size:", sys.getsizeof(Product(pid, name, price)), "bytes")
        sizeofeachProducts = sys.getsizeof(Product(pid, name, price))
        sizeofFile = os.path.getsize('products.pickle')

        print(sizeofFile)
        print(sizeofeachProducts)

        i = i+1

val = int(input("Enter pid to search: "))

sizeofFile = os.path.getsize('products.pickle')

print(sizeofFile)
print(sizeofeachProducts)

if(sizeofFile >= val * sizeofeachProducts):
    try:
        with open("products.pickle", "rb") as fp:
            fp.seek(val * sizeofeachProducts)
            product = pickle.load(fp)
            print("Product found: ", product)

    except (EOFError, OSError):
        print("Product not found.")

'''