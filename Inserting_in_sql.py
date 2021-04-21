import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="pythonprogramming"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Dhoni", "Chepauk 07")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")