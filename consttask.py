'''

class List:

    def __init__(self, vals=None):
        if vals is None:
            self.items = []
        else:
            self.items = vals

    def add(self, val):
        self.items.append(val)

    def find(self, val):
        ''''''
        for item,index in enumerate(self.items):
            if item == val:
                return index
        return -1
        ''''''
        for i in range(len(self.items)):
            if val==self.items[i]:
                return i
        return -1

    def print(self):
        print(", ".join([str(item) for item in self.items]))


listObj = List([10,20,30,40]) 
#listObj = List()
listObj.add(10)
listObj.add(20)
listObj.add(30)

toSearch = int(input("enter value to search: "))
pos = listObj.find(toSearch)
if(pos == -1):
    print(f"{toSearch} is not there in list")
else:
    print(f"Position of {toSearch} = {pos}")

print("All objects in the list are: ")
listObj.print()


'''

class ListClass:

    # items = []
    def __init__(self, *args):
        #print(type(args))
        #print(args)
        if args is None:
            self.items = []
        else:
            self.items = list(args)

    def add(self, val):
        self.items.append(val)

    def find(self, val):
        for index,item in enumerate(self.items):
            # print(type(item),item, type(val), val)
            if item == val:
                return index
        return -1

    def print(self):
        allItems = []
        for item in self.items:
            allItems.append(str(item))
        print(", ".join(allItems))

listObj = ListClass(10,20,30,40) 
#listObj = ListClass()
listObj.add(10)
listObj.add(20)
listObj.add(30)

toSearch = int(input("enter value to search: "))
pos = listObj.find(toSearch)
if(pos == -1):
    print(f"{toSearch} is not there in list")
else:
    print(f"Position of {toSearch} = {pos}")

print("All objects in the list are: ")
listObj.print()

