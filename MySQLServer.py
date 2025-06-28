
import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="qualitytech3",     # replace with your username
        password="Bg@2024!@#"  # replace with your password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    prin("except mysql.connector.Error")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
