#!/usr/bin/env python

import tkinter
import sys

root = tkinter.Tk()

entry = tkinter.Entry(root)
entry.insert(0, "Oh hello there!")

quitbutton = tkinter.Button(root, text="exit", relief="raised", borderwidth=4, command=lambda: sys.exit(0))

entry.grid(column=1, row=1, sticky="we", padx=6, pady=6)
quitbutton.grid(column=1, row=2, sticky="we", padx=6, pady=6)

root.mainloop()
