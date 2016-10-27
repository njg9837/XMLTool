from sys import executable
from subprocess import *
import subprocess
import os
import time
from datetime import datetime
from Tkinter import *
import tkFileDialog
import ctypes
import csv

#parser.add_argument('-s') #Service Tag
#parser.add_argument('-b') #Board part number
#parser.add_argument('-c') #chassis serial number
#parser.add_argument('-p') #chassis part number
#parser.add_argument('-i') #IP Addrss
#parser.add_argument('-u') #UUT #


class Start_Gui:
    def __init__(self,master):
        self.master = master

        master.geometry('740x500+20+20')
        master.title("Dell Server 2nd Touch")
        Label(master, text="UUT #",width=8,  height=1, relief=RAISED,font=("Helvetica",12), bg = "gray").grid(row=0, column=0)
        Label(master, text="Service Tag",width=13, relief=RAISED,font=("Helvetica",12), bg = "gray").grid(row=0, column=2)
        Label(master, text="105 Part #",width=13, relief=RAISED,font=("Helvetica",12), bg = "gray").grid(row=0, column=4)
        Label(master, text="100 Serial #",width=13, relief=RAISED,font=("Helvetica",12), bg = "gray").grid(row=0, column=6)
        Label(master, text="100 Part #",width=13, relief=RAISED,font=("Helvetica",12), bg = "gray").grid(row=0, column=8)
        Label(master, text="UUT 8",width=8, relief=RAISED, font=("Helvetica",12), bg = "gray55").grid(row=1, column=0)
        Label(master, text="UUT 7",width=8, relief=RAISED, font=("Helvetica",12), bg = "gray60").grid(row=2, column=0)
        Label(master, text="UUT 6",width=8, relief=RAISED, font=("Helvetica",12), bg = "gray65").grid(row=3, column=0)
        Label(master, text="UUT 5",width=8, relief=RAISED, font=("Helvetica",12), bg = "gray70").grid(row=4, column=0)
        Label(master, text="UUT 4",width=8, relief=RAISED, font=("Helvetica",12), bg = "gray75").grid(row=5, column=0)
        Label(master, text="UUT 3",width=8, relief=RAISED, font=("Helvetica",12), bg = "gray80").grid(row=6, column=0)
        Label(master, text="UUT 2",width=8, relief=RAISED, font=("Helvetica",12), bg = "gray85").grid(row=7, column=0)
        Label(master, text="UUT 1",width=8, relief=RAISED, font=("Helvetica",12), bg = "gray90").grid(row=8, column=0)
        self.uut8_st = StringVar()
        self.e_uut8_st = Entry(master,textvariable=self.uut8_st)
        self.e_uut8_st.grid(row=1, column=2)
        self.uut8_pn105 = StringVar()
        self.e_uut8_pn105 = Entry(master,textvariable=self.uut8_pn105)
        self.e_uut8_pn105.grid(row=1, column=4)
        self.uut8_ps100 = StringVar()
        self.e_uut8_ps100 = Entry(master,textvariable=self.uut8_ps100)
        self.e_uut8_ps100.grid(row=1, column=6)
        self.uut8_pn100 = StringVar()
        self.e_uut8_pn100 = Entry(master,textvariable=self.uut8_pn100)
        self.e_uut8_pn100.grid(row=1, column=8)
        self.uut7_st = StringVar()
        self.e_uut7_st = Entry(master,textvariable=self.uut7_st)
        self.e_uut7_st.grid(row=2, column=2)
        self.uut7_pn105 = StringVar()
        self.e_uut7_pn105 = Entry(master,textvariable=self.uut7_pn105)
        self.e_uut7_pn105.grid(row=2, column=4)
        self.uut7_ps100 = StringVar()
        self.e_uut7_ps100 = Entry(master,textvariable=self.uut7_ps100)
        self.e_uut7_ps100.grid(row=2, column=6)
        self.uut7_pn100 = StringVar()
        self.e_uut7_pn100 = Entry(master,textvariable=self.uut7_pn100)
        self.e_uut7_pn100.grid(row=2, column=8)
        self.uut6_st = StringVar()
        self.e_uut6_st = Entry(master,textvariable=self.uut6_st)
        self.e_uut6_st.grid(row=3, column=2)
        self.uut6_pn105 = StringVar()
        self.e_uut6_pn105 = Entry(master,textvariable=self.uut6_pn105)
        self.e_uut6_pn105.grid(row=3, column=4)
        self.uut6_ps100 = StringVar()
        self.e_uut6_ps100 = Entry(master,textvariable=self.uut6_ps100)
        self.e_uut6_ps100.grid(row=3, column=6)
        self.uut6_pn100 = StringVar()
        self.e_uut6_pn100 = Entry(master,textvariable=self.uut6_pn100)
        self.e_uut6_pn100.grid(row=3, column=8)
        self.uut5_st = StringVar()
        self.e_uut5_st = Entry(master,textvariable=self.uut5_st)
        self.e_uut5_st.grid(row=4, column=2)
        self.uut5_pn105 = StringVar()
        self.e_uut5_pn105 = Entry(master,textvariable=self.uut5_pn105)
        self.e_uut5_pn105.grid(row=4, column=4)
        self.uut5_ps100 = StringVar()
        self.e_uut5_ps100 = Entry(master,textvariable=self.uut5_ps100)
        self.e_uut5_ps100.grid(row=4, column=6)
        self.uut5_pn100 = StringVar()
        self.e_uut5_pn100 = Entry(master,textvariable=self.uut5_pn100)
        self.e_uut5_pn100.grid(row=4, column=8)
        self.uut4_st = StringVar()
        self.e_uut4_st = Entry(master,textvariable=self.uut4_st)
        self.e_uut4_st.grid(row=5, column=2)
        self.uut4_pn105 = StringVar()
        self.e_uut4_pn105 = Entry(master,textvariable=self.uut4_pn105)
        self.e_uut4_pn105.grid(row=5, column=4)
        self.uut4_ps100 = StringVar()
        self.e_uut4_ps100 = Entry(master,textvariable=self.uut4_ps100)
        self.e_uut4_ps100.grid(row=5, column=6)
        self.uut4_pn100 = StringVar()
        self.e_uut4_pn100 = Entry(master,textvariable=self.uut4_pn100)
        self.e_uut4_pn100.grid(row=5, column=8)
        self.uut3_st = StringVar()
        self.e_uut3_st = Entry(master,textvariable=self.uut3_st)
        self.e_uut3_st.grid(row=6, column=2)
        self.uut3_pn105 = StringVar()
        self.e_uut3_pn105 = Entry(master,textvariable=self.uut3_pn105)
        self.e_uut3_pn105.grid(row=6, column=4)
        self.uut3_ps100 = StringVar()
        self.e_uut3_ps100 = Entry(master,textvariable=self.uut3_ps100)
        self.e_uut3_ps100.grid(row=6, column=6)
        self.uut3_pn100 = StringVar()
        self.e_uut3_pn100 = Entry(master,textvariable=self.uut3_pn100)
        self.e_uut3_pn100.grid(row=6, column=8)
        self.uut2_st = StringVar()
        self.e_uut2_st = Entry(master,textvariable=self.uut2_st)
        self.e_uut2_st.grid(row=7, column=2)
        self.uut2_pn105 = StringVar()
        self.e_uut2_pn105 = Entry(master,textvariable=self.uut2_pn105)
        self.e_uut2_pn105.grid(row=7, column=4)
        self.uut2_ps100 = StringVar()
        self.e_uut2_ps100 = Entry(master,textvariable=self.uut2_ps100)
        self.e_uut2_ps100.grid(row=7, column=6)
        self.uut2_pn100 = StringVar()
        self.e_uut2_pn100 = Entry(master,textvariable=self.uut2_pn100)
        self.e_uut2_pn100.grid(row=7, column=8)
        self.uut1_st = StringVar()
        self.e_uut1_st = Entry(master,textvariable=self.uut1_st)
        self.e_uut1_st.grid(row=8, column=2)
        self.uut1_pn105 = StringVar()
        self.e_uut1_pn105 = Entry(master,textvariable=self.uut1_pn105)
        self.e_uut1_pn105.grid(row=8, column=4)
        self.uut1_ps100 = StringVar()
        self.e_uut1_ps100 = Entry(master,textvariable=self.uut1_ps100)
        self.e_uut1_ps100.grid(row=8, column=6)
        self.uut1_pn100 = StringVar()
        self.e_uut1_pn100 = Entry(master,textvariable=self.uut1_pn100)
        self.e_uut1_pn100.grid(row=8, column=8)

        self.b8 = Button(master, text="START", bg="springgreen3", width = 10, command=self.cb8)
        self.b8.grid(row=1, column=20)
        self.b7 = Button(master, text="START", bg="springgreen3", width = 10, command=self.cb7)
        self.b7.grid(row=2, column=20)
        self.b6 = Button(master, text="START", bg="springgreen3", width = 10, command=self.cb6)
        self.b6.grid(row=3, column=20)
        self.b5 = Button(master, text="START", bg="springgreen3", width = 10, command=self.cb5)
        self.b5.grid(row=4, column=20)
        self.b4 = Button(master, text="START", bg="springgreen3", width = 10, command=self.cb4)
        self.b4.grid(row=5, column=20)
        self.b3 = Button(master, text="START", bg="springgreen3", width = 10, command=self.cb3)
        self.b3.grid(row=6, column=20)
        self.b2 = Button(master, text="START", bg="springgreen3", width = 10, command=self.cb2)
        self.b2.grid(row=7, column=20)
        self.b1 = Button(master, text="START", bg="springgreen3", width = 10, command=self.cb1)
        self.b1.grid(row=8, column=20)

        self.b8r = Button(master, text="Clear Entries", bg="turquoise1", width = 10, command=self.cb8r)
        self.b8r.grid(row=1, column=22)
        self.b7r = Button(master, text="Clear Entries", bg="turquoise1", width = 10, command=self.cb7r)
        self.b7r.grid(row=2, column=22)
        self.b6r = Button(master, text="Clear Entries", bg="turquoise1", width = 10, command=self.cb6r)
        self.b6r.grid(row=3, column=22)
        self.b5r = Button(master, text="Clear Entries", bg="turquoise1", width = 10, command=self.cb5r)
        self.b5r.grid(row=4, column=22)
        self.b4r = Button(master, text="Clear Entries", bg="turquoise1", width = 10, command=self.cb4r)
        self.b4r.grid(row=5, column=22)
        self.b3r = Button(master, text="Clear Entries", bg="turquoise1", width = 10, command=self.cb3r)
        self.b3r.grid(row=6, column=22)
        self.b2r = Button(master, text="Clear Entries", bg="turquoise1", width = 10, command=self.cb2r)
        self.b2r.grid(row=7, column=22)
        self.b1r = Button(master, text="Clear Entries", bg="turquoise1", width = 10, command=self.cb1r)
        self.b1r.grid(row=8, column=22)

        #def text_frame(self):
        self.t_frame = Frame(self.master, bg = "gray61")
        self.t_frame.place(x=5, y=240 ,height=250, width=730)
        self.t_text = Text(self.t_frame)
        self.t_text.pack(expand=True, fill='both')
    
    def insert_text(self,rv):
        self.t_text.insert('end',rv)       
    
    def cb8r(self):
        print self.cb8_return.poll()
        print "pid = ",self.cb8_return.pid
        pid = self.cb8_return.pid
        try:
            os.kill(pid,9)
        except:
            print "trying to kill process ", self.cb8_return.pid

        self.b8.configure(state = NORMAL, bg="springgreen3")
        self.e_uut8_st.delete(0, 'end')
        self.e_uut8_pn105.delete(0, 'end')
        self.e_uut8_ps100.delete(0, 'end')
        self.e_uut8_pn100.delete(0, 'end')

    def cb7r(self):
        print self.cb7_return.poll()
        print "pid = ",self.cb7_return.pid
        pid = self.cb7_return.pid
        try:
            os.kill(pid,9)
        except:
            print "trying to kill process ", self.cb7_return.pid

        self.b7.configure(state = NORMAL, bg="springgreen3")
        self.e_uut7_st.delete(0, 'end')
        self.e_uut7_pn105.delete(0, 'end')
        self.e_uut7_ps100.delete(0, 'end')
        self.e_uut7_pn100.delete(0, 'end')
            
    
    def cb6r(self):
        print self.cb6_return.poll()
        print "pid = ",self.cb6_return.pid
        pid = self.cb6_return.pid
        try:
            os.kill(pid,9)
        except:
            print "trying to kill process ", self.cb6_return.pid

        self.b6.configure(state = NORMAL, bg="springgreen3")
        self.e_uut6_st.delete(0, 'end')
        self.e_uut6_pn105.delete(0, 'end')
        self.e_uut6_ps100.delete(0, 'end')
        self.e_uut6_pn100.delete(0, 'end')
    
    def cb5r(self):
        print self.cb5_return.poll()
        print "pid = ",self.cb5_return.pid
        pid = self.cb5_return.pid
        try:
            os.kill(pid,9)
        except:
            print "trying to kill process ", self.cb5_return.pid

        self.b5.configure(state = NORMAL, bg="springgreen3")
        self.e_uut5_st.delete(0, 'end')
        self.e_uut5_pn105.delete(0, 'end')
        self.e_uut5_ps100.delete(0, 'end')
        self.e_uut5_pn100.delete(0, 'end')
    
    def cb4r(self):
        print self.cb4_return.poll()
        print "pid = ",self.cb4_return.pid
        pid = self.cb4_return.pid
        try:
            os.kill(pid,9)
        except:
            print "trying to kill process ", self.cb4_return.pid

        self.b4.configure(state = NORMAL, bg="springgreen3")
        self.e_uut4_st.delete(0, 'end')
        self.e_uut4_pn105.delete(0, 'end')
        self.e_uut4_ps100.delete(0, 'end')
        self.e_uut4_pn100.delete(0, 'end')
    
    def cb3r(self):
        print self.cb3_return.poll()
        print "pid = ",self.cb3_return.pid
        pid = self.cb3_return.pid
        try:
            os.kill(pid,9)
        except:
            print "trying to kill process ", self.cb3_return.pid

        self.b3.configure(state = NORMAL, bg="springgreen3")
        self.e_uut3_st.delete(0, 'end')
        self.e_uut3_pn105.delete(0, 'end')
        self.e_uut3_ps100.delete(0, 'end')
        self.e_uut3_pn100.delete(0, 'end')
    
    def cb2r(self):
        print self.cb2_return.poll()
        print "pid = ",self.cb2_return.pid
        pid = self.cb2_return.pid
        try:
            os.kill(pid,9)
        except:
            print "trying to kill process ", self.cb2_return.pid

        self.b2.configure(state = NORMAL, bg="springgreen3")
        self.e_uut2_st.delete(0, 'end')
        self.e_uut2_pn105.delete(0, 'end')
        self.e_uut2_ps100.delete(0, 'end')
        self.e_uut2_pn100.delete(0, 'end')
    
    def cb1r(self):
        print self.cb1_return.poll()
        print "pid = ",self.cb1_return.pid
        pid = self.cb1_return.pid
        try:
            os.kill(pid,9)
        except:
            print "trying to kill process ", self.cb1_return.pid

        self.b1.configure(state = NORMAL, bg="springgreen3")
        self.e_uut1_st.delete(0, 'end')
        self.e_uut1_pn105.delete(0, 'end')
        self.e_uut1_ps100.delete(0, 'end')
        self.e_uut1_pn100.delete(0, 'end')
    
    
    def cb8(self):
        st = self.uut8_st.get()
        pn105= self.uut8_pn105.get()
        ps100 = self.uut8_ps100.get()
        pn100 = self.uut8_pn100.get()
        uut = " -u UUT8"
        self.cb8_return = program_uut(self,st,pn105,ps100,pn100,uut)
        if self.cb8_return != None:
            self.b8.configure(state = DISABLED)        

    def cb7(self):
        st = self.uut7_st.get()
        pn105= self.uut7_pn105.get()
        ps100 = self.uut7_ps100.get()
        pn100 = self.uut7_pn100.get()
        uut = " -u UUT7"
        self.cb7_return = program_uut(self,st,pn105,ps100,pn100,uut)
        if self.cb7_return != None:
            self.b7.configure(state = DISABLED)        
    def cb6(self):
        st = self.uut6_st.get()
        pn105= self.uut6_pn105.get()
        ps100 = self.uut6_ps100.get()
        pn100 = self.uut6_pn100.get()
        uut = " -u UUT6"
        self.cb6_return = program_uut(self,st,pn105,ps100,pn100,uut)
        if self.cb6_return != None:
            self.b6.configure(state = DISABLED)        
    def cb5(self):
        st = self.uut5_st.get()
        pn105= self.uut5_pn105.get()
        ps100 = self.uut5_ps100.get()
        pn100 = self.uut5_pn100.get()
        uut = " -u UUT5"
        self.cb5_return = program_uut(self,st,pn105,ps100,pn100,uut)
        if self.cb5_return != None:
            self.b5.configure(state = DISABLED)        
    def cb4(self):
        st = self.uut4_st.get()
        pn105= self.uut4_pn105.get()
        ps100 = self.uut4_ps100.get()
        pn100 = self.uut4_pn100.get()
        uut = " -u UUT4"
        self.cb4_return = program_uut(self,st,pn105,ps100,pn100,uut)
        if self.cb4_return != None:
            self.b4.configure(state = DISABLED)        
    def cb3(self):
        st = self.uut3_st.get()
        pn105= self.uut3_pn105.get()
        ps100 = self.uut3_ps100.get()
        pn100 = self.uut3_pn100.get()
        uut = " -u UUT3"
        self.cb3_return = program_uut(self,st,pn105,ps100,pn100,uut)
        if self.cb3_return != None:
            self.b3.configure(state = DISABLED)        
    def cb2(self):
        st = self.uut2_st.get()
        pn105= self.uut2_pn105.get()
        ps100 = self.uut2_ps100.get()
        pn100 = self.uut2_pn100.get()
        uut = " -u UUT2"
        self.cb2_return = program_uut(self,st,pn105,ps100,pn100,uut)
        if self.cb2_return != None:
            self.b2.configure(state = DISABLED)        
    def cb1(self):
        st = self.uut1_st.get()
        pn105= self.uut1_pn105.get()
        ps100 = self.uut1_ps100.get()
        pn100 = self.uut1_pn100.get()
        uut = " -u UUT1"
        self.cb1_return = program_uut(self,st,pn105,ps100,pn100,uut)
        if self.cb1_return != None:
            self.b1.configure(state = DISABLED)        
    cb8_return = " " #clear var
    cb7_return = " " #clear var
    cb6_return = " " #clear var
    cb4_return = " " #clear var
    cb3_return = " " #clear var
    cb2_return = " " #clear var
    cb1_return = " " #clear var

    #netsh dhcp server scope 192.168.0.0 show clients 1

