class Student:
    sno:int
    name:str
    fee:float
    
    def ReadStudent(self):
        self.sno=input("Enter sno: ")
        self.name=input("Enter name: ")
        self.fee=input("Enter fee: ")
    
    def PrintStudent(self):
        print(f"{self.sno} {self.name} {self.fee}")

students = []

for i in range(5):
    print(f"Enter details for Student {i+1}")
    stud = Student()
    stud.ReadStudent()
    students.append(stud)

for stud in students:
    stud.PrintStudent()

studtosearch = input("Enter sno of student to search: ")
found = False
for stud in students:
    if stud.sno ==studtosearch:
        print("Student Found:")
        stud. ()
        found = True
        break

if not found:
    print("Student not found.")