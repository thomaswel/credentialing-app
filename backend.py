import sqlite3
'''
This file contains necessary functions for modifying
and querying the sqlite3 'professors' database.
'''

######################################################
##       FUNCTIONS FOR PROFS TABLE                  ##
######################################################
def insert(samID, firstName, lastName, email, cv, docYear, docType, mastYear, mastType, experience, profType):
    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO profs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (samID, firstName, lastName, email, cv, docYear, docType, mastYear, mastType, experience, profType))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM profs")
    #rows is a tuple containing all rows from db
    rows = cur.fetchall()
    conn.close()
    return rows

def search(samID="", firstName="", lastName="", email="", cv="", docYear="", docType="", mastYear="", mastType="", experience="", profType=""):
    # Need the if statements because searching while fields were empty was pulling
    # up all records that had at least one empty field.
    if (samID=="") or (samID=="None"):
        samID = -1
    if (firstName=="") or (firstName=="None"):
        firstName = "-1"
    if (lastName=="") or (lastName=="None"):
        lastName="-1"
    if (email=="") or (email=="None"):
        email="-1"
    if (cv=="") or (cv=="None"):
        cv="-1"
    if (docYear=="") or (docYear=="None"):
        docYear=-1
    if (docType=="") or (docType=="None"):
        docType="-1"
    if (mastYear=="") or (mastYear=="None"):
        mastYear=-1
    if (mastType=="") or (mastType=="None"):
        mastType="-1"
    if (experience=="") or (experience=="None"):
        experience="-1"
    if (profType == "") or (profType=="None"):
        profType=-1
    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM profs WHERE samID=? OR firstName=? OR lastName=? OR email=? OR cv=?
                OR doctorate_year=? OR doctorate_type=? OR masters_year=? OR masters_type=? OR experience=? OR profType=?""",
                (samID, firstName, lastName, email, cv, docYear, docType, mastYear, mastType, experience, profType))
    #rows is a tuple containing all rows from db
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(samID):
    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM profs WHERE samID=?", (samID,))
    conn.commit()
    conn.close()

# Update assumes that the samID is correct and will only change the other fields.
def update(samID, firstName, lastName, email, cv, docYear, docType, mastYear, mastType, experience, profType):
    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("""UPDATE profs SET firstName=?, lastName=?, email=?, cv=?, doctorate_year=?,
                doctorate_type=?, masters_year=?, masters_type=?, experience=?, profType=? WHERE samID=?""",
                (firstName, lastName, email, cv, docYear, docType, mastYear, mastType, experience, profType, samID))
    conn.commit()
    conn.close()


###############################################################
# FUNCTIONS FOR COURSES TABLE
###############################################################
def view_courses():
    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses")
    #rows is a tuple containing all rows from db
    rows = cur.fetchall()
    conn.close()
    return rows

def insert_courses(semester, year, courseNum, sectionNum, instructorID, instructorLastName, instructionMethod, ideaScore):
    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO courses VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (semester, year, courseNum, sectionNum, instructorID, instructorLastName, instructionMethod, ideaScore))
    conn.commit()
    conn.close()

def search_courses(semester='', year='', courseNum='', sectionNum='', instructorID='', instructorLastName='', instructionMethod='', ideaScore=''):
    # need the if statements because searching while fields were empty was pulling
    # up all records that had at least one empty field.
    if (semester=="") or (semester=="None"):
        semester = "-1"
    if (year=="") or (year=="None"):
        year = -1
    if (courseNum=="") or (courseNum=="None"):
        courseNum=-1
    if (sectionNum=="") or (sectionNum=="None"):
        sectionNum=-1
    if (instructorID=="") or (instructorID=="None"):
        instructorID=-1
    if (instructorLastName=="") or (instructorLastName=="None"):
        instructorLastName="-1"
    if (instructionMethod=="") or (instructionMethod=="None"):
        instructionMethod=-1
    if (ideaScore=="") or (ideaScore=="None"):
        ideaScore=-1.1
    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM courses WHERE semester=? OR year=? OR courseNum=? OR sectionNum=?
                OR instructorID=? OR instructorLastName=? OR instructionMethod=? OR ideaScore=?""",
                (semester, year, courseNum, sectionNum, instructorID, instructorLastName, instructionMethod, ideaScore))
    #rows is a tuple containing all rows from db
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_courses(semester, year, courseNum, sectionNum):
    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM courses WHERE semester=? AND year=? AND courseNum=? AND sectionNum=?",
                (semester, year, courseNum, sectionNum))
    conn.commit()
    conn.close()


######################################################################
# FUNCTIONS FOR REPORT GENERATION
######################################################################

def prof_report (samID):
    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM courses WHERE instructorID=?""", (samID,))
    rows=cur.fetchall()
    conn.close()
    return rows

def course_report (semester, year, courseNum):
    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM courses WHERE semester=? AND year=? AND courseNum=?""",
                (semester, year, courseNum))
    rows=cur.fetchall()
    conn.close()
    return rows

def get_prof_info(samID):
    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM profs WHERE samID=?""",(samID,))
    rows=cur.fetchall()
    conn.close()
    return rows
