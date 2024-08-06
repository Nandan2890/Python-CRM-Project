import mysql.connector

dataBase = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = 'N@ndan2000'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crmproject")

print("All Done!")