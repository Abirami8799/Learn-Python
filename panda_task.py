import pandas as pd

data={'name':['jaya','abi'],
       'age':[24,21]}

df=pd.DataFrame(data)

df["name"]=df["name"].str.lower()

print(df)


import pandas as pd
import tamil
from tamil.utf8 import  get_letters, get_letters_length

all_tamil_words = open('task1.txt',mode='r',encoding='utf-8').read()
word = pd.DataFrame({'words':all_tamil_words.split('\n')})

print(word)



import pandas as pd
import time
import os
start=time.time()

all_tamil_words = open('unique_sorted_words_in_all_words_20200604-133955.txt',mode='r',encoding='utf-8').read()
word = pd.DataFrame({'words':all_tamil_words.split('\n')})
search="அ"

df1=word[word['words'].str.startswith(search)]
print(df1)

end=time.time()
print(f'runt time {end-start}')


import pandas as pd
import tamil
from tamil.utf8 import  get_letters, get_letters_length

all_tamil_words = open('task1.txt',mode='r',encoding='utf-8').read()
word = pd.DataFrame({'words':all_tamil_words.split('\n')})
df1=word[word['words'].str.contains("அசிசு")]
print(df1)



import pandas as pd
import tamil
import os

all_tamil_words = open('task1.txt',mode='r',encoding='utf-8').read()
word = pd.DataFrame({'words':all_tamil_words.split('\n')})
search="சு"

df1=word[word['words'].str.endswith(search)]
print(df1)
