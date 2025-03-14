from tkinter import *
from tkinter import ttk
from login import Login
from login import Registro
from container import Container
import sys
import os

class Manager(Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("Mini Market")
        self.geometry("1100x650+120+20")
        self.resizable(False,False)

        container = Frame(self)
        container.pack(fill=BOTH,expand=True,side=TOP)
        container.configure(bg="#C6D9E3")

        self.frames = {}
        for i in (Login,Registro,Container):
            frame = i(container,self)
            self.frames[i] = frame

        self.show_frame(Login)

        self.style=ttk.Style()
        self.style.theme_use('clam')

    def show_frame(self,container):
        frame = self.frames[container]
        frame.tkraise()

def main():
    app = Manager()
    app.mainloop()

if __name__ == '__main__':
    main()