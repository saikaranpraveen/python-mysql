import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="sakila"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)