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
with open('./csvFiles/users-with-gmail.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    # Iterate over each row in the CSV file
    for row in reader:
        # Extract data from each row
        sourced_id = row['sourcedId']
        status = row['status']
        date_last_modified = row['dateLastModified']
        enabled_user = row['enabledUser']
        org_sourced_ids = row['orgSourcedIds']
        role = row['role']
        username = row['username']
        user_ids = row['userIds']
        given_name = row['givenName']
        family_name = row['familyName']
        middle_name = row['middleName']
        identifier = row['identifier']
        email = row['email']
        sms = row['sms']
        phone = row['phone']
        agent_sourced_ids = row['agentSourcedIds']
        grades = row['grades']
        password = row['password']
        gmail = row['gmail']

        # Insert data into the 'users' table
        sql = """INSERT INTO users (sourced_id, status, date_last_modified, enabled_user, org_sourced_ids, role, username, user_ids, given_name, family_name, middle_name, identifier, email, sms, phone, agent_sourced_ids, grades, password, gmail)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (sourced_id, status, date_last_modified, enabled_user, org_sourced_ids, role, username, user_ids, given_name, family_name, middle_name, identifier, email, sms, phone, agent_sourced_ids, grades, password, gmail))

# Commit the changes to the database
connection.commit()

# Close the cursor object and database connection
cursor.close()
connection.close()
