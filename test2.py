'''arrays'''

arr = [1,2,3,4,5]
print(type(arr))

print(arr[0])
print(arr[1])

arr.append(50)

arr.remove(3)

arr.insert(2,25)

print(arr)

print("*************")

for i in arr:
    print(i)

for i in range(len(arr)-1,-1,-1):
    print(arr[i])

'''searching a value in a list'''
'''searching a value in a list and print position''' '''for and while'''

'''enumerate'''

for index,value in enumerate(arr,3):
    print(f"{index} : {value}")