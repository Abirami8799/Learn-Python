>>> s= 'i am indian'
>>> s
'i am indian'
>>> s='here is line splint in two lines'
>>> s
'here is line splint in two lines'
>>> s='here is line  \n splint in two lines'
>>> s
'here is line  \n splint in two lines'
>>> s="here is line  \n splint in two lines"
>>> s
'here is line  \n splint in two lines'
>>> print(s)
here is line  
 splint in two lines
  s= """ This is a
... multiline string, so you can
... write many line"""
>>> print(s)
 This is a
multiline string, so you can
write many line
>>> print(s)
helloworld
>>> len(s)
10
>>> s.title()
'Helloworld'
>>> s.upper()
'HELLOWORLD'
>>> s.lower()
'helloworld'
>>> s.swapcase()
'HELLOWORLD'
>>> s.isalnum()
True
>>> s="jsifjwo 223242"
>>> s.isalnum()
False
>>> s="12345"
>>> s.isdigit()
True
>>> s="12345serte"
>>> s.isdigit()
False
>>> s="Fedora9 is coming"
>>> s.islower()
False
>>> s.istitle()
False
>>> s="Fedora9 Is Coming"
>>> 
>>> s.istitle()
True
>>> s="INDIA"
s.isupper()
True
>>> s="we all love python"
>>> s.split(" ")
['we', 'all', 'love', 'python']
>>> s
'we all love python'
>>> x="nishant:is:waiting"
>>> x.split(":")
['nishant', 'is', 'waiting']
>>> s="abc\n"
>>> s
'abc\n'
>>> s.strip()
'abc'
s="www.foss.in"
>>> s.lstrip("cwsd.")
'foss.in'
>>> s.rstrip("cnwdi.")
'www.foss'
>>> s="faculty for a reason"
>>> s.find("for")
8
>>> s.find("fac")
0
 s.startswith("fu")
False
>>> s.endswith("son")
True
for ch in "python":
...    print(ch)
... 
p
y
t
h
o
n

s= input("please enter a string")
z= s[::-1]
if(s==z):
    print("palindrome")
else:
    print("not a palindrome")

