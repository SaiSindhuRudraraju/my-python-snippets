class Product:
    def __init__(self):
        self._id = 0
        self._name = ""
        self._price = 0.0

    @property       #decorator
    def id(self):
        return self._id

    @id.setter
    def id(self,value):
        self._id = value

    @property       #decorator
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    @property       #decorator
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        self._price = value

    @price.deleter
    def price(self):
        print("in deleter")
        del self._price

product = Product()

product.id = 1001
product.name = "dell"
product.price = 45000

print(f"{product.id} {product.name} {product.price}")

del product.price
print(f"{product.id} {product.name} ")       #will get error because there will be no price 

product.price = 5000

print(f"{product.id} {product.name} {product.price}")