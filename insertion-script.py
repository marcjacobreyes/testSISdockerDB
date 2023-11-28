import csv
import pymysql

# Connect to the MySQL ascender database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="ascender"
)

# Create a cursor object
cursor = connection.cursor()

# Open the CSV file
with open('./csvFiles/ascender-data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    # Iterate over each row in the CSV file
    for row in reader:
        # Extract data from each row
        first_name = row['First Name']
        last_name = row['Last Name']
        student_id = row['Student ID']
        grade = row['Grade']
        short_name = row['Short Name']

        # Insert data into the 'student' table
        sql = "INSERT INTO students (first_name, last_name, student_id, grade, short_name) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (first_name, last_name, student_id, grade, short_name))

# Commit the changes to the database
connection.commit()

# Close the cursor object and database connection
cursor.close()
connection.close()
