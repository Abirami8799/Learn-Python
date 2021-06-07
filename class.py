>>> class Myclass(object):
...  a,b=30,50
... 
>>> p= Myclass()
>>> p
<__main__.Myclass object at 0x7f3c6686a400>
>>> dir(p)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'b']


class Student(object):
    def __init__(self, name, branch, year):
        self.name=name
        self.branch= branch
        self.year= year
        print("a student object is created")
    def print_details(self):
        print("name:",self.name)
        print("branch:",self.branch)
        print("year:",self.year)
