import Tkinter, tkFileDialog

class EL737(Tkinter.LabelFrame):
    def __init__(self,parent,name):
        Tkinter.LabelFrame.__init__(self,parent,text=name)
        self.parent = parent

        self.hostname = Tkinter.StringVar()
        self.portname = Tkinter.StringVar()
        self.cmd = Tkinter.StringVar()
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
        entry = Tkinter.Entry(f,textvariable=self.cmd)
        submit = Tkinter.Button(f,text=u"Submit",
                                    command=self.OnButtonClick,relief="groove")
        entry.bind("<Return>",(lambda event: self.OnButtonClick()))
        lb.grid(column=0,row=0)
        entry.grid(column=1,row=0)
        submit.grid(column=0,row=1,columnspan=2)
        f.grid(column=0,row=1,columnspan=2)

    def line3(self):
        f = Tkinter.Frame(self)


        f.grid(column=0,row=2,columnspan=2)

    def OnButtonClick(self):
        self.echobox.insert(Tkinter.END,self.cmd.get())

