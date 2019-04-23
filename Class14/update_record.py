#Notice the WHERE clause in the UPDATE syntax:
#The WHERE clause specifies which record or records that should be updated.
#If you omit the WHERE clause, all records will be updated!

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Welcome@123",
    database="mydb1"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Bandra' WHERE address = 'hsr'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")