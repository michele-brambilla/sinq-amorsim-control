#!/bin/python

import Tkinter, tkFileDialog


class ESSFileWriter(Tkinter.LabelFrame):
    def __init__(self,parent,name):
        Tkinter.LabelFrame.__init__(self,parent,text=name)
        self.parent = parent
        self.cmd = Tkinter.StringVar()
        self.src = Tkinter.StringVar()
        self.text = ""
        self.initialize()
        self.grid()
        
    def initialize(self):
        self.grid()
        f1 = Tkinter.Frame(self)
        f2 = Tkinter.Frame(self)
        f3 = Tkinter.Frame(self)
        
        self.cmd.set("//[host]:[port]/[topic]")
        self.line1(f1)
        self.line2(f2)
        self.line3(f3)
        
        
        f1.grid(column=0,row=0,columnspan=3)
        f2.grid(column=0,row=1,columnspan=3)
        f3.grid(column=0,row=2,columnspan=3)

    def line1(self,parent):
        lbl = "kafka-to-nexus command-broker: "
        entry1 = Tkinter.Entry(parent,textvariable=self.cmd,width=40)
        lb = Tkinter.Label(parent,text=lbl)
        lb.grid(column=0,row=0,columnspan=2)
        entry1.grid(column=2,row=0,columnspan=2)
        
    def line3(self,parent):
        button_sub = Tkinter.Button(parent,text=u"Submit",
                                command=self.OnButtonClick)
        button_stop = Tkinter.Button(parent,text=u"Stop",
                                command=self.OnButtonClick)
        button_sub.grid(column=0,row=0)
        button_stop.grid(column=1,row=0)

    def line2(self,parent):
        lbl = "command file: "
        lb = Tkinter.Label(parent,text=lbl)

        self.src.set("")
        self.sr = Tkinter.Label(parent,textvariable=self.src)

        button = Tkinter.Button(parent,text=u"Open",
                                    command=self.OnButtonClickOpenfile)
        
        lb.grid(column=0,row=0)
        self.sr.grid(column=1,row=0)
        button.grid(column=2,row=0)        
        
    def OnButtonClick(self):
        pass

    def OnButtonClickOpenfile(self):
        ftypes = [('JSON files', '*.json'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        self.src.set(fl)
        print fl
        self.sr.update()
        f = open(fl, "r")
        self.text = f.read()



