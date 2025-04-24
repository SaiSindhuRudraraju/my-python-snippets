class Student:
    sno:int
    name:str
    fee:float
    
    def ReadStudent(self):
        self.sno=input("Enter sno")
        self.name=input("Enter name")
        self.fee=input("Enter fee")
    
    def PrintStudent(self):
        print(f"{self.sno}{self.name}{self.fee}")

students = []

for i in range(5):
    stud = Student()
    stud.ReadStudent()
    students.append(stud)


for stud in students:
    stud.PrintStudent()
    
#find student by student number

def FindStudent(sno):
    for stud in students:
        if stud.sno == sno:
            return stud
    return None


find = input("Enter sno: ")
found_student = FindStudent(find)

if found_student:
    print("Student found:")
    found_student.PrintStudent()
else:
    print("Student not found")