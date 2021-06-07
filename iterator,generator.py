mytuple=("apple","banana","cherry")
myit= iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))



class Mynum:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x

myclass = Mynum()
myiter =iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


def Generatorfun():
    yield 1
    yield 2
    yield 3

for val in Generatorfun():
    print(val)
   
x=Generatorfun()

print(x.next())
print(x.next())
print(x.next())


def add(num):
    def adder(number):
        return num + number
        return adder
        
