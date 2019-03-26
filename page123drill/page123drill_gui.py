
from tkinter import *
import tkinter as tk

import page123drill_main
import page123drill_func

def load_gui(self):
    
    self.btnBrowse = tk.Button(self.master,width=14,height=1,text="Find Directory Path", command = self.searchDir)
    self.btnBrowse.grid(row=1,column=0, padx=(25,25),pady=(45,25))

    self.txtBrowse = tk.Entry(self.master, textvariable = btnSearch, width=70, font=("sans-serif","14"))
    self.txtBrowse.grid(row=2, column=1,padx=(0,0),pady=(25,25))

    page123drill_func.browseDirectory(self)
    
 


if __name__ == "__main__":
    pass           
