#!/usr/bin/env python3
from tkinter import *
import os
import backend


class ProfReport:
    def __init__(self, selected_tuple):
        self.selected_tuple = selected_tuple
        self.samID = selected_tuple[0]
        self.firstName = selected_tuple[1]
        self.lastName = selected_tuple[2]
        self.email = selected_tuple[3]
        self.cv = selected_tuple[4]
        self.doctorateYear = selected_tuple[5]
        self.doctorateType = selected_tuple[6]
        self.mastersYear = selected_tuple[7]
        self.mastersType = selected_tuple[8]
        self.experience = selected_tuple[9]
        self.profType = selected_tuple[10]
        self.onlineCert = selected_tuple[11]


    def create_report(self):
        # Create the new window and grid widgets
        top = Toplevel()
        myTitle = "Professor Credentials for: " + str(self.firstName) + " " + str(self.lastName)
        top.wm_title(myTitle)
        textBox = Text(top, height=20, width=70)
        textBox.grid(row=0, column=0, sticky='nsew')
        myScrollBar = Scrollbar(top, orient='vertical')
        myScrollBar.grid(row=0, column=1, sticky='nsew')
        textBox.configure(yscrollcommand=myScrollBar.set)
        myScrollBar.configure(command=textBox.yview)

        # Make the 'top' window, textbox, and scroll bar resizable
        Grid.rowconfigure(top, 0, weight=1)
        Grid.columnconfigure(top, 0, weight=1)
        


        # Populate the text box
        myString = "Professor Credentials for: " + str(self.firstName) + " " + str(self.lastName)
        textBox.insert(END, myString)
        textBox.insert(END, str('\n\n'))

        myString = "SamID: " + str(self.samID) + str('\n')
        textBox.insert(END, myString)
        
        myString = "Professor Type: "
        theType = ''
        if self.profType == 1:
            theType = 'Full Time'
        elif self.profType == 2:
            theType = 'Doctoral Teaching'
        elif self.profType == 3:
            theType = 'Overload'
        elif self.profType == 4:
            theType = 'Lecturer/Adjunct'
        else:
            theType = 'Not Specified'
        myString += theType + '\n'
        textBox.insert(END, myString)
        
        myString = "email: " + str(self.email) + str('\n\n')
        textBox.insert(END, myString)
        myString = "Doctorate Degree Year: " + str(self.doctorateYear) + str('\n')
        textBox.insert(END, myString)
        myString = "Doctorate Degree Spec: " + str(self.doctorateType) + str('\n')
        textBox.insert(END, myString)
        myString = "Master's Degree Year: " + str(self.mastersYear) + str('\n')
        textBox.insert(END, myString)
        myString = "Master's Degree Spec: " + str(self.mastersType)+ str('\n')
        textBox.insert(END, myString)
        myString = "Online Certification: "
        certString = ''
        if (self.onlineCert == 0):
            certString = "No"
        elif (self.onlineCert == 1):
            certString = "Yes"
        else:
            certString = "N/A"
        myString += certString + '\n\n'
        textBox.insert(END, myString)
        myString = "Experience: " + str('\n') + str(self.experience) + str('\n\n')
        textBox.insert(END, myString)

        # Pull courses the professor has taught from courses table
        courses = backend.prof_report(self.samID)

        # Calculate the average IDEA score for the professor across all courses.
        ideaSum = 0
        ideaCount = 0
        for i in range (len(courses)):
            if (courses[i][7] != None):
                ideaSum += courses[i][7]
                ideaCount += 1
        if (ideaCount == 0):
            myString = "Average IDEA score across all courses taught: N/A\n\n"
        else:
            ideaAvg = ideaSum / ideaCount
            ideaAvgString = "%.2f" % ideaAvg
            myString = "Average IDEA score across all courses taught: " + ideaAvgString + "\n\n"
        textBox.insert(END, myString)
        
        myString = "Courses Taught: " + str('\n')
        textBox.insert(END, myString)
        for i in range (len(courses)):
            myString = str(courses[i][0]) + " " + str(courses[i][1]) + " "
            myString += "Course " + str(courses[i][2]) + ", "
            myString += "Section " + str(courses[i][3]) + " "
            if (courses[i][6] == 1):
                myString += "(In-person)"
            if (courses[i][6] == 2):
                myString += "(Online)"
            if (courses[i][6] == 3):
                myString += "(Remote Sync)"
            myString += " IDEA score = " + str(courses[i][7])
            myString += '\n'
            textBox.insert(END, myString)
            


