import Tkinter, tkFileDialog
import socket
import sys

class Connector:
    def __init__(self):
        
        self.connected = False
        
    def connect(self,host,port):
        
        if not self.connected:
            try:
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((host, port))
            except socket.error as msg:
                self.s.close()
                self.s = None
            if self.s is None:
                sys.stderr.write("ERROR: could not open socket\n")
                return
            self.connected = True

    def disconnect(self):
        if self.connected:
            self.s.close()
        
    def send(self,message):
        if self.connected:
            sent = self.s.send(message)
            if sent == 0:
                raise RuntimeError("socket connection broken")
#            return self.s.recv(1)
        else:
            raise RuntimeError("socket not connected")
        
class EL737(Tkinter.LabelFrame):
    
    def __init__(self,parent,name):
        self.mess = Connector()
        Tkinter.LabelFrame.__init__(self,parent,text=name)
        self.parent = parent
        self.hostname = Tkinter.StringVar()
        self.portname = Tkinter.StringVar()
        self.cmd = Tkinter.StringVar()
        self.entry = Tkinter.Entry
        self.initialize()
        self.grid()

    def initialize(self):
        self.hostname.set("localhost")
        self.portname.set("62000")
        self.cmd.set("")
        
        self.left()
        self.right()

    def left(self):
        self.line1()
        self.line2()
        self.line3()
        
    def right(self):
        f = Tkinter.Frame(self)
        lb = Tkinter.Label(f,text="echo")
        self.echobox = Tkinter.Listbox(f)
        
        lb.grid(row=0)
        self.echobox.grid(row=1)
        f.grid(column=10,row=0,rowspan=3)
        pass
    
    def line1(self):
        f = Tkinter.Frame(self)

        lb = Tkinter.Label(f,text="dest [host]:[port] ")
        host = Tkinter.Entry(f,textvariable=self.hostname,width=15)
        separator = Tkinter.Label(f,text=":")
        port = Tkinter.Entry(f,textvariable=self.portname,width=10)

        lb.grid(column=0,row=0)
        host.grid(column=1,row=0)
        separator.grid(column=2,row=0)
        port.grid(column=3,row=0)
        
        f.grid(column=0,row=0,columnspan=2)
        
    def line2(self):
        f = Tkinter.Frame(self)
        lbl = "command: "
        lb = Tkinter.Label(f,text=lbl)
        self.entry = Tkinter.Entry(f,textvariable=self.cmd)
        submit = Tkinter.Button(f,text=u"Submit",
                                    command=self.OnButtonClick,relief="groove")
        self.entry.bind("<Return>",(lambda event: self.OnButtonClick()))
        lb.grid(column=0,row=0)
        self.entry.grid(column=1,row=0)
        submit.grid(column=0,row=1,columnspan=2)
        f.grid(column=0,row=1,columnspan=2)

    def line3(self):
        f = Tkinter.Frame(self)


        f.grid(column=0,row=2,columnspan=2)

    def OnButtonClick(self):
        if self.mess.connected == False:
            self.mess.connect(self.hostname.get(),
                                  int(self.portname.get()))

        self.echobox.insert(Tkinter.END,
                                self.cmd.get())

        self.echobox.insert(Tkinter.END,
                                self.mess.send(self.cmd.get()+"\r"))
        self.entry.delete(0, 'end')
