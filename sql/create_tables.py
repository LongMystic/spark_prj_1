import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="password",
    database="spark_prj_1"
)

my_cursor = mydb.cursor()

my_cursor.execute("DROP TABLE IF EXISTS users")
my_cursor.execute("""
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        firstName VARCHAR(255) NOT NULL,
        lastName VARCHAR(255) NOT NULL,
        date_of_birth DATE,
        age INT,
        address VARCHAR(255)
    )
""")

my_cursor.execute("DROP TABLE IF EXISTS accounts")
my_cursor.execute("""
    CREATE TABLE accounts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        createdDate DATE NOT NULL,
        user_id INT NOT NULL
    )
""")