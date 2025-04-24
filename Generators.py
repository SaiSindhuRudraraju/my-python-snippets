def Generator():
    yield 1
    yield 2
    yield 3

def MyRange(start, end):
    count = start
    while(count<end):
        yield count
        count = count+1

gen = Generator()

print(gen)

print(next(gen))
print(next(gen))
print(gen.__next__())

gen = Generator()
for item in gen:
    print(item)

for item in MyRange(0,15):
    print(item)