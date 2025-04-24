arr = [10,20,30,40,50]

val = int(input("Enter value to search"))
found = False

for i in range(0,len(arr),1):
    if arr[i] == val:
        print(f"Value Found at pos {i}")
        found = True
        break
if found == False:
    print("Value not found")

'''using while loop'''
print("**********using while**********")

i = 0
while i < len(arr):
    if val == arr[i]:
        print(f"Value found at pos {i}")
        break
    i += 1
else:
    print("Value not found")