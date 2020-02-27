#!/usr/bin/env python

import tkinter

root = tkinter.Tk()
root.title("Obvod/obsah čtverce")
obsah = tkinter.StringVar()
obvod = tkinter.StringVar()
entryvar = tkinter.StringVar()

def calculate_obsah(smt):
    try:
        result = "Obsah je: " + str(float(smt.get()) ** 2)
    except:
        result = "Nelze vypočítat!"
    return result

def calculate_obvod(smt):
    try:
        result = "Obvod je: " + str(float(smt.get()) * 4)
    except:
        result = "Nelze vypočítat!"
    return result

label = tkinter.Label(root, text="délka strany", padx = 10)
textbox = tkinter.Entry(root, textvar = entryvar)

button1 = tkinter.Button(root, text="Obsah", pady = 10, command = lambda: obsah.set(calculate_obsah(entryvar)))
button2 = tkinter.Button(root, text = "Obvod", pady = 10, command = lambda: obvod.set(calculate_obvod(entryvar)))

textbox_obsah = tkinter.Label(root, textvar = obsah)
textbox_obvod = tkinter.Label(root, textvar = obvod)

label.grid(row = 0, column = 0)
textbox.grid(row = 0, column = 1, columnspan = 2)

button1.grid(row = 1, column = 0, sticky = "we")
button2.grid(row = 2, column = 0, sticky = "we")

textbox_obsah.grid(row = 1, column = 1, columnspan = 2)
textbox_obvod.grid(row = 2, column = 1, columnspan = 2)

root.mainloop()
