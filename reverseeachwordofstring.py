st = "innovative software solutions"

x = st.split()

print(x)
print(x[0])

for i in x:
    # print(i)
    for j in range(len(i)-1,-1,-1):
        print(i[j])
    print(" ")


# OR Used another variable for Copying

revOfSt = ""

for i in x:
    # print(i)
    temp = ""
    for j in range(len(i)-1,-1,-1):
        temp += i[j]
    revOfSt += temp
    revOfSt += " "

print(revOfSt)