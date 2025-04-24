class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(id={self.pid}, name={self.name}, price={self.price})"

class Collection:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        if isinstance(index, int):
            for item in self._items:
                if item.pid == index:
                    return item
            return None
        elif isinstance(index, str):
            result = []
            for item in self._items:
                if item.name == index:
                    result.append(item)
            return result
        elif callable(index):
            result = []
            for item in self._items:
                if index(item):
                    result.append(item)
            return result
        
class List:
    def __init__(self):
        self._collection = Collection()

    @property
    def Items(self):
        return self._collection

listOfProducts=List()
listOfProducts.Items.add(Product(1001,'dell',4500))
listOfProducts.Items.add(Product(1002,'mac',6500))
listOfProducts.Items.add(Product(1003,'hp',9540))
listOfProducts.Items.add(Product(1004,'lenovo',5501))

prod=listOfProducts.Items[1003] 
print(prod)  
prods=listOfProducts.Items[lambda prod:prod.price>5500] 
print(prods)
prod=listOfProducts.Items['dell']
print(prod)
