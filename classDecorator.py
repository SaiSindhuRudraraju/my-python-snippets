def add_str_repr(cls):
    def __str__(self):
        return f"{self.__dict__}"
    
    def __repr__(self):
        return f"{cls.__name__}({self.__dict__})"
    
    cls.__str__ = __str__
    cls.__repr__ = __repr__

    return cls

@add_str_repr
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Laptop", 1200)

print(str(product))
print(product.__str__())
print(repr(product))
print(product.__repr__())
print(product)