import json

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __str__(self):
        #print("called")
        return f"{{name = {self.name}, price = {self.price}}}"
    
def converter(obj):
    if isinstance(obj, Product):
        return {
            'name' : obj.name,
            'price' : obj.price
        }
    
def toobject(dct):
    return Product(dct['name'], dct['price'])
    #return Product(**dct)

product = Product("Dell", 2500)

#print(product.__dict__)
#json_string = json.dumps(product.__dict__)
json_string = json.dumps(product, default=converter)
#print(json_string)


#json to dictionary
product_obj = json.loads(json_string)
#print(product_obj)
#print(type(product_obj))

dict = {**product_obj}
#print(dict)

#changing dictionary to product object
#print(Product(**product_obj))

#simplifying things
product_obj = json.loads(json_string, object_hook=toobject)
#print(type(product_obj))
#print(product_obj)


fp = open('product.json', 'a')
fp.write(json_string)
fp.write("\n")
fp.close()

fp = open('product.json', 'r')
json_string = fp.readlines()

for line in json_string:
    product_obj = json.loads(line, object_hook=toobject)
    print(product_obj)
fp.close()