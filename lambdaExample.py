list = [10,20,30,40]
'''
def filter(lst, val):
    temp = []
    for i in lst:
        if i < val:
            temp.append(i)
    return temp

filteredList = filter(list, 30)
print(filteredList)
'''

def filter(lst, func):
    temp = []
    for i in lst:
        if func(i):
            temp.append(i)
    return temp

filteredList = filter(list, lambda x : x>20)
print(filteredList)

filteredList = filter(list, lambda x : x>10)
print(filteredList)

def expr(x):
    return x>20

filteredList = filter(list,expr)
print(filteredList)


'''
Question:

create a class product
create a class productList
add product class objects to productList class
provide a method to filter the product list based on price
provide a method to filter the product list based on name
provide a method to filter the product list based on category
provide a method to filter the product list based on brand
provide a method to filter the product list based on rating
provide a method to filter the product list based on stock
provide a method to filter the product list based on availability
provide a method to filter the product list based on discount