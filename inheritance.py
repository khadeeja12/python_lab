class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)

# x=Person("khadeeja","Beevi")
# x.printname()

#inheritance
class Student(Person):
    # def __init__(self,fname,lname):        #this will not inherit person init function
    #     self.firstname=fname
    #     self.lastname=lname
     def __init__(self,fname,lname,year):         
        #  Person.__init__(self,fname,lname)  #this inherit the person init function
         super().__init__(fname,lname)   #this inherit all methods and properties
         self.graduationyear=year
     def welcome(self):
         print("welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)
         

x=Student("Muhammed","Faris",2026)
x.printname()
x.welcome()