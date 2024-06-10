class Sem3:
    def __init__(self,name): # self is like this . ie, it gives the current,first parameter is always self .
        self.name=name            # so if we have first last name , put it as 2nd and 3rd parameter
    # rep1="khadeeja"
    # rep2="merin"     
    #pass
    def duties(self):
        print("attendence")

classrep1=Sem3("Revathy")  # here object is created
placementrep=Sem3("merin")
# print(classrep1.rep1)
classrep1.duties()    # it prints attedence
print(placementrep.name)  # it prints merin