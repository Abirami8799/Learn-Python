import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='xxxx',
                             db='tamil_word',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        file=open("task2","r")
        val=file.readlines()
        for item in val:
             data=item.split(",")
             sql = "INSERT INTO `all_words` (`words`) VALUES (%s)"
             cursor.execute(sql,data)
    connection.commit()

finally:
    connection.close()



