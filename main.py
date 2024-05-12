from config import db_config
import psycopg2

connection = psycopg2.connect(**db_config)
cursor = connection.cursor()

cursor.execute('SELECT * FROM students')
students = cursor.fetchall()
print(students)