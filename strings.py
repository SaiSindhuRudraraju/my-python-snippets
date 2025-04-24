st = "innovative"
print(type(st))

print(st[0])
print(st[4])

print(st[0:5])

print(st[:5])

print(st[5:])

print(st[0:10:2])

print(st[-1])

print(st[-2])

st2 = "innovative\nsoftware"
print(st2)

st2 = "innovative\tsoftware"
print(st2)

print(st2.upper())

print(st2.find("soft"))

st2 = "innovative software"
x = st2.split()  #default is space
print(type(x)) 
print(x)

print(st2)

st3 = "innovative,software"
print(st2.split(","))

for ch in st3:
    print(ch)

st4 = "    innovative             "
print(st4)

print(st4.strip())          #strip removes only at beggining and at end. Not in the middle

st5 = "innovative,software,solutions"
print(st5.replace(',',''))

st6 = "innovative\"software\""
print(st6)

st7 = r"innovative\nsoftware"  #raw string
print(st7)

st8 = "innovative\\nsoftware"
print(st8)

st9 = "d:\desktop\kk.txt"
print(st9)

st10 = "c,cpp,java,c,cpp"

print(st10.count('c'))

print(st10.count("c",5))

'''formats'''

st11 = "i love {} language"
st12 = "C"

print(st11.format(st12))

print(st11.format("Cpp"))

st11 = "i love {},{},{} language"

print(st11.format("cpp","c","python"))

lst = ["c", "cpp", "java"]
print("".join(lst))
print(" ".join(lst))
print(",".join(lst))

print(len(st10))


#1. reverse of a string
#2. reverse each word in a string
    # input: ravi rakesh suresh
    # output: ivar hsekar hserus
