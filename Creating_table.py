import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "pythonprogramming"
)

print(mydb)

mycursor =mydb.cursor("SHOW DATABASES")

for x in mycursor:
    print(x)

mycursor.execute("CREATE TABLE Customers (name VARCHAR(255), address VARCHAR(255)")

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)