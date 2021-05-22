#!/usr/bin/env python3
from tkinter import *
import os # for directory manipulation.
import backend # for database queries.
import reports # generate credentialing reports.
import startup # make correct directories on startup.
import menu # make menu at top of application.
from idlelib.tooltip import Hovertip # for pop-up tips.

'''
Author: Thomas Welborn
Position: Database Designer - Student Assistant (SHSU Department of Criminal Justice & Criminology)
Purpose: This program is designed to enable the database containing
professor and course catalog information to be easily modified and viewed using CRUD.
It uses the information within the database to produce credentialing
reports.
'''

# Grabs the currently selected listbox row for professors
# and adds the selected contents into the input fields.
def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    #fill out boxes with selected info
    e1.delete(0,END)
    e1.insert(END, selected_tuple[0])
    e2.delete(0,END)
    e2.insert(END, selected_tuple[1])
    e3.delete(0,END)
    e3.insert(END, selected_tuple[2])
    e4.delete(0,END)
    e4.insert(END, selected_tuple[3])
    e5.delete(0,END)
    e5.insert(END, selected_tuple[4])
    e6.delete(0,END)
    e6.insert(END, selected_tuple[5])
    e7.delete(0,END)
    e7.insert(END, selected_tuple[6])
    e8.delete(0,END)
    e8.insert(END, selected_tuple[7])
    e9.delete(0,END)
    e9.insert(END, selected_tuple[8])
    e10.delete(0,END)
    e10.insert(END, selected_tuple[9])
    profType_text.set(selected_tuple[10])
    onlineCert_text.set(selected_tuple[11])

# Grabs the currently selected listbox row for courses
# and adds the selected contents into the input fields.
def get_selected_row_courses(event):
    global selected_tuple2
    index = list2.curselection()[0]
    selected_tuple2 = list2.get(index)
    #e1c.delete(0,END)
    #e1c.insert(END, selected_tuple2[0])
    semester_text.set(selected_tuple2[0])
    e2c.delete(0,END)
    e2c.insert(END, selected_tuple2[1])
    e3c.delete(0,END)
    e3c.insert(END, selected_tuple2[2])
    e4c.delete(0,END)
    e4c.insert(END, selected_tuple2[3])
    e5c.delete(0,END)
    e5c.insert(END, selected_tuple2[4])
    e6c.delete(0,END)
    e6c.insert(END, selected_tuple2[5])
    #e7c.delete(0,END)
    #e7c.insert(END, selected_tuple2[6])
    instructMethod_text.set(selected_tuple2[6])
    e8c.delete(0,END)
    e8c.insert(END, selected_tuple2[7])

############################################################
##    FUNCTIONS FOR BUTTONS    #############################
############################################################
def report_command():
    try:
        myReport = reports.ProfReport(selected_tuple)
        myReport.create_report()
    except:
        pass

def report_command_courses():
    try:
        myCourseReport = reports.CourseReport(semester_text.get(), year_text.get(), courseNum_text.get())
        myCourseReport.create_report()
    except:
        pass

def view_command():
    try:
        #backend.view() returns a list of tuples
        list1.delete(0,END)
        for row in backend.view():
            list1.insert(END, row)
    except:
        pass

def view_command_courses():
    try:
        #backend.view_courses() returns a list of tuples
        list2.delete(0,END)
        for row in backend.view_courses():
            list2.insert(END, row)
    except:
        pass

def search_command():
    list1.delete(0,END)
    try:
        for row in backend.search(samID_text.get(), firstName_text.get(), lastName_text.get(), email_text.get(), cv_text.get(), docYear_text.get(), docType_text.get(), mastYear_text.get(), mastType_text.get(), experience_text.get(), profType_text.get(), onlineCert_text.get()):
            list1.insert(END,row)
        return
    except:
        list1.insert(END,"Unable to perform search.")
        return

def search_doctoral():
    list1.delete(0,END)
    try:
        for row in (backend.getDoctoralOnly()):
            list1.insert(END,row)
    except:
        pass

