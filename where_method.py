import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="sakila"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM actors WHERE first_name ='ADAM'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)