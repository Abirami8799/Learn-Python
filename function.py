def change(b):
    a=10
    print(a)
a=9
print("before function",a)
print("interchange",end= " ")
change(a)
print("aftercall",a)

def change(b):
    global a
    a=10
    print(a)
a=9
print("before function",a)
print("interchange",end= " ")
change(a)
print("aftercall",a)

def test (a, b=-99):
 if a > b:
  return true
 else:
  return false
  
  
  >>> def f(a,data=[]):
...  data.append(a)
...  return data

>>> print(f(2))
[1, 2]


>>> def func(a,b=5,c=10):
...  print('a is',a,'b is',b,'c is',c)
... 
>>> func(12,24)
a is 12 b is 24 c is 10
>>> func(a=4)
a is 4 b is 5 c is 10
>>> 

>>> lst=[1,2,3,4,5,6]
>>> def square(num):
...  return num*num
... 
>>> print(list(map(square, lst)))
[1, 4, 9, 16, 25, 36]
>>> 



