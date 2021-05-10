import tkinter as tk
from tkinter import filedialog
# os used to modify paths and directories
import os
# shutil used to copy files
import shutil


class GetCourseTemplate:
    def __init__ (self):
        self.source = os.path.abspath(r"./Assets/Templates/courseImport_TEMPLATE.xlsx")
        self.destination = ''

    def get_destination(self):
        # Prompt the user with filedialog.
        myPath = filedialog.askdirectory(initialdir='/', title="Select a directory to save template to:",
                                               mustexist=tk.TRUE)
        self.destination = myPath
        # Copy the template file.
        shutil.copy2(self.source, self.destination)


class GetProfTemplate:
    def __init__ (self):
        self.source = os.path.abspath(r"./Assets/Templates/profImport_TEMPLATE.xlsx")
        self.destination = ''

    def get_destination(self):
        # Prompt the user with filedialog.
        myPath = filedialog.askdirectory(initialdir='/', title="Select a directory to save template to:",
                                               mustexist=tk.TRUE)
        self.destination = myPath
        # Copy the template file.
        shutil.copy2(self.source, self.destination)