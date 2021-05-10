import tkinter as tk
# filedialog to allow the user to select files
from tkinter import filedialog
# os used to modify paths and directories
import os
# shutil used to copy files
import shutil


class ImportCV:
    def __init__ (self):
        self.source = ""
        self.destination = os.path.abspath(r"./Assets/CVs")

    def get_file(self):
        # Prompt the user with filedialog.
        myFilename = filedialog.askopenfilename(initialdir='/', title="Select a Curriculum Vitae PDF to import.",
                                               filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")))
        self.source = myFilename
        # Copy the template file.
        shutil.copy2(self.source, self.destination)