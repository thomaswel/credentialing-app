import os
import sqlite3

'''
This script automatically exectues when the application starts.
It will make the correct directories if they do not exist,
and it will construct a database with the appropriate schema
if one does not already exist within the same directory.
'''

# Make directories if they do not exist.
def make_directories():
    if (not os.path.exists(r"./Assets")):
        os.mkdir(r"./Assets")
        os.mkdir(r"./Assets/CVs")
        os.mkdir(r"./Assets/Icons")
        os.mkdir(r"./Assets/Templates")
        os.mkdir(r"./Assets/Documentation")


# Make database if it does not exist.
def make_database():
    # Define connection to database
    conn = sqlite3.connect("professors.db")
    # Define a cursor object to execute SQL statements
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS profs (samID INTEGER NOT NULL, firstName TEXT, lastName TEXT, email TEXT, cv TEXT,
                doctorate_year INTEGER, doctorate_type TEXT, masters_year INTEGER, masters_type TEXT, experience TEXT, profType INTEGER, PRIMARY KEY(samID))""")
    cur.execute("""CREATE TABLE IF NOT EXISTS courses (semester TEXT NOT NULL, year INTEGER NOT NULL, courseNum INTEGER NOT NULL, sectionNum INTEGER NOT NULL,
                instructorID INTEGER, instructorLastName TEXT, instructionMethod INTEGER, ideaScore REAL, PRIMARY KEY(semester, year, courseNum, sectionNum))""")
    conn.commit()
    conn.close()


# Execute functions when imported
make_directories()
make_database()

