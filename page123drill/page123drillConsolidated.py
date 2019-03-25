##Python Ver:     3.6.6
##
##Author:         Jordan Richter
##
##Purpose:        write a script that creates a GUI with a button widget and a
##                text widget. Your script will also include a function that when it is
##                called will invoke a dialog modal which will allow users the
##                ability to select a folder directory from their system.
##                Finally, your script will show the user’s selected
##                directory path into the text field.
##
##Tested OS:      This code was written and tested on Windows 10.


from tkinter import *
import tkinter as tk
import tkinter.filedialog as tkFileDialog




class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self,master, *args, **kwargs)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(1000,250))

        self.master.title("Path Revealer")

    
        self.btnBrowse = tk.Button(self.master,width=14,height=1,text="Find Directory Path", command = searchDir)
        self.btnBrowse.grid(row=1,column=0, padx=(25,25),pady=(45,25))

        self.txtBrowse = tk.Entry(self.master, textvariable = btnSearch, width=70, font=("sans-serif","14"))
        self.txtBrowse.grid(row=2, column=1,padx=(0,0),pady=(25,25))

    def searchDir(self):
        btnSearch = tkFileDialog.askdirectory()
        return(btnSearch)



        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()             
