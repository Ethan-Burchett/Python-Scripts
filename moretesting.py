import subprocess


from posixpath import split
import tkinter as tk
from tkinter import simpledialog, filedialog
from tkinter.constants import TRUE

from docx import Document

from docx.shared import Inches  

import os

import sys

from docxfunctions import *

#from win32com import client

import re
import os
import sys
import win32com.client as win32
from win32com.client import constants



root = tk.Tk()

root.withdraw() 

my_filetypes = [('all files', '.*'), ("Text Files", "*.txt;" "*.doc;" "*.docx")]

#[("Text Files", "*.txt;" "*.doc;" "*.docx")]


file_path = filedialog.askopenfile(parent=root,initialdir=os.getcwd(),title="Please select a file:", filetypes=my_filetypes)  # returns fancy object that has the path as the name. 

print(type(file_path))
#w = client.Dispatch('Word.Application')

print(type(file_path.name))

path = file_path.name
print(path)

path = path.replace("/","\\")
print(path)


#doc = w.Documents.Open(path)


#doc.SaveAs("E:\\Jupyter\\sa.docx",16)# Must have parameter 16, otherwise an error will occur

#w = wc.Dispatch('Word.Application')

#save_as_docx(file_path.name)

#path = r'C:\Users\EBurchett\Automation\PythonDocx\M21560 1296 E Hoffman Sewer Tie-In - Report #2.doc'
#path = file_path.name

#path = os.path.join(fr"{file_path.name}")





# Opening MS Word
word = win32.gencache.EnsureDispatch('Word.Application')
doc = word.Documents.Open(path)
doc.Activate ()

    # Rename path with .docx
new_file_abs = os.path.abspath(path)
new_file_abs = re.sub(r'\.\w+$', '.docx', new_file_abs)

    # Save and Close
word.ActiveDocument.SaveAs(new_file_abs, FileFormat=constants.wdFormatXMLDocument)
doc.Close(False)








#if file_path.name.endswith('.doc'):
 #   print(".doc")
  #  subprocess.call(['soffice', '--headless', '--convert-to', 'docx', r"C:\Users\EBurchett\Automation\PythonDocx\M21560 1296 E Hoffman Sewer Tie-In - Report #2.doc"])