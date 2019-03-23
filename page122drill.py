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
        self.btn_add = tk.Button(self.master,width=14,height=1,text="Browse...", font=("sans-serif", "12"))
        self.btn_add.grid(row=1,column=0,padx=(25,25),pady=(75,10))

        self.btn_add = tk.Button(self.master,width=14,height=1,text="Browse...", font=("sans-serif", "12"))
        self.btn_add.grid(row=2,column=0,padx=(25,25),pady=(15,10))

        self.btn_add = tk.Button(self.master,width=14,height=2,text="Check for files...", font=("sans-serif", "12"))
        self.btn_add.grid(row=3,column=0,padx=(25,25),pady=(15,5))

        self.btn_add = tk.Button(self.master,width=14,height=2,text="Close Program", font=("sans-serif", "12"))
        self.btn_add.grid(row=3,column=3,padx=(335,0),pady=(15,5))
        
# build Entry form objects - call widget/ text boxes
        self.txt_browse1 = tk.Entry(self.master,width=43,text="", font=("sans-serif","14"))
        self.txt_browse1.grid(row=1, column=1, columnspan=3, padx=(15,0),pady=(75,0))
        
        self.txt_browse2 = tk.Entry(self.master,width=43,text="", font=("sans-serif","14"))
        self.txt_browse2.grid(row=2, column=1, columnspan=3, padx=(15,0),pady=(15,0))


        














if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()             
