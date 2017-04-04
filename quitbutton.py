import Tkinter, tkFileDialog

class ExitFrame(Tkinter.Frame):
    def __init__(self,parent):
        Tkinter.Frame.__init__(self,parent)
        self.parent = parent

        bottom = Tkinter.Frame(parent)
        quit = Tkinter.Button(bottom,text=u"Exit",
                                  command=parent.Quit,
                                  relief="groove")
        quit.grid(column=0)
        bottom.grid(row=100)
        
        self.grid()
