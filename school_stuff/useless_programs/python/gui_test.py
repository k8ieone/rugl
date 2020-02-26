#!/usr/bin/env python

import tkinter
import sys

main_window = tkinter.Tk()

pressed1 = tkinter.StringVar()
pressed2 = tkinter.StringVar()

textbox1 = tkinter.Label(main_window, textvariable=pressed1)
button1 = tkinter.Button(main_window, text="Tlačítko 1", borderwidth=4, command=lambda: pressed1.set("stisknuto"), relief="groove")
textbox2 = tkinter.Label(main_window, textvariable=pressed2)
button2 = tkinter.Button(main_window, text="Tlačítko 2", borderwidth=4, command=lambda: pressed2.set("stisknuto"), relief="groove")
exitbutton = tkinter.Button(main_window, borderwidth=4, text="exit", height=6, background="green", foreground="yellow", command=lambda: sys.exit(0), relief="groove")

textbox1.grid(column=1, row=1, padx=6, pady=6)
button1.grid(column=1, row=2, padx=6, pady=6)
textbox2.grid(column=2, row=1, padx=6, pady=6)
button2.grid(column=2, row=2, padx=6, pady=6)
exitbutton.grid(column=3, row=1, padx=6, pady=6)

main_window.mainloop()
