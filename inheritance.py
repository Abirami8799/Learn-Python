class Person(object):
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch

    def print_name(self):
        print(self.name,self.branch)
    
x= Person("Abi","cse")
x.print_name()


class Student(Person):
    pass
   
x=Student("my","be")
x.print_name()



