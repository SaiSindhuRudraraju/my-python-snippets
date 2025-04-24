def outer():
    x = 100
    def inner():
        print(x)

    inner()

outer()

#this is a clousers example

def Calculate(x,y):
    def Sum():
        return x+y

    return Sum

calc = Calculate(10,20)
x = calc()
print(x)

#example 2:

def calcu(x,y,action):
    return action(x,y)

def add(x,y):
    return x+y

def sub(x,y):
    print("Called", x, y)
    return x-y

z = calcu(10,20,add)
print(z)

y = calcu(1000,200,sub)
print(y)