def search_masters():
    list1.delete(0,END)
    try:
        for row in (backend.getMastersOnly()):
            list1.insert(END,row)
    except:
        pass

def search_command_courses():
    list2.delete(0,END)
    try:
        for row in backend.search_courses(semester_text.get(), year_text.get(), courseNum_text.get(), sectionNum_text.get(), instructID_text.get(), instructLastName_text.get(), instructMethod_text.get(), ideaScore_text.get()):
            list2.insert(END,row)
    except:
        pass

def add_command():
    if (samID_text.get() == ''):
        return
    elif ((samID_text.get() == '') and (firstName_text.get() == '') and (lastName_text.get() == '') and (email_text.get() =='') and (cv_text.get() =='') and (docYear_text.get() == '') and (docType_text.get() == '') and (mastYear_text.get() == '') and (mastType_text.get() == '') and (experience_text.get() == '') and (profType_text.get() == '') and (onlineCert_text.get() == '')):
        return
    else:
        try:
            backend.insert(samID_text.get(), firstName_text.get(), lastName_text.get(), email_text.get(), cv_text.get(), docYear_text.get(), docType_text.get(), mastYear_text.get(), mastType_text.get(), experience_text.get(), profType_text.get(), onlineCert_text.get())
            list1.insert(END, "The record below was successfully added:")
            list1.insert(END, "====================================================")
            list1.insert(END,(samID_text.get(), firstName_text.get(), lastName_text.get(), email_text.get(), cv_text.get(),
                       docYear_text.get(), docType_text.get(), mastYear_text.get(), mastType_text.get(), experience_text.get(), profType_text.get(), onlineCert_text.get()))  
        except:
            pass

def add_command_courses():
    # If statement to make sure that all of the primary key fields are filled in before insertion occurs.
    if ((semester_text.get() == '') or (year_text.get() == '') or (courseNum_text.get() == '') or (sectionNum_text.get() == '')):
        pass
    else:
        backend.insert_courses(semester_text.get(), year_text.get(), courseNum_text.get(), sectionNum_text.get(),
                               instructID_text.get(), instructLastName_text.get(), instructMethod_text.get(), ideaScore_text.get())
        list2.delete(0,END)
        list2.insert(END, "The record below was successfully added:")
        list2.insert(END, "====================================================")
        list2.insert(END,(semester_text.get(), year_text.get(), courseNum_text.get(), sectionNum_text.get(),
                        instructID_text.get(), instructLastName_text.get(), instructMethod_text.get(), ideaScore_text.get()))  


def delete_command():
    try:
        backend.delete(selected_tuple[0])
        list1.delete(0,END)
        list1.insert(END, "The record below was successfully deleted:")
        list1.insert(END, "====================================================")
        list1.insert(END,(samID_text.get(), firstName_text.get(), lastName_text.get(), email_text.get(), cv_text.get(),
                       docYear_text.get(), docType_text.get(), mastYear_text.get(), mastType_text.get(), experience_text.get(), profType_text.get(), onlineCert_text.get()))
    except:
        pass

def delete_command_courses():
    backend.delete_courses(selected_tuple2[0], selected_tuple2[1], selected_tuple2[2], selected_tuple2[3])
    list2.delete(0,END)
    list2.insert(END, "The record below was successfully deleted:")
    list2.insert(END, "====================================================")
    list2.insert(END,(semester_text.get(), year_text.get(), courseNum_text.get(), sectionNum_text.get(),
                        instructID_text.get(), instructLastName_text.get(), instructMethod_text.get(), ideaScore_text.get()))


