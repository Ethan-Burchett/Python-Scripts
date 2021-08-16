from glob import glob
import re
import os

import subprocess


from posixpath import split
import tkinter as tk
from tkinter import simpledialog, filedialog
from tkinter.constants import TRUE

from docx import Document

from docx.shared import Inches  

from docxfunctions import *

#from win32com import client

import sys
import win32com.client as win32
from win32com.client import constants
#import win32com.client as win32
#from win32com.client import constants



def find_report_number(report_str):

    number = 0
    for word in report_str.split():
        if word.isdigit():
            number = word
          #numbers.append(int(word))
    return number


def doc_to_docx(path):
    path = path.replace("/","\\")
    print(path)
    word = win32.gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(path)
    doc.Activate ()

    # Rename path with .docx
    new_file_abs = os.path.abspath(path)
    new_file_abs = re.sub(r'\.\w+$', '.docx', new_file_abs)

    # Save and Close
    word.ActiveDocument.SaveAs(new_file_abs, FileFormat=constants.wdFormatXMLDocument)
    doc.Close(False)



