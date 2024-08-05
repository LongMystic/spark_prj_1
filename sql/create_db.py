import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="password"
)

my_cursor = mydb.cursor()

# create database
my_cursor.execute("CREATE DATABASE spark_prj_1")

