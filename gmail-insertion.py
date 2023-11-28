import csv
import os

def add_gmail_column(input_file, output_file):
  """Adds a new Gmail field to all users in the input CSV file and writes the output to the output CSV file.

  Args:
    input_file: The path to the input CSV file.
    output_file: The path to the output CSV file.
  """

  if not os.path.exists(input_file):
    raise FileNotFoundError(f"Input CSV file {input_file} does not exist.")

  if os.path.exists(output_file):
    raise FileExistsError(f"Output CSV file {output_file} already exists.")

  with open(input_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    rows = list(reader)

  for row in rows:
    user_role = row[5]

    # Get the first and last name.
    first_name = row[8]
    last_name = row[9]

    # Format the Gmail address based on the user role.
    if user_role == "teacher":
      gmail = f"{first_name}.{last_name}@bcisdistrict.net"
    else:
      gmail = f"{last_name}.{first_name}@bcisdistrict.net"

    # Insert the Gmail field into the row.
    row.insert(18, gmail)

  with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['sourcedId', 'status', 'dateLastModified', 'enabledUser',
                     'orgSourcedIds', 'role', 'username', 'userIds', 'givenName',
                     'familyName', 'middleName', 'identifier', 'email', 'sms',
                     'phone', 'agentSourcedIds', 'grades', 'password', 'gmail'])

    for row in rows:
      writer.writerow(row)

if __name__ == '__main__':
  input_file = './csvFiles/users.csv'
  output_file = './csvFiles/users-with-gmail.csv'

  add_gmail_column(input_file, output_file)
