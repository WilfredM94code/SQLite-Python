# Create a table called students and within the table add the following columns
# 1- Student ID
# 2- First Name
# 3- Last Name
# 4- Email Address

# After the table is created, insert four records into the Database
# Once the Database is populated with data, query the database to retrieve all the email addresses

# For solution, use the following two approaches
# 1- SQLite module
# 2- SQLAlchemy

import sqlite3

student_data = [
    ('Wilfred','Medina','WilfredM9acode@gmail.com'),
    ('Elon','Musk','rockets_and_stuff@gmail.com'),
    ('Wilmer','Medina','wilmer.medina24@gmail.com'),
    ('Albert','Einstein','spacetime@gmail.com')
]

with sqlite3.connect('students.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Students (
                        Student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        First_name TEXT NOT NULL,
                        Last_name TEXT NOT NULL,
                        Email_address TEXT NOT NULL
                    )
                ''')
    connection.commit()
    cursor.executemany('INSERT INTO Students VALUES (NULL,?,?,?)',student_data)
    cursor.execute('SELECT st.Email_address FROM Students st')
    print(cursor.fetchall())