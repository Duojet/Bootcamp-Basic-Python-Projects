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

import page123drill_gui
import page123drill_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self,master, *args, **kwargs)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(1000,250))
        page123drill_func.center_window(self,1000,250)
        self.master.title("Folder Selector")

        page123drill_gui.load_gui(self)
        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()             
