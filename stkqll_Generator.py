class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return 'Stack Empty'

    def Iterator(self):
        for i in range(len(self.stack)-1, -1, -1):
            yield self.stack[i]

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return 'Queue empty'

    def Iterator(self):
        for i in range(len(self.queue)):
            yield self.queue[i]

class LinkedList():
    def __init__(self):
        self.data = 0
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

    def Iterator(self):
        guest = self.first
        while guest != None:
            yield guest.data
            guest = guest.next

stack = Stack()
queue = Queue()
lnkdlist = LinkedList()

stack.push(100)
stack.push(200)
stack.push(300)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

lnkdlist.add(1)
lnkdlist.add(2)
lnkdlist.add(3)

print("Stack:")
itr = stack.Iterator()
for item in itr:
    print(item)

print("Queue:")
for item in queue.Iterator():
    print(item)

print("Linked List:")
for item in lnkdlist.Iterator():
    print(item)

print("Linked List:")
for item in lnkdlist.Iterator():
    print(item)

'''
print(stack.pop())

print("Stack:")
itr = stack.Iterator()
for item in itr:
    print(item)

print(stack.pop())
print(stack.pop())
print(stack.pop())
'''