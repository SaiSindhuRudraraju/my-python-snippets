import pickle

class Category:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{{name = {self.name}}}"
    
    def __repr__(self):
        return f"{{name = {self.name}}}"
    
class Product:
    def __init__(self, name, price, category = None):
        self.category = category
        self.name = name
        self.price = price

    def __str__(self):
        return f"{{name = {self.name}, price = {self.price}}}, category = {self.category.name}"
    
    def __repr__(self):
        return f"{{name = {self.name}, price = {self.price}}}"
    
c1 = Category("laptop")
p1 = Product("mac", 125000, c1)
p2 = Product("dell", 15000, c1)
p3 = Product("hp", 20000, c1)

products = [p1, p2, p3]

with open('product.pickle', 'wb') as fp:
    pickle.dump(products, fp)

with open('product.pickle', 'rb') as fp:
    while True:
        try:
            productsobj = pickle.load(fp)
        except EOFError:
            break

for product in productsobj:
    print(product)


'''
with open('product.pickle', 'wb') as fp:
    pickle.dump(p1, fp)
    pickle.dump(p2, fp)
    pickle.dump(p3, fp)

with open('product.pickle', 'rb') as fp:
    p11 = pickle.load(fp)
    p21 = pickle.load(fp)
    p31 = pickle.load(fp)

print(p11)
print(p21)
print(p31)

products = []
with open('product.pickle', 'rb') as fp:
    while True:
        try:
            temp = pickle.load(fp)
            products.append(temp)
        except EOFError:
            break

for product in products:
    print(product)


products_list = []

products_list.append({"name":'dell', "price":15000})
products_list.append({"name":'lenovo', "price":25000})
products_list.append({"name":'hp', "price":56000})

with open('products_list.pickle', 'wb') as fp:
    pickle.dump(products_list, fp)

with open('products_list.pickle', 'rb') as fp:
    products_list_temp = pickle.load(fp)

for product in products_list_temp:
    print(product)

'''