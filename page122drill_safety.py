##Python Ver:     3.6.6
##
##Author:         Jordan Richter
##
##Purpose:        Create GUI
##
##Tested OS:      This code was written and tested on Windows 10.


from tkinter import *
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,250))
        self.master.title("Check Files")

        
# build buttons
        self.btn_add = tk.Button(self.master,width=13,height=1,text="Browse...", font=("sans-serif", "13", "bold"))
        self.btn_add.grid(row=2,column=0,padx=(25,0),pady=(75,15))

        self.btn_add = tk.Button(self.master,width=13,height=1,text="Browse...", font=("sans-serif","13", "bold"))
        self.btn_add.grid(row=3,column=0,padx=(25,0),pady=(0,15))

        self.btn_add = tk.Button(self.master,width=13,height=2,text="Check for files...", font=("sans-serif","13", "bold"))
        self.btn_add.grid(row=4,column=0,padx=(25,0),pady=(0,10))

        self.btn_add = tk.Button(self.master,width=13,height=2,text="Close Program", font=("sans-serif","13", "bold"))
        self.btn_add.grid(row=4,column=3,padx=(370,10),pady=(0,10))
        
 #build Entry form objects - call widget/ text boxes
        self.btn_browse1 = tk.Entry(self.master,text="", font=("sans-serif","13", "bold"))
        self.btn_browse1.grid(row=2, column=1, columnspan=3, padx=(0,10),pady=(75,15))
        
        self.btn_browse2 = tk.Entry(self.master,text="", font=("sans-serif","13", "bold"))
        self.btn_browse2.grid(row=3, column=1, columnspan=3, padx=(0,10),pady=(75,15))













if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()             
