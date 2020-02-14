#!/usr/bin/env python

import tkinter
import sys

def exit():
    sys.exit(0)

root = tkinter.Tk()

checkbutton = tkinter.Checkbutton(root, text="Do you like Python?", command=lambda: print("change"))

quitbutton = tkinter.Button(root, text="exit", relief="raised", borderwidth=4, height=1, width=10, command=exit)

checkbutton.pack()
quitbutton.pack()

root.mainloop()
