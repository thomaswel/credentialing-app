#import tkinter as tk
from tkinter import *
import os
import excel_import
import template_copy
import pdf_import


#@param window_name, Tk() object that serves as the main window in the program.
def make_menu(window_name):
    # Make the main menu bar in the window that was passed in.
    my_menu = Menu(window_name)
    window_name.config(menu=my_menu)

    # Create the File menu item.
    file_menu = Menu(my_menu)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Exit", command = window_name.destroy)

    # Create a Import menu item
    import_menu = Menu(my_menu)
    my_menu.add_cascade(label="Import", menu=import_menu)
    import_menu.add_command(label="Get Professor Import Template", command = copy_prof_template)
    import_menu.add_command(label="Get Courses Import Template", command = copy_course_template)
    import_menu.add_separator()
    import_menu.add_command(label="Import Professors (Excel)", command = import_excel_profs)
    import_menu.add_command(label="Import Courses (Excel)", command = import_excel_courses)
    import_menu.add_separator()
    import_menu.add_command(label="Import Curriculum Vitae (PDF)", command = import_cv)

    # Create the Help menu item
    help_menu = Menu(my_menu)
    my_menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="User Manual", command = open_usermanual)


def nothing_func():
    print('hi')

def import_excel_courses():
    try:
        myImportWindow = excel_import.ExcelImportCourses()
        myImportWindow.add_rows()
    except:
        pass

def import_excel_profs():
    try:
        myImportWindow = excel_import.ExcelImportProfs()
        myImportWindow.add_rows()
    except:
        pass

def copy_course_template():
    try:
        myCopyWindow = template_copy.GetCourseTemplate()
        myCopyWindow.get_destination()
    except:
        pass

def copy_prof_template():
    try:
        myCopyWindow = template_copy.GetProfTemplate()
        myCopyWindow.get_destination()
    except:
        pass

def import_cv():
    try:
        myCVWindow = pdf_import.ImportCV()
        myCVWindow.get_file()
    except:
        pass

def open_usermanual():
    try:
        os.startfile(".\\Assets\\Documentation\\UserManual.pdf")
    except:
        pass

