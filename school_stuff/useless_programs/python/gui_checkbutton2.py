#!/usr/bin/env python

import tkinter
import sys

root = tkinter.Tk()

like_python = tkinter.StringVar()

checkbutton = tkinter.Checkbutton(root, text="Do you like Python?", variable=like_python, onvalue="yes", offvalue="no", command=lambda: label.configure(text="Choice: " + like_python.get()))
label = tkinter.Label(root, text="not me...")

quitbutton = tkinter.Button(root, text="exit", relief="raised", borderwidth=4, height=1, width=10, command=lambda: sys.exit(0))

checkbutton.pack()
label.pack()
quitbutton.pack()

root.mainloop()