class CourseReport:
    def __init__ (self, semester, year, courseNum):
        self.semester = semester
        self.year = year
        self.courseNum = courseNum

    def create_report(self):
        # Create the new window and grid widgets
        top = Toplevel()
        myTitle = "Course Report for: " + str(self.semester) + " " + str(self.year) + " CRIJ " + str(self.courseNum)
        top.wm_title(myTitle)
        textBox = Text(top, height=20, width=65)
        textBox.grid(row=0, column=0, sticky='nsew')
        myScrollBar = Scrollbar(top, orient='vertical')
        myScrollBar.grid(row=0, column=1, sticky='nsew')
        textBox.configure(yscrollcommand=myScrollBar.set)
        myScrollBar.configure(command=textBox.yview)

        # Make the 'top' window, textbox, and scroll bar resizable
        Grid.rowconfigure(top, 0, weight=1)
        Grid.columnconfigure(top, 0, weight=1)

        # Populate the text box
        myString = "Course Report for: " + str(self.semester) + " " + str(self.year) + " CRIJ " + str(self.courseNum)
        textBox.insert(END, myString)
        textBox.insert(END, str('\n\n'))
        
        # Pull courses list from the database
        courses = backend.course_report(self.semester, self.year, self.courseNum)
       
        # Display instruction method stats.
        myString = "Total sections found: " + str(len(courses)) + "\n"
        textBox.insert(END, myString)
        
        myString = "Total F2F sections: "
        count = 0
        for i in range (len(courses)):
            if (courses[i][6] == 1):
                count += 1
        myString += str(count) + "\n"
        textBox.insert(END, myString)
           
        myString = "Total Online/Remote sections: "
        count = 0
        remote_count = 0
        for i in range (len(courses)):
            if (courses[i][6] == 2) or (courses[i][6] == 3):
                count += 1
            if (courses[i][6] == 3):
                remote_count += 1
        myString += str(count)
        if (remote_count > 0):
            myString += "(Includes " + str(remote_count) + " being 100% Remote)\n\n"
        else:
            myString += "\n\n"
        textBox.insert(END, myString)

        # Display professor stats.
        myString = "Total number of professors: "
        prof_ID_list = []
        for i in range (len(courses)):
            if (courses[i][4] not in prof_ID_list):
                prof_ID_list.append(courses[i][4])
        myString += str(len(prof_ID_list)) + "\n"
        textBox.insert(END, myString)

        # Get the number of each type of professor.
        fullTime_count = 0
        doctoralTeach_count = 0
        overload_count = 0
        adjunct_count = 0
        error_count = 0
        for i in range (len(prof_ID_list)):
            profRow = backend.get_prof_info(prof_ID_list[i])
            if profRow[0][10] == 1:
                fullTime_count += 1
            elif profRow[0][10] == 2:
                doctoralTeach_count += 1
            elif profRow[0][10] == 3:
                overload_count += 1
            elif profRow[0][10] == 4:
                adjunct_count += 1
            else:
                error_count += 1
        # Display professor type sums.
        myString = "Number of Full Time: " + str(fullTime_count) + "\n"
        textBox.insert(END, myString)
        myString = "Number of Doctoral Teaching: " + str(doctoralTeach_count) + "\n"
        textBox.insert(END, myString)
        myString = "Number of Overload: " + str(overload_count) + "\n"
        textBox.insert(END, myString)
        myString = "Number of Adjunct/Lecturer: " + str(adjunct_count) + "\n\n"
        textBox.insert(END, myString)
        if error_count > 0:
            myString = """There has been one or more errors in the typing calculation.
                        Please make sure all professors have the field for their
                        type (profType, field 11) filled in within the profs table.\n\n"""
            textBox.insert(END, myString)

        
        # List all of the sections.
        myString = "List of all sections: \n"
        textBox.insert(END, myString)
        for i in range (len(courses)):
            myString = "Section " + str(courses[i][3])
            if (courses[i][6]==1):
                myString += " (F2F): "
            if (courses[i][6]==2):
                myString += " (Online): "
            if (courses[i][6]==3):
                myString += " (Remote Sync): "
            myString += "Taught by " + str(courses[i][5]) + " (samID:" + str(courses[i][4])
            myString += ")\n"
            myString +="\tIDEA score = " + str(courses[i][7]) + "\n"
            textBox.insert(END, myString)
        myString = "\n\n"
        textBox.insert(END, myString)
            
               
        myString = "Professor Credentials: \n\n"
        textBox.insert(END, myString)
        for i in range (len(prof_ID_list)):
            currInfo = backend.get_prof_info(prof_ID_list[i])
            myString = str(currInfo[0][1]) + " " + str(currInfo[0][2]) + " ("
            # Get the professor type
            if currInfo[0][10] == 1:
                myString += "Full Time):\n"
            elif currInfo[0][10] == 2:
                myString += "Doctoral Teaching):\n"
            elif currInfo[0][10] == 3:
                myString += "Overload):\n"
            elif currInfo[0][10] == 4:
                myString += "Lecturer/Adjunct):\n"
            else:
                myString += "Unspecified):\n"
            textBox.insert(END, myString)
            myString = str(currInfo[0][9]) + "\n\n"
            textBox.insert(END, myString)
            '''
            # This section is still in testing. It retreives the title of the professor and appends it
            # to their name. (e.g. Tim Well, M.S.)
            profTitle = ''
            titlePointer = 0
            if (len(currInfo) >= 1):
                myString = str(currInfo[0][2]) + " " + str(currInfo[0][3]) + ", "
                # Get the Ph.D., J.D., M.S., etc. for the name
                if (currInfo[0][7] != '')and(currInfo[0][7] != 'None')and(currInfo[0][7] != 'NULL')and(currInfo[0][7] != None):
                    while (currInfo[0][7][titlePointer] != ' ') and (titlePointer < len(currInfo[0][7])-1):
                        profTitle += currInfo[0][7][titlePointer]
                        titlePointer += 1
                if (profTitle != ''):
                    myString += profTitle + ' '

                profTitle=''
                titlePointer=0
                if (currInfo[0][9] != '')and(currInfo[0][9] != 'None')and(currInfo[0][9] != 'NULL')and(currInfo[0][9] != None):
                    while (currInfo[0][9][titlePointer] != ' ') and (titlePointer < len(currInfo[0][9])-1):
                        profTitle += currInfo[0][9][titlePointer]
                        titlePointer += 1
                if (profTitle != ''):
                    myString += profTitle

                myString += ":\n"
                myString += str(currInfo[0][10]) + "\n\n"
                textBox.insert(END, myString)
            '''