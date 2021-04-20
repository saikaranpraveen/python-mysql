import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="sakila"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM actors LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)