import mysql.connector

# Replace with your connection details
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234567890'
)

cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE abdul")

print("All Done")
