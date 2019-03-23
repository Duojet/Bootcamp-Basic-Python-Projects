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

        self.btn_add = tk.Button(self.master,width=13,height=1,text="Browse...")
        self.btn_add.grid(row=2,column=0,padx=(25,0),pady=(75,5))

        self.btn_add = tk.Button(self.master,width=13,height=1,text="Browse...")
        self.btn_add.grid(row=3,column=0,padx=(25,0),pady=(0,15))

        self.btn_add = tk.Button(self.master,width=13,height=2,text="Check for files...")
        self.btn_add.grid(row=4,column=0,padx=(25,0),pady=(0,10))

        self.btn_add = tk.Button(self.master,width=13,height=2,text="Close Program")
        self.btn_add.grid(row=4,column=3,padx=(350,0),pady=(0,10))
        
# build Entry form objects - call widget/ text boxes
        self.txt_browse1 = tk.Entry(self.master,text="")
        self.txt_browse1.grid(row=2, column=1, columnspan=3, rowspan=1, padx=(25,0),pady=(75,5))
        
        self.txt_browse2 = tk.Entry(self.master,text="")
        self.txt_browse2.grid(row=3, column=1, columnspan=3, rowspan=1, padx=(25,0),pady=(0,0))













if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()             
