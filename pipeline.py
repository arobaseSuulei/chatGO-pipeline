import mysql.connector

conn = mysql.connector.connect(
    
    user="chatgouser",
    password="123",
    host="127.0.0.1",
    database="chatGO"  # ou chatGO_data
)
print("Connecté !")
conn.close()
