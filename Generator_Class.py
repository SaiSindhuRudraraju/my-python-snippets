class List():
    def __init__(self):
        self.list = []

    def add(self,value):
        self.list.append(value)

    def Generator(self):
        count = 0
        while count < len(self.list):
            yield self.list[count]
            count = count + 1

    def Reverse_Generator(self):
        count = len(self.list) - 1
        while count >= 0:
            yield self.list[count]
            count = count - 1

lst = List()
lst.add(100)
lst.add(200)
lst.add(300)
lst.add(400)
lst.add(500)

for item in lst.Generator():
    print(item)

print("In reverse order:")
for item in lst.Reverse_Generator():
    print(item)

#Question: implement List class where i should get values in reverse. I need a generator function which should give me the values in reverse.
#i.e write generator function to retrieve values in reverse from list.


#Question : create a class stack, queue, linkedlist
# all these three classes i should be able to access with one object.
# i'll be using like this:
'''
    stack = Stack()
    queue = Queue()
    ll = LinkedList()

    stack.push(100)
    stack.push(200)

    queue.enqueue(100)
    queue.enqueue(200)
    queue.enqueue(300)

    ll.add(100)
    ll.add(200)
    ll.add(300)

    itr = stack.Iterator()
    for item in itr:
        print(item)

    itr = queue.Iterator()
    for item in itr:
        print(item)

        in the same way linked list

    ( class like stack, queue, linked list. Dont use built in classes, you write all these classes as per their meaning and pattren)
'''