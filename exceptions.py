>>> print(abi)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'abi' is not defined
>>> print(1+'abi')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> def get_number():
...  number=float(input("enter a float number"))
...  return number
... 
>>> while true:
...  try:
...   print(get_number())
...  except valueerror:
...   print("you enter value is wrong")
... 

>>> try:
...  input()
... except:
...  print("unknow exception")

try: 
    fobj=open("/home/abirami/Desktop/love.txt",'w')
    res =12/0
except ZeroDivisionError:
    print("we have an error")
finally:
    fobj.close()
    print("close the file")
    
