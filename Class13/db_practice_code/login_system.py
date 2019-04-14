import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Welcome@123",
    database="mydb1"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address, phone_no, pwd, data) VALUES (%s, %s, %s, %s, %s)"
val = ("SRK", "Ahmedabad","9978787640","abc@123", "i live in ahmedabad")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
