from Tkinter import *
import tkFileDialog
from tkFileDialog import *



class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        path1 = StringVar()
        path2 = StringVar()

        self.bttn1 = Button(self, text = "Browse", fg="blue", command=lambda:path1.set(tkFileDialog.askopenfilename()))
        self.bttn1.grid(row='0', column='0')

        self.bttn2 = Button(self)
        self.bttn2.grid(row='1',column='0')
        self.bttn2.configure(text = "Browse", fg="red", command=lambda:path2.set(tkFileDialog.askopenfilename()))

        self.bttn3 = Button(self)
        self.bttn3.grid(row='3', column='0')
        self.bttn3["text"] = "Apply"

        self.entry1 = Entry(self, textvariable=path1)
        self.entry1.grid(row='0', column='1', columnspan='5')
        #self.entry1.place(x='100', y='5', width='700')

        self.entry2 = Entry(self, textvariable=path2)
        self.entry2.grid(row='1', column='5')

    #def browsefile(self):
     #   from tkFileDialog import askopenfilename
      #  Tk().withdraw()
       # filename = askopenfilename()

root = Tk()
root.title("Use button")
root.geometry("800x100")
app = Application(root)
root.mainloop()