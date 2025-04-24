class MyTuple:
    def __init__(self, *args):
        self.Items = list(args)

    def __getitem__(self, index):
        return self.Items[index]
    
    def __eq__(self,value):
        if isinstance(value, MyTuple):
            for i in range(len(self.Items)):
                if self.Items[i] != value[i]:
                    return False
        else:
            return False
        return True
    
tuple1 = MyTuple(1,2,3)
tuple2 = MyTuple(10,20,30)
tuple3 = MyTuple(1,2,3)

print(tuple1[0])
print(tuple1[1])

if tuple1 == tuple2:
    print("The tuples 1,2 are equal")
else:
    print("The tuples 1,2 are not equal")

if tuple1 == tuple3:
    print("The tuples 1,3 are equal")
else:
    print("The tuples 1,3 are not equal")

if tuple1 == [1,2,3]:
    print("The tuples 1,3 are equal")
else:
    print("The tuples 1,3 are not equal")