#!/usr/bin/env python

import tkinter
import sys

root = tkinter.Tk()

value = tkinter.StringVar()

entry = tkinter.Entry(root, textvariable=value)
entry.insert(0, "Oh hello there!")

showbutton = tkinter.Button(root, text="print text", relief="raised", borderwidth=4, command=lambda: print(value.get()))
quitbutton = tkinter.Button(root, text="exit", relief="raised", borderwidth=4, command=lambda: sys.exit(0))

entry.grid(column=1, row=1, sticky="we", padx=6, pady=6)
showbutton.grid(column=1, row=2, sticky="we", padx=6, pady=6)
quitbutton.grid(column=1, row=3, sticky="we", padx=6, pady=6)

root.mainloop()
