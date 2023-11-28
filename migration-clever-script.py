import pymysql
from psycopg2 import connect

# Connect to the MySQL source database
mysql_connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="ascender"
)

# Create a cursor object for the MySQL database
mysql_cursor = mysql_connection.cursor()

# Connect to the PostgreSQL target database using DB-API
postgresql_connection = connect(
    host="localhost",
    user="clever",
    password="cleverPGPassword",
    database="clever"
)

# Create a cursor object for the PostgreSQL database
postgresql_cursor = postgresql_connection.cursor()

# Extract data from the MySQL source table
mysql_cursor.execute("SELECT * FROM students")
student_data = mysql_cursor.fetchall()

# Convert data types if necessary
# For example, if the MySQL 'grade' column is an integer, but the PostgreSQL 'grade' column is a decimal,
# you would need to convert the data type here.

# Insert data into the PostgreSQL target table
for student in student_data:
    postgresql_cursor.execute("INSERT INTO students (first_name, last_name, student_id, grade, short_name) VALUES (%s, %s, %s, %s, %s)",
                               (student[0], student[1], student[2], student[3], student[4]))

# Commit the changes to the PostgreSQL database
postgresql_connection.commit()

# Close the cursor objects and database connections
mysql_cursor.close()
mysql_connection.close()
postgresql_cursor.close()
postgresql_connection.close()
