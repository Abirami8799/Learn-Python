
import tamil
from tamil.utf8 import  get_letters, get_letters_length, get_words


with open ('unique_sorted_words_in_all_words_20200604-133955.txt') as file:
    words=[line.strip() for line in file]

value=int(input("enter the value "))

l=[]
for i in range(1,value+1):
    x=input(f'enter the letter {i} ')
    l.append(x)

n=get_words(l)
r=get_letters_length(n[0])
s=[]

for each in words:  
    m=get_letters(each)
    if each.startswith(l[0]) and each.endswith(l[value-1]) and get_letters_length(each)==value:   
       y=[m.index(j) for i,j in zip(l,m) if i==j]
       if len(y)==r:
          print(m)

          
   
