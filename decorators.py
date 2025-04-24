def Mydecorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@Mydecorator
def sum(x,y):
    return x+y

print(sum(1,2))

'''
def sum(x,y):
    return x+y

wrapper = decorator(sum)

print(wrapper.__name__)

print(wrapper(1,2))
'''

def Repeat(num_time):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_time):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@Repeat(num_time=3)
@Mydecorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")