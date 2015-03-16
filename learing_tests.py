__author__ = 'Andrei'


import tkinter

class GuiControl(object):
    def __init__(self,Parent:'root application from Tk'):
        self.App = Parent
        self.App.title ("ceva")
        self.App.protocol("WM_DELETE_WINDOW",self.trapClose)
        self.Frame1 = tkinter.Frame(self.App)
        self.Frame1.pack()
        self.Frame2 = tkinter.Frame(self.App)
        self.Frame2.pack()
        self.FirstMsg = tkinter.Label(self.Frame1,fg="red",bg="black", text = "Hello World, this is a message from TKinter, delivered as a lable")
        self.FirstMsg.pack(side = "left")
        self.SecMsg = tkinter.Label(self.Frame1, text = "this is another test just to test what ever is going on there")
        self.SecMsg.pack(side = "left")
        self.Mbox = tkinter.Message(self.Frame1,text="this is another test but comming in from a different place")
        self.Mbox.pack(side = "left")

        self.OK = tkinter.Button(self.Frame1,text = "salut")
        self.OK["bg"] = "red"
        self.OK["fg"] = "black"
        self.OK.pack(side="bottom",anchor = "e")
        self.OK.bind("<Button-1>",self.pushed)

    def pushed(self,event):
        print("just got pressed {}".format(event))
    def trapClose(self):
        print("just got closed")
        self.App.destroy()

def main():
    Application = tkinter.Tk()
    GuiControl(Application)    
    Application.mainloop()

if __name__=='__main__':
    main()
