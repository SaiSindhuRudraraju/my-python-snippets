#constructors:

# is also a member function of a class but it is automatically invoked when we create instanse of a class

# constructor in python should be named __init__

# constructor can take parameter but cant return any value

class Student:
    #sno:int
    #sname:str
    #fee:float    no need to declare in class.

    def __init__(self, sno=0, sname='', fee=0):
        #pass

        print("init method invoked")
        self.sno = sno
        self.sname = sname
        self.fee = fee 

    def PrintStudent(self):
        print(f"{self.sno} {self.sname} {self.fee}")      

stud = Student(1001, 'ravi', 4500)
stud = Student()
stud.PrintStudent()
