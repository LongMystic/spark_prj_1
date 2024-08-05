import mysql.connector
import random
from faker import Faker
from datetime import date
from utils.utils import get_age_from_dob

faker = Faker()

mydb = mysql.connector.connect(
    host="localhost",
    username="admin",
    password="password",
    database="spark_prj_1"
)

my_cursor = mydb.cursor()
num_of_records = 1000000

sql = """
    INSERT INTO users (firstName, lastName, date_of_birth, age, address)
    VALUES (%s, %s, %s, %s, %s)
"""


for i in range(1, num_of_records + 1):
    dob = faker.date_of_birth(minimum_age=15, maximum_age=70)
    val = [
        faker.first_name(), faker.last_name(), dob, get_age_from_dob(dob), faker.address()
    ]
    my_cursor.execute(sql, val)


mydb.commit()

print(my_cursor.rowcount, "was inserted")

sql = """
    INSERT INTO accounts (username, password, email, createdDate, user_id)
    VALUES (%s, %s, %s, %s, %s)
"""

for i in range(1, num_of_records + 1):
    for _ in range(random.randint(0, 4)):
        val = [
            faker.user_name(),
            faker.password(),
            faker.email(),
            faker.date_between(start_date=date(2018, 1, 1)),
            i
        ]

        my_cursor.execute(sql, val)

mydb.commit()
