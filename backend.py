import sqlite3
'''
This file contains necessary functions for modifying
and querying the sqlite3 'professors' database.
'''
######################################################
##       FUNCTIONS FOR PROFS TABLE                  ##
######################################################
def insert(samID, firstName, lastName, email, cv, docYear, docType, mastYear, mastType, experience, profType, onlineCert):
    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO profs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (samID, firstName, lastName, email, cv, docYear, docType, mastYear, mastType, experience, profType, onlineCert))
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

def search(samID="", firstName="", lastName="", email="", cv="", docYear="", docType="", mastYear="", mastType="", experience="", profType="", onlineCert=""):
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
    if (onlineCert=="") or (onlineCert=="None"):
        onlineCert=-1
    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM profs WHERE samID=? OR firstName=? OR lastName=? OR email=? OR cv=?
                OR doctorate_year=? OR doctorate_type=? OR masters_year=? OR masters_type=? OR experience=? OR profType=?""",
                (samID, firstName, lastName, email, cv, docYear, docType, mastYear, mastType, experience, profType, onlineCert))
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
def update(samID, firstName, lastName, email, cv, docYear, docType, mastYear, mastType, experience, profType, onlineCert):
    # Clean the inputs. If the string is "None" or "", must change to the python None type before updating.
    if (firstName == "") or (firstName == "None") or (firstName == None):
        firstName = ""
    if (lastName == "") or (lastName == "None"):
        lastName = ""
    if (email == "") or (email == "None"):
        email = ""
    if (cv == "") or (cv == "None"):
        cv = ""
    if (docYear == "") or (docYear == "None"):
        docYear = ""
    if (mastYear == "") or (mastYear == "None"):
        mastYear = ""
    if (mastType == "") or (mastType == "None"):
        mastType = ""
    if (experience == "") or (experience == "None"):
        experience = ""
    if (profType == "") or (profType == "None"):
        profType = ""
    if (onlineCert == "") or (onlineCert == "None"):
        onlineCert = ""

    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("""UPDATE profs SET firstName=?, lastName=?, email=?, cv=?, doctorate_year=?,
                doctorate_type=?, masters_year=?, masters_type=?, experience=?, profType=?, onlineCert=? WHERE samID=?""",
                (firstName, lastName, email, cv, docYear, docType, mastYear, mastType, experience, profType, onlineCert, samID))
    conn.commit()
    conn.close()

def getDoctoralOnly():
    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM profs WHERE doctorate_year IS NOT NULL AND doctorate_year!=\'\' AND doctorate_year != \'None\'")
    rows = cur.fetchall()
    conn.close()
    return rows

def getMastersOnly():
    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM profs WHERE doctorate_year IS NULL OR doctorate_year=\'\' OR doctorate_year=\'None\'")
    rows = cur.fetchall()
    conn.close()
    return rows

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
    searchString = "SELECT * FROM courses WHERE"
    count = 0
    
    if (semester=="") or (semester=="None"):
        semester = "-1"
    else:
        searchString += " semester= \'" + str(semester) + "\'"
        count += 1
    

    if (year=="") or (year=="None"):
        year = -1
    else:
        if (count==0):
            searchString += " year=\'" + str(year) + "\'"
            count +=1
        else:
            searchString += " AND year=\'" + str(year) + "\'"
            count +=1


    if (courseNum=="") or (courseNum=="None"):
        courseNum=-1
    else:
        if (count==0):
            searchString += " courseNum=\'" + str(courseNum) + "\'"
            count += 1
        else:
            searchString += " AND courseNum=\'" + str(courseNum) + "\'"
            count +=1


    if (sectionNum=="") or (sectionNum=="None"):
        sectionNum=-1
    else:
        if (count==0):
            searchString += " sectionNum=\'" + str(sectionNum) + "\'"
            count += 1
        else:
            searchString += " AND sectionNum=\'" + str(sectionNum) + "\'"
            count +=1


    if (instructorID=="") or (instructorID=="None"):
        instructorID=-1
    else:
        if (count==0):
            searchString += " instructorID=\'" + str(instructorID) + "\'"
            count += 1
        else:
            searchString += " AND instructorID=\'" + str(instructorID) + "\'"
            count +=1


    if (instructorLastName=="") or (instructorLastName=="None"):
        instructorLastName="-1"
    else:
        if (count==0):
            searchString += " instructorLastName=\'" + str(instructorLastName) + "\'"
            count += 1
        else:
            searchString += " AND instructorLastName=\'" + str(instructorLastName) + "\'"
            count +=1


    if (instructionMethod=="") or (instructionMethod=="None"):
        instructionMethod=-1
    else:
        if (count==0):
            searchString += " instructionMethod=\'" + str(instructionMethod) + "\'"
            count += 1
        else:
            searchString += " AND instructionMethod=\'" + str(instructionMethod) + "\'"
            count +=1


    if (ideaScore=="") or (ideaScore=="None"):
        ideaScore=-1.1
    else:
        if (count==0):
            searchString += " ideaScore=\'" + str(ideaScore) + "\'"
            count += 1
        else:
            searchString += " AND ideaScore=\'" + str(ideaScore) + "\'"
            count +=1


    if (count != 0):
        #print(searchString)
        conn = sqlite3.connect("professors.db")
        cur = conn.cursor()
        cur.execute(searchString)
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

# Update assumes that the samID is correct and will only change the other fields.
def update_courses(semester='', year='', courseNum='', sectionNum='', instructorID='', instructorLastName='', instructionMethod='', ideaScore=''):
    conn = sqlite3.connect("professors.db")
    cur = conn.cursor()
    cur.execute("""UPDATE courses SET instructorID=?, instructorLastName=?, instructionMethod=?, ideaScore=?
                 WHERE semester=? AND year=? AND courseNum=? AND sectionNum=?""",
                (instructorID, instructorLastName, instructionMethod, ideaScore, semester, year, courseNum, sectionNum))
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
