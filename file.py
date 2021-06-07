>>> fobj=open("love.txt")
>>> fobj
<_io.TextIOWrapper name='love.txt' mode='r' encoding='UTF-8'>
>>> fobj.close()
fobj=open("love.txt",'w')
>>> fobj.write("powerpork\n")
10
>>> fobj.write("hello world\n")
12
>>> fobj.close()

>>> fobj=open("love.txt")
>>> fobj.read()

>>> fobj=open("love.txt")
>>> fobj.readline()
'powerpork\n'
>>> fobj.readline()
'hello world\n'


name=input("enter the file name")
fobj=open(name)
print(fobj.read())
fobj.close()
