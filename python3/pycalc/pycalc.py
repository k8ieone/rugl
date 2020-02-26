#!/usr/bin/env python

import tkinter

def calculate(equation):
    expression = str(equation.get())
    try:
        expression = str(eval(expression))
    except:
        expression = "ERROR"
    return expression

root = tkinter.Tk()

equation = tkinter.StringVar()
numbuttons = []

field = tkinter.Entry(root, textvariable=equation)
field.grid(row = 0, column = 0, columnspan = 4)

button1 = tkinter.Button(root, text = "1", pady=6, padx=16, relief="solid", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "1"))
button2 = tkinter.Button(root, text = "2", pady=6, padx=16, relief="solid", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "2"))
button3 = tkinter.Button(root, text = "3", pady=6, padx=16, relief="solid", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "3"))
button4 = tkinter.Button(root, text = "4", pady=6, padx=16, relief="solid", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "4"))
button5 = tkinter.Button(root, text = "5", pady=6, padx=16, relief="solid", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "5"))
button6 = tkinter.Button(root, text = "6", pady=6, padx=16, relief="solid", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "6"))
button7 = tkinter.Button(root, text = "7", pady=6, padx=16, relief="solid", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "7"))
button8 = tkinter.Button(root, text = "8", pady=6, padx=16, relief="solid", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "8"))
button9 = tkinter.Button(root, text = "9", pady=6, padx=16, relief="solid", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "9"))
button0 = tkinter.Button(root, text = "0", pady=6, padx=16, relief="solid", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "0"))

dot = tkinter.Button(root, text = ".", pady=6, padx=18, relief="solid", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "."))

plus = tkinter.Button(root, text = "+", pady=6, padx=6, width=2, relief="solid", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "+"))
minus = tkinter.Button(root, text = "-", pady=6, padx=6, width=2, relief="solid", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "-"))
times = tkinter.Button(root, text = "×", pady=6, padx=6, width=2, relief="solid", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "*"))
divide = tkinter.Button(root, text = "/", pady=6, padx=6, width=2, relief="solid", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "/"))

equal = tkinter.Button(root, text = "=", pady=46, padx=6, width=2, relief="solid", activebackground="#00ccff", command = lambda: equation.set(calculate(equation)))
root.bind('<Return>', (lambda event: equation.set(calculate(equation)))) # TODO
clear = tkinter.Button(root, text = "CLR", pady=12, padx=12, relief="solid", activebackground="red", command = lambda: equation.set(""))

button1.grid(row = 1, column = 0)
button2.grid(row = 1, column = 1)
button3.grid(row = 1, column = 2)
button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)
button7.grid(row = 3, column = 0)
button8.grid(row = 3, column = 1)
button9.grid(row = 3, column = 2)
button0.grid(row = 4, column = 0, columnspan = 2, sticky="we")

dot.grid(row = 4, column = 2)
plus.grid(row = 1, column = 4)
minus.grid(row = 2, column = 4)
times.grid(row = 1, column = 5)
divide.grid(row = 2, column = 5)
equal.grid(row = 3, column = 4, sticky = "we", columnspan = 2, rowspan = 3)
clear.grid(row = 5, column = 0, sticky = "we", columnspan = 3, rowspan = 1)

root.mainloop()