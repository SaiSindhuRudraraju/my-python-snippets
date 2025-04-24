class Parent_one:
    def print(self):
        print("hello from parent one")

class Parent_two:
    def print(self):
        print("hello from parent two")

'''
class Child(Parent_one,Parent_two):
    pass
'''
'''
class Child(Parent_two,Parent_one):
    pass
'''

class Child(Parent_one,Parent_two):
    def print(self):
        print("hello from child")

child = Child()
child.print()