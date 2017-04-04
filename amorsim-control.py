#!/bin/python

import Tkinter, tkFileDialog
import essfw
import quitbutton
import el737

        
class AppBase(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.fw_command = Tkinter.StringVar()
        self.resultsContents = Tkinter.StringVar()
        self.resultsContents.set("")
        
        self.initialize()

        
    def initialize(self):
        self.grid()

        lf1 = essfw.ESSFileWriter(self,"send-command")

        lf2 = el737.EL737(self,"EL737 counterbox")

        lf3 = quitbutton.ExitFrame(self)
        
        
        self.update()
        self.resizable(True,True)
    
    def Quit(self):
        self.quit()
    
if __name__ == "__main__":
    amorsim = AppBase(None)
    amorsim.title('sinq-amorsim control')
    amorsim.mainloop()
