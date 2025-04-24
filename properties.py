'''
    property is collection of get and set methods.
    Properties allows developer to access private data members as if like a public data members.
    all the properties are converted into set_xxx and get_xxx methods by the compiler.
'''

class Product:

    def __init__(self):
        self._id = 0
        self._name = ""
        self._price = 0.0

    def set_Id(self,value):
        self._id = value

    def set_Name(self,value):
        self._name = value
    
    def set_Price(self,value):
        self._price = value

    def get_Id(self):
        return self._id

    def get_Name(self):
        return self._name

    def get_Price(self):
        return self._price

    Id = property(get_Id,set_Id)
    Name = property(get_Name,set_Name)
    Price = property(get_Price,set_Price)
    
product = Product()
'''
product.set_Id(1001)
product.set_Name("dell")
product.set_Price(45000.00)
'''

product.Id = 1001
product.Name = "dell"
product.Price = 45000

'''
print(f"{product.get_Id()} {product.get_Name()} {product.get_Price()}")
'''

print(f"{product.Id} {product.Name} {product.Price}")