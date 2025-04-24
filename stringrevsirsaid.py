str = "Innovative Software Solutions"

list = []
for i in range(len(str)-1, -1, -1):
    list.append(str[i])

#print(list)
print("".join(list))

#OR
'''
revlist = [ 1 if str[i] == 'S' else 0 for i in range(len(str)-1, -1, -1) ]
print(revlist)
'''

#OR

#print(revlist)

revlist = [ str[i] for i in range(len(str)-1, -1, -1) ]

print("".join(revlist))

revword = ""
for word in str.split():
    revword += "".join([ word[i] for i in range(len(word)-1, -1, -1)])
    revword += " "
print(revword)   

#OR


revword = []
for word in str.split():
    revword.append( "".join(word[i] for i in range(len(word)-1, -1, -1) ))

print(revword)
print(" ".join(revword))


'''**************'''

st1 = "Rajesh"
print(st1[::-1])

arr = ["Rajesh" , "Ram", "Raj"]
print(arr[::-1])

arr = ["rajesh", "ram", "raj"]
for name in arr:
    print(name[::-1])