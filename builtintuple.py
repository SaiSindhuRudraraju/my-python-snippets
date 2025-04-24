tuple1 = (10,20,30,40,50)
tuple2 = (60,70,80,90,100)
tuple3 = tuple((10,20,30,40,50,[60,70,80,90,100],(110,120,130,140,150)))

print(tuple1[0])
print(tuple1 == tuple2)

print(tuple1[0:3])

print(tuple3[0])

print(tuple3[5])

print(tuple3[5][0])

print(tuple3[6][0])

for item in tuple3:
    if isinstance(item, tuple):
        for sub_item in item:
            print(sub_item)
    elif isinstance(item,list):
        for sub_item in item:
            print(sub_item)
    else:
        print(item)