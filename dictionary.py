dictionary1 = dict(name="Sindhu", age = 24)
dictionary = dict(one = 1, two = 2, three = 3, four = 4)

print(dictionary["one"])

dictionary2 = {
    "one" : 1, "two" : 2, "three" : 3, "four" : 4
}

print(dictionary2["one"])

for key in iter(dictionary2.keys()):
    print(f"{key} {dictionary2[key]}")

print(dictionary2.values())

for value in iter(dictionary2.values()):
    print(value)

if dictionary2.get("ten") is not None:
    print("one is available")

dictionary3 = {"sno":1001, "marks":[10,20,30,40]}

print(dictionary3["sno"])
print(dictionary3["marks"])

class Student:
    def __init__(self, sno, marks):
        self.sno = sno
        self.marks = marks

    def __str__(self):
        return f"{self.sno} {self.marks}"
    
s1 = Student(1001, [10,20,30,40])
s2 = Student(1002, [1,2,30,40])
s3 = Student(1003, [1000,2000,30,40])
s4 = Student(1004, [100,200,30,40])

dictionary4 = {"1001":[s1,s2,s3], "1002":s4}

print(dictionary4["1001"])
print(dictionary4.values)
