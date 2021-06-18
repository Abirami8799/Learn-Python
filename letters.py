import tamil
from tamil.utf8 import  get_letters, get_letters_length, get_words
file=open("unique_sorted_words_in_all_words_20200604-133955.txt","r")
real_word=file.read()
word=get_words(real_word)

value=int(input("enter the value"))

l=[]
for i in range(1,value+1):
    x=input(f'enter the letter {i} ')
    l.append(x)
q=get_words(l)

def correct():
    for each in word:  
        if all(i in get_letters(each) for i in l):  
            print(get_words(each))

def incorrect():
   for each in word:  
        m=get_letters(each)   
        if l[0]==m[0] and l[2]==m[2]:
            print(get_words(each))


if ( get_letters_length(q[0])==len(l)):
    correct()
else:
    incorrect()










    



