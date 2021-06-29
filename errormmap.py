import mmap
import re
import tamil
from tamil.utf8 import  get_letters, get_letters_length, get_words
import time
start=time.time()
status = False

names_file = open("unique_sorted_words_in_all_words_20200604-133955.txt", "a")
value=int(input("enter the value "))

l=[]
for i in range(1,value+1):
    x=input(f'enter the letter {i} ')
    l.append(x)

n=get_words(l)
r=get_letters_length(n[0])
s=[]

with open("unique_sorted_words_in_all_words_20200604-133955.txt", "rb", 0) as file, \
    mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
    paste = [str(d, 'UTF-8') for d in l] #or paste = bytes(l, 'utf-8')
    words=[line.strip() for line in file]
for each in words:
    m=get_letters(each)
    if each.startswith(l[0]) and each.endswith(l[value-1]) and get_letters_length(each)==value:   
       y=[m.index(j) for i,j in zip(l,m) if i==j]
       if len(y)==r:
          print(m)
        

end=time.time()
print(f'runt time {end-start}')


error:

Traceback (most recent call last):
  File "todaysamp.py", line 23, in <module>
    paste = [str(d, 'UTF-8') for d in l] 
  File "todaysamp.py", line 23, in <listcomp>
    paste = [str(d, 'UTF-8') for d in l] 

Traceback (most recent call last):
  File "todaysamp.py", line 23, in <module>
    paste = bytes(l, 'utf-8')
TypeError: encoding without a string argument
TypeError: decoding str is not supported

