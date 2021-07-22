import os
import tamil
from tamil.utf8 import get_letters, get_letters_length, get_words
file=open("unique_sorted_words_in_all_words_20200604-133955.txt.txt")
lines=file.read()
word=get_words(lines)
s=[]
y=[]
q=['ஃ','அ','ஆ','இ','ஈ','உ','ஊ','எ','ஏ','ஐ','ஒ','ஓ','ஔ','௧','௨','௩','௪','௫','௬','௭','௮','௯','௰','௱','௲','ஶ','௦','க', 'ச','ஞ','ட','ண','த','ந','ப','ம','ய','ர','ல','வ','ழ','ள','ற','ன','ஹ','ஜ','ஷ','ஸ']
for each in word:
    if get_letters_length(each)==3:
       s.append(each[0])
a=set(s)

for each in word:
    for x in a:
        if x in q and get_letters_length(each)==3:
           if each.startswith(x) :
              y.append(each)


for x in a:
    if x in q:
       file1=open(os.path.join('/home/abirami/Music/demo/len_3',str(x)+'.txt'),"w")
       for words in y:
           if words.startswith(x):
              file1.writelines("%s\n"%words)
