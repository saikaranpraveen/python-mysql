import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "sakila"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM actor")
my_result= mycursor.fetchall()

for x in my_result:
    print(x)