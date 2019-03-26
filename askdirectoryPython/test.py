from tkinter import *
import tkinter as tk
import tkinter.filedialog as tkFileDialog

 
def searchDir():
    btnSearch = tkFileDialog.askdirectory()
    print(btnSearch)

searchDir()

