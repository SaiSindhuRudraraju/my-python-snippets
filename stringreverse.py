st = "innovative software solutions"

for i in range(len(st)-1, -1, -1):
    print(st[i])

# OR
'''Copying in another variable'''

st2 = ""
for i in range(len(st)-1, -1, -1):
    st2 += st[i]

print(st2)