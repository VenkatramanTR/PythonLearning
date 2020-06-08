import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="Venkat", password="1234", database="sakila")

cursor = mydb.cursor()
cursor.execute("select * from actor")
result = cursor.fetchone()
print(result)
mydb.close