def update_command():
    try:
        backend.update(samID_text.get(), firstName_text.get(), lastName_text.get(), email_text.get(), cv_text.get(),
                     docYear_text.get(), docType_text.get(), mastYear_text.get(), mastType_text.get(), experience_text.get(), profType_text.get(), onlineCert_text.get())
        list1.delete(0,END)
        list1.insert(END, "The record below was successfully updated:")
        list1.insert(END, "====================================================")
        list1.insert(END,(samID_text.get(), firstName_text.get(), lastName_text.get(), email_text.get(), cv_text.get(),
                       docYear_text.get(), docType_text.get(), mastYear_text.get(), mastType_text.get(), experience_text.get(), profType_text.get()))  
    except:
        pass

def update_command_courses():
    if ((semester_text.get() == '') or (year_text.get() == '') or (courseNum_text.get() == '') or (sectionNum_text.get() == '')):
        pass
    else:
        try:
            backend.update_courses(semester_text.get(), year_text.get(), courseNum_text.get(), sectionNum_text.get(),
                               instructID_text.get(), instructLastName_text.get(), instructMethod_text.get(), ideaScore_text.get())
        except:
            list2.delete(0,END)
            list2.insert(END, "Unable to perform update.")

def cv_command():
    try:
        cv = ".\\Assets\\CVs\\"
        cv += str(selected_tuple[4])
        os.startfile(cv)
    except:
        return

def clear_command():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    profType_text.set("")
    onlineCert_text.set("")
    list1.delete(0,END)

def clear_command_courses():
    #e1c.delete(0,END)
    semester_text.set("")
    e2c.delete(0,END)
    e3c.delete(0,END)
    e4c.delete(0,END)
    e5c.delete(0,END)
    e6c.delete(0,END)
    #e7c.delete(0,END)
    instructMethod_text.set("")
    e8c.delete(0,END)
    list2.delete(0,END)

#####################################################################################
##        Start of main application window containing all the widgets              ##
#####################################################################################
window=Tk()
window.wm_title("SHSU CRIJ Professor Credentialing Database Desktop App V1.6")

window.geometry("850x600")
window.minsize(850,600)

#icon = ".\\Assets\\Icons\\db_logo.ico"
#window.iconbitmap(icon)

# Make the menu at the top of the window.
menu.make_menu(window)


# Make the frames to logically separate the GUI.
frame_profs = LabelFrame(window, text="PROFESSORS", labelanchor='nw')
frame_courses = LabelFrame(window, text="COURSES", labelanchor='nw')
frame_profs.grid(row=0, column=0, sticky='nsew')
frame_courses.grid(row=1, column=0,sticky='nsew')
Grid.rowconfigure(window, 0, weight=1)
Grid.rowconfigure(window, 1, weight=1)
Grid.columnconfigure(window, 0, weight=1)

##########################################################################
# POPULATE THE PROFESSOR FRAME
##########################################################################
#makes the labels beside the text boxes for profs frame
l1 = Label(frame_profs,text="SamID")
l1.grid(row=0, column=0, sticky='nsew')

l2 = Label(frame_profs,text="First Name")
l2.grid(row=1, column=0, sticky='nsew')

l3 = Label(frame_profs,text="Last Name")
l3.grid(row=2, column=0, sticky='nsew')

l4 = Label(frame_profs,text="Email")
l4.grid(row=3, column=0, sticky='nsew')

l5 = Label(frame_profs,text="CV")
l5.grid(row=4, column=0, sticky='nsew')

l6 = Label(frame_profs,text="Doctorate Year")
l6.grid(row=5, column=0, sticky='nsew')

l7 = Label(frame_profs,text="Doctorate Type")
l7.grid(row=6, column=0, sticky='nsew')

l8 = Label(frame_profs,text="Master's Year")
l8.grid(row=7, column=0, sticky='nsew')

l9 = Label(frame_profs,text="Master's Type")
l9.grid(row=8, column=0, sticky='nsew')

l10 = Label(frame_profs,text="Experience")
l10.grid(row=9, column=0, sticky='nsew')

lab11 = Label(frame_profs, text="Prof Type")
lab11.grid(row=10, column=0, sticky='nsew')
profTypeTip = Hovertip(lab11, "1=Full Time, 2=Doctoral Teaching, 3=Overload, 4=Lecturer/Adjunct", hover_delay=0)

