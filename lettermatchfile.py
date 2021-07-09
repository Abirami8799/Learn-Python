

import os
key = input("enter the length of the string  ")
letter=input("enter the first letter of word")
dict = {'3': 'len_3' , '4': 'len_4', '5':'len_5'}  
if key in dict:
   b=dict[key]
a=b
s=[]
for root, dirs, files in os.walk("/home/abirami/Music/findfolder", topdown=False):
    for name in dirs:
        if name == a:
           a=os.path.join(root,name)
           for root, dirs, files in os.walk(a):
               for val in files:
                   if val.startswith(letter):
                      s.append(os.path.join(root,val))
        

file=open(s[0],"r")
word=file.read()
print(word)
 





                      
        


           
               
           






        


