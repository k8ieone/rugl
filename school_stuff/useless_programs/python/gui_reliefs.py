#!/usr/bin/env python

import tkinter
import sys

def exit():
    sys.exit(0)

root = tkinter.Tk()
buttonReliefs = ["sunken", "solid", "flat", "groove", "raised", "ridge"]

buttons = []

for buttonRelief in buttonReliefs:
    buttons.append(tkinter.Button(root, text=buttonRelief, relief=buttonRelief))

quitButton = tkinter.Button(root, text="exit", background="red", command=exit)

for i, button in enumerate(buttons):
    button.grid(column=1, row=i, sticky="we")

quitButton.grid(column=1, row=7, sticky="we")

root.mainloop()