def program_uut(self,st,pn105,ps100,pn100,uut):
    print "-s "+st+" -b "+pn105+" -c "+ps100+" -p "+pn100
    st = st.replace(" ","")
    pn105 = pn105.replace(" ","")
    ps100 = ps100.replace(" ","")
    pn100 = pn100.replace(" ","")
    st = st.replace("\n","")
    pn105 = pn105.replace("\n","")
    ps100 = ps100.replace("\n","")
    pn100 = pn100.replace("\n","")
    st = st.replace("\t","")
    pn105 = pn105.replace("\t","")
    ps100 = ps100.replace("\t","")
    pn100 = pn100.replace("\t","")
    st = st.replace("\r","")
    pn105 = pn105.replace("\r","")
    ps100 = ps100.replace("\r","")
    pn100 = pn100.replace("\r","")
    if ps100 == "":
        ps100 ="na"
    if pn105 == "":
        pn105 = "na"
    if pn100 == "":
        pn100 = pn105
    pn100_s00 = pn100[0:11]+"-00"  #change suffix to 00
    print "pn100_suffix", pn100_s00
    file_name = "c:\\Scripts\\sku_part_numbers.csv"
    print "TIME STAMP:"+str(datetime.now())
    found_pn100 = "no"
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        #f = "check sku"
        #ff = Start_Gui(f)
        #ff.text_frame()
        for row in reader:
            if pn100_s00 in row:
                found_pn100 ="yes"
        
    
    if found_pn100 == "yes":
        ip_address = " " #clear var
        ip_found = "no"
        netsh = subprocess.check_output('netsh dhcp server scope 192.168.0.0 show clients 1', shell=True)
        #Start_Gui.insert_text(self,netsh)

        #self.t_text.insert('end',"\n\n")
        print netsh
        #self.t_text.insert('end',netsh)
        if st in netsh:
            netsh = netsh.split('\n')
            #print netsh

            for attempt in range(len(netsh)):
                if st in netsh[attempt]:
                    netf = netsh[attempt]
                    ip_address = netf[0:14]
                    ip_address = ip_address.replace(" ","")
                    ip_address = ip_address.replace("\n","")
                    ip_address = ip_address.replace("\r","")
                    ip_address = ip_address.replace("\u ","")
                    ip_address = ip_address.replace("\t","")
                    ip_found = "yes"
                    print "IP_address from NETSH = ", netf[0:14]
            ping = " " #clear var
            try:
                ping = subprocess.check_output('ping '+ip_address+' -w 3 -n 3', shell=True)
            except:
                no_ping =  "\nNo reply of from IP Address ",ip_address
                Start_Gui.insert_text(self,no_ping)

            if "Lost = 0 (0% loss)" in ping:
                cmd = "-s "+ st+" -b "+pn105+" -c "+ps100+" -p "+pn100+" -i "+ ip_address+uut
                cmd =  "c:\\Python27\\python.exe c:\\Scripts\\dell_server_gui_single.py " +cmd
                try:
                    runme = subprocess.Popen(cmd ,creationflags=CREATE_NEW_CONSOLE)
                    print "Executed \n",cmd
                    pid =  runme.pid
                    #print pid
                    return runme
                except subprocess.CalledProcessError, e:
                    fte =  " Failed to execute \n",cmd , e.output
                    Start_Gui.insert_text(self,ftw)
        else:
            no_st =  "\nService Tag not found when executing NETSH ", st
            Start_Gui.insert_text(self,no_st)                          
    else:
        no_btla = "\nBoard TLA (100/105) is not listed on the SKU table " ,pn100
        Start_Gui.insert_text(self,no_btla)

def main():
    root = Tk()
    app = Start_Gui(root)
    root.mainloop()

if __name__ == '__main__':
    main()
