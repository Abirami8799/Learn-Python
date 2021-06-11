import tamil
from tamil.utf8 import  get_letters_length, get_words

file=open("unique_sorted_words_in_all_words_20200604-133955.txt","r")
read_word=file.read()
word=get_words(read_word)
x=int(input("enter the number of word "))
y=input("enter the starting word ")
z=input("enter the ending word ")
 

for each in word:
    if get_letters_length(each)==x  and each.startswith(y) and each.endswith(z):
        print(each)
