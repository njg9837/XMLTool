#!python3

from tkinter import *

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("XML Comparison")

        self.label = Label(master, text="some text")
        self.label.pack()

        self.greet_button = Button(master, text="greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("hi")

root = Tk()
my_gui = GUI(root)
root.mainloop()