lab12 = Label(frame_profs, text="Online Cert")
lab12.grid(row=11, column=0, sticky='nsew')
onlineCertTip = Hovertip(lab12, "0=No, 1=Yes", hover_delay=0)

#makes the entry text boxes to accept user input for profs frame
samID_text = StringVar()
e1 = Entry(frame_profs, textvariable = samID_text, width=34)
e1.grid(row=0, column=1, sticky='nsew')

firstName_text = StringVar()
e2 = Entry(frame_profs, textvariable = firstName_text, width=34)
e2.grid(row=1, column=1, sticky='nsew')

lastName_text = StringVar()
e3 = Entry(frame_profs, textvariable = lastName_text, width=34)
e3.grid(row=2, column=1, sticky='nsew')

email_text = StringVar()
e4 = Entry(frame_profs, textvariable = email_text, width=34)
e4.grid(row=3, column=1, sticky='nsew')

cv_text = StringVar()
e5 = Entry(frame_profs, textvariable = cv_text, width=34)
e5.grid(row=4, column=1, sticky='nsew')

docYear_text = StringVar()
e6 = Entry(frame_profs, textvariable = docYear_text, width=34)
e6.grid(row=5, column=1, sticky='nsew')

docType_text = StringVar()
e7 = Entry(frame_profs, textvariable = docType_text, width=34)
e7.grid(row=6, column=1, sticky='nsew')

mastYear_text = StringVar()
e8 = Entry(frame_profs, textvariable = mastYear_text, width=34)
e8.grid(row=7, column=1, sticky='nsew')

mastType_text = StringVar()
e9 = Entry(frame_profs, textvariable = mastType_text, width=34)
e9.grid(row=8, column=1, sticky='nsew')

experience_text = StringVar()
e10 = Entry(frame_profs, textvariable = experience_text, width=34)
e10.grid(row=9, column=1, sticky='nsew')

profType_text = StringVar()
profType_options=[1, 2, 3, 4, ""]
profType_text.set("")
profTypeDropMenu = OptionMenu(frame_profs, profType_text, *profType_options)
profTypeDropMenu.grid(row=10, column=1, sticky='nsew')
profTypeDropMenu.configure(activebackground='white')
profTypeTip2 = Hovertip(profTypeDropMenu, "(1=Full Time, 2=Doctoral Teaching, 3=Overload, 4=Lecturer/Adjunct)", hover_delay=0)

onlineCert_text = StringVar()
onlineCert_options=[0, 1, ""]
onlineCert_text.set("")
onlineCertDropMenu = OptionMenu(frame_profs, onlineCert_text, *onlineCert_options)
onlineCertDropMenu.grid(row=11, column=1, sticky='nsew')
onlineCertDropMenu.configure(activebackground='white')
onlineCertTip2 = Hovertip(onlineCertDropMenu, "(0=No, 1=Yes)", hover_delay=0)

#makes the list box to hold all of the records for profs frame
#need to add the scroll bar to the list box as well
list1 = Listbox(frame_profs, height=20, width=70)
list1.grid(row=1, column=3, rowspan=10, columnspan=2, sticky='nsew')

scrollbar1 = Scrollbar(frame_profs, orient='vertical')
scrollbar1.grid(row=1, column=5, rowspan = 10, sticky='nsew')

scrollbarHoriz1 = Scrollbar(frame_profs, orient='horizontal')
scrollbarHoriz1.grid(row=11, column=3, columnspan=2, sticky='nsew')

list1.configure(yscrollcommand=scrollbar1.set, xscrollcommand=scrollbarHoriz1.set)
scrollbar1.configure(command=list1.yview)
scrollbarHoriz1.configure(command=list1.xview)

list1.bind('<<ListboxSelect>>', get_selected_row)


