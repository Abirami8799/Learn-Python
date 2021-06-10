import tamil
import sys

file=open("unique_sorted_words_in_all_words_20200604-133955.txt","r")

y=input("enter the starting letter")
z=input("enter the ending letter")
for word in file:
      word=word.rstrip()
      if word.startswith(y) and word.endswith(z):
          print(word)


x=int(input("enter the length"))
  
for word in file:
      word=word.rstrip()
      if len(word)==x:
         print(word)


