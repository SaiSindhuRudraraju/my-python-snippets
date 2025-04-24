'''
list = [10,20,30,40,50]

for i in list:
    print(i)
'''

class Bag:

    def __init__(self):
        self.items = []
        self.current = -1

    def add(self, item):
        self.items.append(item)

    def __iter__(self):
        print("iter invoked")
        return self
    
    def __next__(self):
        self.current += 1
        if self.current < len(self.items):
            return self.items[self.current]
        else:
            raise StopIteration

b = Bag()
b.add(1)
b.add(2)
b.add(3)
b.add(4)
b.add(5)
b.add(6)

'''
for item in b:
    print(item)

for item in b:
    print(item)
'''
itr = iter(b)
'''
for item in itr:
    print(item)
'''
#print(next(itr))

print(itr.__next__())