#make the buttons for profs frame
#note that button commands do not need "()" at the end. it is part of tkinter
b1 = Button(frame_profs, text='View All', width=12, command=view_command)
b1.grid(row=0, column=2, sticky='nsew')

b2 = Button(frame_profs, text='Search', width=12, command=search_command)
b2.grid(row=2, column=2, sticky='nsew')

b3 = Button(frame_profs, text='Add', width=12, command=add_command)
b3.grid(row=3, column=2, sticky='nsew')

b4 = Button(frame_profs, text='Update', width=12, command=update_command)
b4.grid(row=4, column=2, sticky='nsew')

b5 = Button(frame_profs, text='Delete', width=12, command=delete_command)
b5.grid(row=5, column=2, sticky='nsew')
'''
b6 = Button(frame_profs, text='Exit', width=12, command=window.destroy)
b6.grid(row=8, column=2)
'''
b7 = Button(frame_profs, text='Open CV', width=12, command=cv_command)
b7.grid(row=6, column=2, rowspan=2, sticky='nsew')

b8 = Button(frame_profs, text='Clear Fields', width=12, command=clear_command)
b8.grid(row=1, column=2, sticky='nsew')

b9 = Button(frame_profs, text='\nGenerate\nProfessor\nReport\n', width=12, command=report_command)
b9.grid(row=8, column=2, rowspan=3, sticky='nsew')

b10 = Button(frame_profs, text='Show Only Doctoral Degree Holders', width=29, command=search_doctoral)
b10.grid(row=0, column=3, sticky='nsew')

b11 = Button(frame_profs, text='Show Only Master\'s Degree Holders', width=29, command=search_masters)
b11.grid(row=0, column=4, sticky='nsew')


#########################################################################
# POPULATE THE COURSES FRAME
#########################################################################

#makes the labels beside the text boxes
l1c = Label(frame_courses,text="Semester")
l1c.grid(row=0, column=0, sticky='nsew')

l2c = Label(frame_courses,text="Year")
l2c.grid(row=1, column=0, sticky='nsew')
year_tip = Hovertip(l2c, "Must be 4 digits (ex. 2014)", hover_delay=0)

l3c = Label(frame_courses,text="Course Number")
l3c.grid(row=2, column=0, sticky='nsew')
course_tip = Hovertip(l3c, "Must be 4 digits (ex. 2362)", hover_delay=0)

l4c = Label(frame_courses,text="Section Number")
l4c.grid(row=3, column=0, sticky='nsew')
section_tip = Hovertip(l4c, "Must be 1-2 digits (ex. 7, 07, 12)", hover_delay=0)

l5c = Label(frame_courses,text="Instructor's SamID")
l5c.grid(row=4, column=0, sticky='nsew')

l6c = Label(frame_courses,text="Instructor's Last Name")
l6c.grid(row=5, column=0, sticky='nsew')
instructor_tip = Hovertip(l6c, "First letter must be capitalized.", hover_delay=0)

l7c = Label(frame_courses,text="Instruction Method")
l7c.grid(row=6, column=0, sticky='nsew')
instructMethod_tip = Hovertip(l7c, "1=F2F, 2=Online, 3=Remote", hover_delay=0)
#l8c = Label(frame_courses,text="(1=F2F, 2=Online, 3=Remote)")
#l8c.grid(row=7, column=0, sticky='nsew')

l9c = Label(frame_courses,text="IDEA Score")
l9c.grid(row=7, column=0, sticky='nsew')


#makes the entry text boxes to accept user input
semester_text = StringVar()
sem_options = ["Spring", "Summer", "Fall", ""]
semester_text.set("")
semDropMenu = OptionMenu(frame_courses, semester_text, *sem_options)
semDropMenu.grid(row=0, column=1, sticky='nsew')
semDropMenu.configure(activebackground='white')
#e1c = Entry(frame_courses, textvariable = semester_text)
#e1c.grid(row=0, column=1)

year_text = StringVar()
e2c = Entry(frame_courses, textvariable = year_text)
e2c.grid(row=1, column=1, sticky='nsew')

