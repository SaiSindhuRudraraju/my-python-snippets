arr = [10,20,30,40,50]

val = int(input("Enter value to search"))
found = False

for i in range(0,len(arr),1):
    if arr[i] == val:
        print("Value Found")
        found = True
        break
if found == False:
    print("Value not found")

'''using while loop'''
print("**********using while**********")

i = 0
while i < len(arr):
    if val == arr[i]:
        print("Value found")
        break
    i += 1
else:
    print("Value not found")