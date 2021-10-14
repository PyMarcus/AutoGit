#!/usr/bin/env python
from git import Git
import interface
from tkinter import *



if __name__ == '__main__':
    root = Tk()
    interface.App(root)
    root.title("AutoGit")
    root.geometry('600x400')
    # abre no centro
    interface.center(root)
    root.mainloop()
