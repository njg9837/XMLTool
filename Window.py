import Tkinter
import os
from Tkinter import *
import tkFileDialog
from tkFileDialog import *

class MainGui():
    def __init__(self,master):
        self.master = master

        master.geometry("650x120+250+100")
        master.title('XML Comparison Tool')
'''
        self.file1_st = StringVar()
        self.file_path1 = Entry(master, textvariable=self.file_path1)
        self.file2_st = StringVar()
        self.file_path2 = Entry(master, textvariable=self.file_path2)

        self.bb1 = Button(master, Text='Browse', command=askopenfilename())
        self.bb2 = Button(master, Text='Browse', command=askopenfilename())
        self.sb = Button(master, Text='Start', command='')

        self.t_frame = Frame(self.master, bg="gray61")
        self.t_frame.place(x=5, y=240, height=250, width=100)
        self.t_text = Text(self.t_frame)
        self.t_text.pack(expand=True, fill='both')


    def insert_text(self,rv):
        self.t_text.insert('end',rv)

    def browse_button(self):
        askopenfilename()
'''



def main():
    root = Tk()
   # app = MainGui(root)
    root.mainloop()