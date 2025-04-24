add = lambda x,y : x+y
print(add(100,200))

subt = lambda x,y : x-y
print(subt(100,200))

def Calculate(x,y,operation):
    return operation(x,y)

z = Calculate(100,200, lambda x,y : x+y)
print(z)

def calc(operation):
    if(operation == '+'):
        return lambda x,y:x+y
    if(operation == '-'):
        return lambda x,y:x-y
    if(operation == '*'):
        return lambda x,y:x*y

x = calc('+')
print(x(100,200))

print(calc('-')(300,100))

def fullname(firstname):
    return lambda lastname: firstname + ' ' + lastname

print(fullname("Sindhu")("Rudraraju"))