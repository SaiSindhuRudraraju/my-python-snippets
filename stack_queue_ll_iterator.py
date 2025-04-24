class Stack():
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, val):
        self.stack.append(val)
        self.top += 1

    def __iter__(self):
        self.current = self.top
        return self

    def __next__(self):
        if (self.current >= 0):
            val = self.stack[self.current]
            self.current -= 1
            return val
        else:
            raise StopIteration

class Queue():
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0

    def enqueue(self, val):
        self.queue.append(val)
        self.front += 1

    def __iter__(self):
        self.current = self.rear
        return self

    def __next__(self):
        if (self.current < self.front):
            val = self.queue[self.current]
            self.current += 1
            return val
        else:
            raise StopIteration
        
class LinkedList():
    def __init__(self):
        self.data = 0
        self.temp = 0
        self.next = None
        self.new = None
        self.prev = None
        self.first = None

    def add(self, val):
        self.new = LinkedList()
        self.new.data = val
        self.new.next = None
        if (self.first == None):
            self.first = self.new
        else:
            self.prev.next = self.new
        self.prev = self.new

    def __iter__(self):
        self.guest = self.first
        return self

    def __next__(self):
        if (self.guest != None):
            self.temp = self.guest.data
            self.guest = self.guest.next
            return self.temp
        else:
            raise StopIteration
        
class Tuple():
    def __init__(self, tpl):
        self.tuple = tpl
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.tuple):
            val = self.tuple[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration

stack = Stack()
queue = Queue()
llist = LinkedList()
tuple = Tuple((10,20,30,40))

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

llist.add(100)
llist.add(200)
llist.add(300)
llist.add(400)

print("Stack:")
for val in stack:
    print(val)

print("Queue:")
for val in queue:
    print(val)

print("LinkedList First Iteration:")
for val in llist:
    print(val)

print("LinkedList Second Iteration:")
for val in llist:
    print(val)

print("Tuple:")
for val in tuple:
    print(val)