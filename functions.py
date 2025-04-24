def Sum(x:int, y:int)->int:
    return(x+y)

def PrintInReverse(x:str):
    print(x[::-1])

rval = Sum(100,200)

def VariableLenght(*args):      #any number of parameters we can pass
    for arg in args:
        print(arg)

def NameArguments(**kwargs):            #key value arguments
    for key,value in kwargs.items():
        print(f"{key} {value}")

def Mult(x,y):
    return x*y

print(rval)

PrintInReverse("Sindhu")

print(Mult(10,5))

print(Mult(y=10, x=2))  #named parameters

VariableLenght(10,20,30,40)

NameArguments(x=10,y=20,z=30,k=40)