class Student:
    sno:int
    name:str
    fee:float

stud=Student()

print(type(stud))
print(id(stud))

stud.sno=input("Enter student no")
stud.name=input("Enter student name")
stud.fee=input("Enter fee")

stud2=Student()

print(id(stud2))

stud2.sno=1002
stud2.name="karthik"
stud2.fee=55500

print(f"{stud.sno} {stud.name} {stud.fee}")
print(f"{stud2.sno} {stud2.name} {stud2.fee}")