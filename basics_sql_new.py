import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password"
)

print(mydb)

mycursor =mydb.cursor("CREATE DATABASE pythonprogramming")