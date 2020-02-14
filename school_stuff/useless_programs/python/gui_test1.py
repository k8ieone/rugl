#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter
import sys

def exit():
    sys.exit(0)

main_window = tkinter.Tk()

label = tkinter.Label(main_window, text="Hello friend.")
button = tkinter.Button(main_window, text="Exit", command=exit)

button.configure(background="yellow", foreground="red")
# More settings: borderwidth activebackground activeforeground disabledforeground
# compound bitmap image font text cursor textvariable justify anchor
# relief (sunken, solid, flat, groove, raised, ridge)
# padx, pady (padding = spacing between buttons)
# height, width

label.pack()
button.pack()

main_window.mainloop()
