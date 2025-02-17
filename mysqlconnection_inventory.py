import mysql.connector

# Database Configuration
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",  # Change if needed
    password="dombby12##",  # Add your MySQL password
    database="inventory_db"
)
cursor = db.cursor()
