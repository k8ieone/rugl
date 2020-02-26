#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter
import sys

main_window = tkinter.Tk()

button1 = tkinter.Button(main_window, text="První")
button2 = tkinter.Button(main_window, text="Druhé")
button3 = tkinter.Button(main_window, text="Třetí")
button4 = tkinter.Button(main_window, text="Čtvrté")

button1.grid(column=1, row=3)
button2.grid(column=2, row=3)
button3.grid(column=1, row=4)
button4.grid(column=2, row=4)

main_window.mainloop()
