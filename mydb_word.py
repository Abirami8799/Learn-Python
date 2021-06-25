import mysql.connector
from pandas.io.pytables import Table
mydb=mysql.connector.connect(host="localhost",user="root",password="abimoorthy",db='tamil_word')


mycursor = mydb.cursor()

mycursor.execute("create table customers (name VARCHAR(255), address VARCHAR(255))")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("ravi", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()


import mysql.connector
from pandas.io.pytables import Table
mydb=mysql.connector.connect(host="localhost",user="root",password="xxxx",db='tamil_word')

mycursor=mydb.cursor()

sql="CREATE TABLE all_word (word)"
mycursor.execute(sql)



import mysql.connector
from pandas.io.pytables import Table
mydb=mysql.connector.connect(host="localhost",user="root",password="xxxx")

mycursor=mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)



