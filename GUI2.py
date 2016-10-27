import os
from tkFileDialog import *
import XML4
from Tkinter import *

content1 = ''
content2 = ''
file_path1 = ''
file_path2 = ''

#~~~~ FUNCTIONS~~~~

def open_file1():
    global content1
    global file_path1

    filename1 = askopenfilename()
    #infile1 = open(filename1, 'r')
    #content1 = infile1.read()
    file_path1 = os.path._getfullpathname(filename1)
    entry1.delete(0, END)
    entry1.insert(0, file_path1)
    return content1

def process_file1(content1):
    print content1

def open_file2():
    global content2
    global file_path2

    filename2 = askopenfilename()
    #infile2 = open(filename2, 'r')
    #content2 = infile2.read()
    file_path2 = os.path._getfullpathname(filename2)
    entry2.delete(0, END)
    entry2.insert(0, file_path2)
    return content2

def process_file2(content2):
    print content2

#~~~~~~ GUI ~~~~~~~~

root = Tk()
root.title('XML Compare Tool')
root.geometry("650x120+250+100")

main = Frame(root)
main.pack()


f1 = Frame(main, width=600, height=250)
f1.pack()
f2 = Frame(main, width=600, height=250)
f2.pack()
f3 = Frame(main, width=600, height=250)
f3.pack()


Label(f1,text="Select File").grid(row=0, column=0, sticky='e')
entry1 = Entry(f1, width=75, textvariable=file_path1)
entry1.grid(row=0,column=1,padx=2,pady=2,columnspan=7)
Button(f1, text="Browse", command=open_file1).grid(row=0, column=8, sticky='ew', padx=5, pady=2)

Label(f2,text="Select File").grid(row=1, column=0, sticky='e')
entry2 = Entry(f2, width=75, textvariable=file_path2)
entry2.grid(row=1,column=1,padx=2,pady=2,columnspan=7)
Button(f2, text="Browse", command=open_file2).grid(row=1, column=8, sticky='ew', padx=5, pady=2)

Button(f3, text="compare", width=25, command=os.system('XML4.py')).grid(sticky='ew', padx=10, pady=10)


root.mainloop()
