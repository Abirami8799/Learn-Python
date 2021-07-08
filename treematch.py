import os
path='/home/abirami/Music/findfolder/len_3'
files=[]
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path,i)) and 'b'in i:
       print(i)

import os
for root, dirs, files in os.walk("/home/abirami/Music/findfolder", topdown=False):
   for name in files:
       if os.path.join(root,name):
          print(name) 
import os
for root, dirs, files in os.walk("/home/abirami/Music/findfolder", topdown=False):
   for name in dirs:
      print(os.path.join(root,name))

import os
for root, dirs, files in os.walk("/home/abirami/Music/findfolder", topdown=False):
   for name in dirs:
       print(name)
   for val in files:
       print(val)


import os
a='len_3'
for root, dirs, files in os.walk("/home/abirami/Music/findfolder", topdown=False):
    for name in dirs:
        if name==a:
           a=os.path.join(root,name)
           for root, dirs, files in os.walk(a):
               for val in files:
                   print(val) 
        if name==b:
           a=os.path.join(root,name)
           for root, dirs, files in os.walk(a):
               for val in files:
                   print(val)



