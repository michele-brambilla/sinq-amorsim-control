#!/bin/python

import Tkinter, tkFileDialog
from kafka import KafkaProducer
import re

def cleanup(value):
    if value[0]=='/':
        return cleanup(value[1:])
    if value[len(value)-1]==':':
        return cleanup(value[:-1])
    return value


def parse(uri,regex,default):
    p=re.compile(regex)
    found=p.findall(uri)
    if len(found) == 0:
        return default
    else :
        if len(found) == 1:
            return cleanup(found[0])
        else:
            raise RuntimeError("command-broker parsing failure")

        
class Connector:
    def __init__(self):
        self.connected = False
        self.server = ""
        self.topic = ""

    def connect(self,uri):
        # protocol: ^[A-Za-z]*
        # broker:   \/{2}[A-Za-z.0-9]+:  (literal)
        # port:     :([0-9]+)
        # topic:    \/[A-Za-z._-]+$
        broker = parse(uri,r"\/{2}[A-Za-z.0-9]+:","ess01.psi.ch")
        port   = parse(uri,r":([0-9]+)","9092")

        if not self.connected:
            self.server = broker+":"+port
            self.topic  = parse(uri,r"\/[A-Za-z._-]+$","topic.default")
            self.producer = KafkaProducer(bootstrap_servers=self.server)
            self.connected = True
        
    def disconnect(self):
        if self.connected:
            self.producer.close()
            
    def send(self,message):
        if self.connected:
            self.producer.send(self.topic,value=message)
            self.producer.flush()
        else:
            raise RuntimeError("producer not connected")

    
        
class ESSFileWriter(Tkinter.LabelFrame):

    def __init__(self,parent,name):
        self.mess = Connector()
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
        entry = Tkinter.Entry(parent,textvariable=self.cmd,width=40)
        lb = Tkinter.Label(parent,text=lbl)
        lb.grid(column=0,row=0,columnspan=2)
        entry.grid(column=2,row=0,columnspan=2)
        entry.bind("<Return>",(lambda event: self.OnClickConnect()))

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

    def line3(self,parent):
        button_sub = Tkinter.Button(parent,text=u"Submit",
                                command=self.OnButtonSubmit)
        button_stop = Tkinter.Button(parent,text=u"Stop",
                                command=self.OnButtonStop)
        button_sub.grid(column=0,row=0)
        button_stop.grid(column=1,row=0)

    def OnButtonClick(self):
        pass

    def OnClickConnect(self):
        self.mess.connect(self.cmd.get())
    
    def OnButtonClickOpenfile(self):
        ftypes = [('JSON files', '*.json'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        self.src.set(fl)
        self.sr.update()
        f = open(fl, "r")
        self.text = f.read()

    def OnButtonSubmit(self):
        if len(self.text) == 0:
            print "Command message not defined: nothing to do"
            pass
        self.mess.send(self.text)

    def OnButtonStop(self):
        self.mess.send("{\"cmd\": \"FileWriter_exit\",\"teamid\": 0}")
