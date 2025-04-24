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

stud=Student()

ReadStudent(stud)
PrintStudent(stud)