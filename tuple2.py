list = [[10,20,30], [40,50,60]]

for lst in list:
    print(lst)
    for val in lst:
        print(val)

t1 = ((10,20,30), (10,20,30), (40,50,60), [10,20,30], ([60,70,80],))

print(t1)

print(t1[0:2])

print(t1[2:])
print("****")
print(t1[0][0])
print("*****")

for item1 in t1:
    print(item1)
    for val in item1:
        print(val)

print(t1.count((10,20,30)))

print(t1.index((40,50,60)))