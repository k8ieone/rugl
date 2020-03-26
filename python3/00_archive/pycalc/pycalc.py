#!/usr/bin/env python

import tkinter
import tkinter.simpledialog
import tkinter.filedialog

def calculate(equation):
    expression = str(equation.get())
    try:
        expression = str(eval(expression))
    except ZeroDivisionError:
        expression = "Division by zero!"
    except:
        expression = "ERROR"
    return expression

def copy_to_clipboard(stuff):
    root.clipboard_clear()
    root.clipboard_append(stuff)
    root.update()

def cut_to_clipboard(stuff):
    root.clipboard_clear()
    root.clipboard_append(stuff)
    root.update()
    return stuff.get()

def open_context(ev):
    context.post(ev.x_root-5, ev.y_root-5)

def save_as_text(stuff):
    filetypes = [("Text file", "*.txt")]
    dialog = tkinter.filedialog.SaveAs(root, filetypes=filetypes, initialfile="equation")
    filepath = dialog.show()
    if filepath is None or filepath == '':
        pass
    else:
        with open(filepath, "w") as file1:
            file1.writelines(stuff)

def open_file():
    filetypes = [("Text file", "*.txt")]
    dialog = tkinter.filedialog.Open(root, filetypes=filetypes)
    filepath = dialog.show()
    with open(filepath, "r") as file1:
        equation = file1.readline()
    if filepath is None or filepath == '':
        pass
    else:
        return equation


# Variables definition
root = tkinter.Tk()
equation = tkinter.StringVar()
root.title("pycalc")

# The text field
field = tkinter.Entry(root, textvariable=equation)
field.grid(row = 0, column = 0, columnspan = 4)

# Context menu
context = tkinter.Menu(root, tearoff=0)

context.add_command(label="Copy", command = lambda: copy_to_clipboard(str(equation.get())))
context.add_command(label="Cut", command = lambda: equation.set(cut_to_clipboard(str(equation.get()))))
context.add_command(label="Paste", command = lambda: equation.set(str(equation.get() + root.clipboard_get())))
context.add_separator()
context.add_command(label="Exit", command=root.quit)

field.bind("<Button-3>", open_context)

# Menubar
menubar = tkinter.Menu(root)

filemenu = tkinter.Menu(menubar, tearoff=0)
constantsmenu = tkinter.Menu(menubar, tearoff=0)
mathsmenu = tkinter.Menu(constantsmenu, tearoff=0)
elemenu = tkinter.Menu(constantsmenu, tearoff=0)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Constants", menu=constantsmenu)

filemenu.add_command(label="Save equation as", activebackground="#00ccff", command=lambda: save_as_text(equation.get()))
filemenu.add_command(label="Open equation", activebackground="#00ccff", command=lambda: equation.set(open_file()))
filemenu.add_separator()
filemenu.add_command(label="Change window title", activebackground="#00ccff", command = lambda: root.title(tkinter.simpledialog.askstring("New window title", "Enter the new window name.", initialvalue="pycalc")))
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit, activebackground="red")

constantsmenu.add_cascade(label="Mathematics", menu=mathsmenu, activebackground="#00ccff")
mathsmenu.add_command(label="Pi", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "3.14159265359"))
mathsmenu.add_command(label="Euler number", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "2.71828182846"))
mathsmenu.add_command(label="Golden ratio", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "1.61803398875"))
constantsmenu.add_cascade(label="Electromagnetism", menu=elemenu, activebackground="#00ccff")
elemenu.add_command(label="Light speed", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "299792458"))
elemenu.add_command(label="Impedance of vaccum", activebackground="#00ccff", command = lambda: equation.set(equation.get() + "376.730313461"))

# Buttons
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
root.bind('<Return>', (lambda event: equation.set(calculate(equation))))
root.bind('<KP_Enter>', (lambda event: equation.set(calculate(equation))))
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

root.config(menu=menubar)
root.mainloop()
