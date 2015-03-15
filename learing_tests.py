__author__ = 'Andrei'


import tkinter

class GuiControl(object):
    def __init__(self,Parent:'root application from Tk'):
        FirstMsg = tkinter.Label(Parent,fg="red",bg="black", text = "Hello World, this is a message from TKinter, delivered as a lable")
        FirstMsg.pack()
        SecMsg = tkinter.Label(Parent,justify = "left", text = "this is another test just to test what ever is going on there")
        SecMsg.pack()
        Mbox = tkinter.Message(Parent,text="this is another test but comming in from a different place")
        Mbox.pack()






def main():
    Application = tkinter.Tk()
    GuiControl(Application)
    Application.mainloop()

if __name__=='__main__':
    main()

