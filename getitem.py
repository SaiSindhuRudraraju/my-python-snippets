class List:
    def __init__(self):
        self.items = []

    @property
    def Items(self):
        return self.items

    def add(self,value):
        self.items.append(value)
    
    def __getitem__(self,ndx):
        return self.items[ndx]

list = List()
list.Items.append(100)
list.Items.append(200)
list.Items.append(300)
list.Items.append(400)
list.Items.append(500)

list.add(600)

print(list.Items)
print(list[0])



"""
Question:

class Collection:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

class List:
    def __init__(self):
        self.collection = Collection()

    @property
    def Items(self):
        return self._collection

    
list = List()
list.Items.add(100)
list.Items.add(200)
list.Items.add(300)
list.Items.add(400)

print(list.Items[0])
print(list.Items[1])    
print(list.Items[2])    
print(list.Items[3])    

"""