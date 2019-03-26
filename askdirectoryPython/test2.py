from tkinter import *
import tkinter as tk
import tkinter.filedialog as tkFileDialog

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self,master, *args, **kwargs)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(1000,250))
        self.master.title("File Selector")
        
        
        
    def searchDir():
        btnSearch = tkFileDialog.askdirectory()
        print(btnSearch)

    searchDir()

          
  


if __name__ == "__main__":
   
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop() 
