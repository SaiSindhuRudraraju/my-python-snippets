#python does not supports traditional method overloading

#we can acieve with default parameters for some extent and add if condition
#we dont have method overloading in python

#access specifiers also not available

class Math:
    def sum(self, x=None, y=None):
        if(x is not None and y is not None):
            return x+y
        else:
            print('no parameters')

math = Math()

print(math.sum())
print("****")
print(math.sum(100,200))

print(math.sum(y=100))