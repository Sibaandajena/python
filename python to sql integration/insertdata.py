import mysql.connector

conn= mysql.connector.connect(host="localhost", user="root", password="761032", database='pythondb')
mycursor = conn.cursor()

sql = 'insert into student (name, branch, id) values(%s, %s, %s)'
# val =('siba', 'cse', 97)

# if user want to create multiple value then you can create list
val=[('siba', 'cse', 97), ('tapan', 'cse', 115), ('srikant', 'cse', '105')]

#mycursor.execute(sql, val)
mycursor.executemany(sql, val)
conn.commit()
print(mycursor.rowcount, 'record inserted')