courseNum_text = StringVar()
e3c = Entry(frame_courses, textvariable = courseNum_text)
e3c.grid(row=2, column=1, sticky='nsew')

sectionNum_text = StringVar()
e4c = Entry(frame_courses, textvariable = sectionNum_text)
e4c.grid(row=3, column=1, sticky='nsew')

instructID_text = StringVar()
e5c = Entry(frame_courses, textvariable = instructID_text)
e5c.grid(row=4, column=1, sticky='nsew')

instructLastName_text = StringVar()
e6c = Entry(frame_courses, textvariable = instructLastName_text)
e6c.grid(row=5, column=1, sticky='nsew')

instructMethod_text = StringVar()
instruct_options=[1, 2, 3, ""]
instructMethod_text.set("")
instructDropMenu = OptionMenu(frame_courses, instructMethod_text, *instruct_options)
instructDropMenu.grid(row=6, column=1, sticky='nsew')
instructDropMenu.configure(activebackground='white')
instructMethod_tip2 = Hovertip(instructDropMenu, "1=F2F, 2=Online, 3=Remote", hover_delay=0)
#e7c = Entry(frame_courses, textvariable = instructMethod_text)
#e7c.grid(row=6, column=1)

ideaScore_text = StringVar()
e8c = Entry(frame_courses, textvariable = ideaScore_text)
e8c.grid(row=7, column=1, sticky='nsew')



#makes the list box to hold all of the records
#need to add the scroll bar to the list box as well
list2 = Listbox(frame_courses, height=15, width=70)
list2.grid(row=0, column=3, rowspan=8, columnspan=1, sticky='nsew')

scrollbar2 = Scrollbar(frame_courses, orient='vertical')
scrollbar2.grid(row=0, column=4, rowspan = 8, sticky='nsew')

list2.configure(yscrollcommand=scrollbar2.set)
scrollbar2.configure(command=list2.yview)

list2.bind('<<ListboxSelect>>', get_selected_row_courses)


#make the buttons on the right side
#note that button commands do not need "()" at the end. it is part of tkinter
b1c = Button(frame_courses, text='View All', width=12, command=view_command_courses)
b1c.grid(row=0, column=2, sticky='nsew')

b2c = Button(frame_courses, text='Search', width=12, command=search_command_courses)
b2c.grid(row=2, column=2, sticky='nsew')

b3c = Button(frame_courses, text='Add', width=12, command=add_command_courses)
b3c.grid(row=3, column=2, sticky='nsew')
b3c.configure(activebackground='white')


b4c = Button(frame_courses, text='Update', width=12, command=update_command_courses)
b4c.grid(row=4, column=2, sticky='nsew')


b5c = Button(frame_courses, text='Delete', width=12, command=delete_command_courses)
b5c.grid(row=5, column=2, sticky='nsew')

'''
b6c = Button(frame_courses, text='Exit', width=12, command=window.destroy)
b6c.grid(row=6, column=2)
'''

b7c = Button(frame_courses, text='Clear Fields', width=12, command=clear_command_courses)
b7c.grid(row=1, column=2, sticky='nsew')

b8c = Button(frame_courses, text='Generate\nCourse Report', width=12,
             command=report_command_courses)
b8c.grid(row=6, column=2, rowspan=2, sticky='nsew')
reportCourse_tip = Hovertip(b8c, "Requires:Semester,Year,Course", hover_delay=0)

################################################################
##             CONFIGURE GRID TO BE RESIZABLE                 ##
################################################################
for i in range(0, 11):
    Grid.rowconfigure(frame_profs, i, weight=2)
for i in range(1,5):
    Grid.columnconfigure(frame_profs, i, weight=2)

for i in range(8):
    Grid.rowconfigure(frame_courses, i, weight=1)
for i in range(1,4):
    Grid.columnconfigure(frame_courses, i, weight=1)

#end of main window that wraps all of the widgets
window.mainloop()
#################################################################