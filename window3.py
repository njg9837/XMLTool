import Tkinter
import tkFileDialog
from Tkinter import *
from tkFileDialog import *

class GUI:
    def __init__(self, master):
        self.master = master

        master.title("XML Compare Tool")
        master.geometry('700x300')

        path1 = StringVar()
        path2 = StringVar()
        self.bb1 = Button(master, text="Browse", command= lambda : self.callback())
        self.bb1.grid(row=0, column=0, padx=5, pady=5)


        self.bb2 = Button(master, text="Browse", command=lambda: path2.set(askopenfilename()))
        self.bb2.grid(row=1, column=0, padx=5, pady=5)

        self.confirm = Button(master, text="Confirm", command=self.on_button)
        self.confirm.grid(row=3, column=1, padx=5, pady=5, sticky='')

        self.entry1 = Entry(master, width=75, textvariable=self.display_path)
        self.entry1.grid(row=0, column=1, columnspan=2, sticky=W)
        print (self.entry1.get())

        self.entry2 = Entry(master, width=75, textvariable=path2)
        self.entry2.grid(row=1, column=1, sticky=W)

        self.t_label = Label(master, text="Script Output")
        self.t_label.grid(row=4, column=1, columnspan=1, sticky='')

        self.t_frame = Frame(master, bg="white", height=150, width=600)
        self.t_frame.grid(row=5, column=1, columnspan=1, sticky='')
        self.t_text = Text(self.t_frame)

    def callback(self):
        get_path = StringVar()
        get_path.set(askopenfilename())
        get_path.get()
        return get_path

    def display_path(self):
        path = self.callback()
        print path

    def on_button(self):
        path1 = self.entry1.get()
        path2 = self.entry2.get()
        print path1
        print path2


root = Tk()
my_gui = GUI(root)
root.mainloop()

