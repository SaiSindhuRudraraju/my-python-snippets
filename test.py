print("Hello World")
x = int(input("Enter a number"))
y = int(input("Enter another number:"))
z = int(input("Enter another number:"))

print(type(x))
print(x+y)
print("%d + %d = %d" % (x, y, x+y))
print(f"{x} + {y} = {x+y}")

if x>y:
    print("x is greater than y")
else:
    print("y is greater than x")

    
if x>y:
    print("x is greater than y")
elif x==y:
    print("Both are equal")
else:
    print("y is greater than x")


if x>y and x>z:
    print("x is greater than y and z")
elif y>z:
    print("Y is greater than x and z")
else:
    print("z is greater than x and y")

'''ternary operator'''
message = "x is greater than y" if x>y else "y is greater than x"
print(message)

'''nested if'''

if x>35 and y>35 and z>35:
    if (x+y+z)/3 > 60:
        print("A grade")
    elif (x+y+z)/3 > 50:
        print("B grade")
    else:
        print("C grade")
else:
    print("Fail")

'''for loop'''

for i in range(1,5,1):
    print(i)

for i in range(5):
    print(i)

x = [1,2,3,4,5,6]
print("********")
for i in range(5,1,-1):
    print(i)

'''while loop'''

i=0
while i<10:
    if i==5:
        break
    print(i)
    i+=1

print("************")

j=0
while j<5:
    print(j)
    j += 1
    if j==3:
        break
else:
    print("Loop completed")