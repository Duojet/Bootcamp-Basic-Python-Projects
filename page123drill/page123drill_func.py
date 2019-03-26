from tkinter import *
import tkinter as tk
import tkinter.filedialog as tkFileDialog

import page123drill_main
import page123drill_gui





def searchDir(self):
    btnSearch = tkFileDialog.askdirectory()
    print(btnSearch)
    self.txtBrowse.insert(END,btnSearch)



if __name__ == "__main__":
    pass

    
