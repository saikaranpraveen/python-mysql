import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="sakila"
)

mycursor = mydb.cursor()

sql = "DELETE FROM actors WHERE first_name = 'ADAM'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
