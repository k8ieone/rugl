#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter
import sys

def exit():
    sys.exit(0)

main_window = tkinter.Tk()

label = tkinter.Label(main_window, text="Hello friend.")
button = tkinter.Button(main_window, text="Exit", command=exit)

button1 = tkinter.Button(main_window, text="První")
button2 = tkinter.Button(main_window, text="Druhé")
button3 = tkinter.Button(main_window, text="Třetí")
button4 = tkinter.Button(main_window, text="Čtvrté")

label.grid(column=1, row=1)
button.grid(column=1, row=2)

button1.grid(column=1, row=3)
button2.grid(column=2, row=3)
button3.grid(column=1, row=4)
button4.grid(column=2, row=4)

# label.pack()
# button.pack()

main_window.mainloop()
