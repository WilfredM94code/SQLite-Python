# -----------------------------------------------------------------
# ---------------------- SQLite for Python  -----------------------
# -----------------------------------------------------------------

# SQLite is a DBMS which is serverless and works locally on the PC where
# executed which access files and data within make accessing and managing
# data extremely fast. No instalation is required and no server config is
# required either. It's self contained (no extra dependencies) and runs
# in several platforms

# -----------------------------------------------------------------
# ------------------ SQLite creating a Database -------------------
# -------------------------- and tables ---------------------------
# -----------------------------------------------------------------

import sqlite3

with sqlite3.connect('test.db') as connection:
    print(type(connection))
    cursor = connection.cursor()
    print(type(cursor))
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Movies (
                        Title TEXT,
                        Director TEXT,
                        Year INT
                    )
                ''')
    connection.commit()

# This with statement allows us to wotk with a particular database aliased
# as 'connection' within the with block.

# The 'sqlite3.connect('test.db')' gives as result a database saved at the
# CWD and makes a <class 'sqlite3.Connection'> object

# The 'connection.cursor()' returns a <class 'sqlite3.Cursor'> which is the
# object employed to create tables within a <class 'sqlite3.Connection'>
# object wich is itself a database

# The 'cursor.execute()' method recieves the SQL query instruction and puts
# it in place to be commited into the table

# The 'connection.commit()' method executes the SQL instruction stord at
# the <class 'sqlite3.Connection'> object

# This with statement allows to  create a database if it does not exists
# or to sstablish a connection if the database exists

# Note: There has to be considered that when typing SQL queries one must
# have # consideration for the keywords on the SQL paradigm (a table
# cannot be named 'Table' for instance)

# -----------------------------------------------------------------
# ---------------- SQLite adding and fetching data ----------------
# -------------------------- from table ---------------------------
# -----------------------------------------------------------------

with sqlite3.connect('test.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Movies (
                        Title TEXT,
                        Director TEXT,
                        Year INT
                    )
                ''')
    # Adding a row of data
    cursor.execute(
        'INSERT INTO Movies VALUES ("Avatar","James Cameron", 2009)')
    # Fetching a row of data
    cursor.execute('SELECT * FROM Movies')
    print(cursor.fetchone())
    connection.commit()

# Using the 'cursor.execute()' method we add the SQL instruction to add
# data to our Movie table. This instruction recieve data for 3 fields.
# Each field is contained as the position of a tuple and it is passed
# in order to the table

# Note: The with statement either connects to the 'test.db' or creates
# if it doesnt exists it creates and connects to it, then the 
# 'CREATE TABLE IF NOT EXISTS' creates a table if it does not exists, but
# it does now so this instruction gets without effect after the 1st 
# execution of the statement

# Then, when fetching data, the instruction is passed as well employing
# the 'cursor.execute()' method. Then, the data selected gets available 
# to be fetched using the method 'cursor.fetchone()'

# To add several more records lists are useful

movies = [
    ('The dark knight','Christopher Nolan', 2008),
    ('Unglorious Basterds','Quentin Tarantino', 2009),
    ('Fight Club','David Fincher',1999)
]

with sqlite3.connect('test.db') as connection:
    cursor = connection.cursor()
    # Adding data
    cursor.executemany('INSERT INTO Movies VALUES (?,?,?)',movies)
    # Fetching data
    records = cursor.execute('SELECT * FROM Movies')
    for record in records:
        print (record)
    connection.commit()

# Note: The 'cursor.execute('SELECT * FROM Movies')' instruction returns
# an interable that once iterated it becomes 'None' that why its been 
# stored within a variable called 'record'

# The filtering data process is done using the SQL instructions

year = (2000,)

with sqlite3.connect('test.db') as connection:
    cursor = connection.cursor()
    # Fetching data
    cursor.execute('SELECT * FROM Movies WHERE Year >?',year)
    #####
    # 1st approach
    print (cursor.fetchall())
    # Single use iterator can't be called once more used


with sqlite3.connect('test.db') as connection:
    cursor = connection.cursor()
    # Fetching data
    filtered_movies = cursor.execute('SELECT * FROM Movies WHERE Year >?',year)
    #####
    # 2nd approach
    for movie in filtered_movies:
        print (movie)
    # Single use iterator can't be called once more used

# In these particular cases, the data is filtered by year, excluding a movie
# In both cases, the returning value is an interator

# The 'filtered_movies' stores the iterator returned from the 
# 'cursor.execute('SELECT * FROM Movies WHERE Year >?',year)' method

# The 'cursor.fetchall()' method returns an interator, the last one added 
# to the <class 'sqlite3.Cursor'>
