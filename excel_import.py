import os
import copy
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import filedialog
# Import backend.py too for database insertion
import backend


class ExcelImportCourses:
    def __init__(self):
        self.file = None
        self.dataframe = None
        self.rowList = []
        self.columnNum = 0

    def add_rows(self):
        # First prompt the user to pick their Excel file.
        # Safeguard, keep prompting user for a new file if the number of columns != 7.
        while self.columnNum != 8:
            # Prompt the user with filedialog.
            myFilename = filedialog.askopenfilename(initialdir='/', title="Select an Excel sheet to import Courses.",
                                               filetypes=(("Excel Files", "*.xlsx"), ("All Files", "*.*")))
            self.file = myFilename
            # Added for bugs. Don't allow a user to pick a directory.
            # Retreive the dataframe object from the excel file.
            if not os.path.isdir(self.file):
                df = pd.read_excel(self.file, engine='openpyxl')
                self.dataframe = df
                columnLen = 0
                for key in df:
                    columnLen += 1
                self.columnNum = columnLen

        # Clean the dataframe object. Remove all NaN where the cell was empty.
        # If there was not a value within the cell
        # in the Excel file, then it will be equal to "nan". Need
        # to change all of these to an empty string "".
        self.dataframe = self.dataframe.where(pd.notnull(df), "")

        # Create the new window to show the imported excel file before touching the db
        top = Toplevel()
        myTitle = "Import Excel File for Courses"
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

        myString = "File chosen: "
        myString += str(self.file)
        myString += '\n\n'
        textBox.insert(END, myString)
        # Now parse the dataframe object into a 2-d list.
        # One row of the excel file will be a list of strings.
        for i in range(len(self.dataframe)):
            tempRow = []
            for key in self.dataframe:
                tempRow.append(str(self.dataframe[key][i]))
            self.rowList.append(tempRow)

        # Display the rows that were successfully added.
        for i in range (len(self.rowList)):
            # Edge case, do not add rows that are all empty.
            if self.rowList[i][0] == "" and self.rowList[i][1]=="" and self.rowList[i][2]=="" and self.rowList[i][3]=="" and self.rowList[i][4]=="" and self.rowList[i][5]=="" and self.rowList[i][6]=="" and self.rowList[i][7]=="":
                myString = 'Error in row ' + str(i+1) + ': ' + str(self.rowList[i]) + '. It was not added because all fields were empty.\n\n'
                textBox.insert(END, myString)
                continue
            # Edge case, do not add rows that have an empty string in one of the required fields. 
            # Note: empty string != NULL, so SQLite will still add it.
            if self.rowList[i][0] == "" or self.rowList[i][1]=="" or self.rowList[i][2]=="" or self.rowList[i][3]=="":
                myString = 'Error in row ' + str(i+1) + ': ' + str(self.rowList[i]) + '. It was not added because one of the primary fields was empty.\n\n'
                textBox.insert(END, myString)
                continue               
            try:
                backend.insert_courses(self.rowList[i][0], self.rowList[i][1], self.rowList[i][2], self.rowList[i][3],
                                       self.rowList[i][4], self.rowList[i][5], self.rowList[i][6], self.rowList[i][7])
                myString = 'Row ' + str(i+1) + ': ' + str(self.rowList[i]) + ' was successfully added.\n\n'
                textBox.insert(END, myString)
            except:
                myString = 'Error in row ' + str(i+1) + ': ' + str(self.rowList[i]) + '. It was not added.\n\n'
                textBox.insert(END, myString)
        



class ExcelImportProfs:
    def __init__(self):
        self.file = None
        self.dataframe = None
        self.rowList = []
        self.columnNum = 0

    def add_rows(self):
        # First prompt the user to pick their Excel file.
        # Safeguard, keep prompting user for a new file if the number of columns != 7.
        while self.columnNum != 12:
            # Prompt the user with filedialog.
            myFilename = filedialog.askopenfilename(initialdir='/', title="Select an Excel sheet to import Professors.",
                                               filetypes=(("Excel Files", "*.xlsx"), ("All Files", "*.*")))
            self.file = myFilename
            # Added for bugs. Don't allow a user to pick a directory.
            # Retreive the dataframe object from the excel file.
            if not os.path.isdir(self.file):
                df = pd.read_excel(self.file, engine='openpyxl')
                self.dataframe = df
                columnLen = 0
                for key in df:
                    columnLen += 1
                self.columnNum = columnLen
        
        # Clean the dataframe object. Remove all NaN where the cell was empty.
        # If there was not a value within the cell
        # in the Excel file, then it will be equal to "nan". Need
        # to change all of these to an empty string "".
        self.dataframe = self.dataframe.where(pd.notnull(df), "")

        # Create the new window to show the imported excel file before touching the db
        top = Toplevel()
        myTitle = "Import Excel File for Professors"
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

        myString = "File chosen: "
        myString += str(self.file)
        myString += '\n\n'
        textBox.insert(END, myString)
        # Now parse the dataframe object into a 2-d list.
        # One row of the excel file will be a list of strings.
        for i in range(len(self.dataframe)):
            tempRow = []
            for key in self.dataframe:
                tempRow.append(str(self.dataframe[key][i]))
            self.rowList.append(tempRow)

        # Display the rows that were successfully added.
        for i in range (len(self.rowList)):
            # Edge case, do not add rows that are all empty.
            if self.rowList[i][0] == "" and self.rowList[i][1]=="" and self.rowList[i][2]=="" and self.rowList[i][3]=="" and self.rowList[i][4]=="" and self.rowList[i][5]=="" and self.rowList[i][6]=="" and self.rowList[i][7]=="" and self.rowList[i][8]=="" and self.rowList[i][9]=="" and self.rowList[i][10]=="" and self.rowList[i][11]=="":
                myString = 'Error in row ' + str(i+1) + ': ' + str(self.rowList[i]) + '. It was not added because all fields were empty.\n\n'
                textBox.insert(END, myString)
                continue
            # Edge case, do not add rows that have an empty string in the required samID field. 
            # Note: empty string != NULL, so SQLite will still add it.
            if self.rowList[i][0] == "":
                myString = 'Error in row ' + str(i+1) + ': ' + str(self.rowList[i]) + '. It was not added because the primary field samID was empty.\n\n'
                textBox.insert(END, myString)
                continue   
            try:
                backend.insert(self.rowList[i][0], self.rowList[i][1], self.rowList[i][2], self.rowList[i][3],
                                       self.rowList[i][4], self.rowList[i][5], self.rowList[i][6], self.rowList[i][7], 
                                       self.rowList[i][8], self.rowList[i][9], self.rowList[i][10], self.rowList[i][11])
                myString = 'Row ' + str(i+1) + ': ' + str(self.rowList[i]) + ' was successfully added.\n\n'
                textBox.insert(END, myString)
            except:
                myString = 'Error in row ' + str(i+1) + ': ' + str(self.rowList[i]) + '. It was not added.\n\n'
                textBox.insert(END, myString)
        

