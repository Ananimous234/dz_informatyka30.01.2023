import sys
import tkinter as tk
import math
from tkinter import messagebox as mb
from tkinter import *
def add_digit(digit):
    value = calc.get()
    if value[0] == '0':
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)


def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


def calculate():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value + value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, eval(value))


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, 0)


def cos():
    value = calc.get()
    x = float(value)
    value = math.cos(x)
    calc.delete(0, tk.END)
    calc.insert(0, value)


def sin():
    value = calc.get()
    x = float(value)
    value = math.sin(x)
    calc.delete(0, tk.END)
    calc.insert(0, value)


def tan():
    value = calc.get()
    x = float(value)
    value = math.tan(x)
    calc.delete(0, tk.END)
    calc.insert(0, value)


def ctg():
    value = calc.get()
    x = float(value)
    value = math.cos(x) / math.sin(x)
    calc.delete(0, tk.END)
    calc.insert(0, value)


def log():
    value = calc.get()
    x = float(value)
    value = math.log2(x)
    calc.delete(0, tk.END)
    calc.insert(0, value)


def ln():
    value = calc.get()
    x = float(value)
    value = math.log10(x)
    calc.delete(0, tk.END)
    calc.insert(0, value)

def sqrt():
    value = calc.get()
    x = float(value)
    value = math.sqrt(x)
    calc.delete(0, tk.END)
    calc.insert(0, value)

def x2():
    value = calc.get()
    x = float(value)
    value = math.pow(x, 2)
    calc.delete(0, tk.END)
    calc.insert(0, value)

def abbreviation(digit):
    return tk.Button(text=digit, bd=5, command=lambda: add_digit(digit), fg = '#000', bg = '#fefefe', font=('Times New Roman', 20))


def abbreviation_operation_button(operation):
    return tk.Button(text=operation, bd=7, command=lambda: add_operation(operation),fg = '#000', bg = '#fefefe', font=('Times New Roman', 20))


def abbreviation_calc_button(operation):
    return tk.Button(text=operation, bd=7, command=calculate, fg = '#000', bg = '#fefefe', font=('Times New Roman', 20))


def abbreviation_clear_button(operation):
    return tk.Button(text=operation, bd=7, command=clear, fg = '#DC143C', bg = '#fefefe', font=('Times New Roman', 20))


def cos_button(operation):
    return tk.Button(text=operation, bd=7, command=cos, fg = '#000', bg = '#fefefe', font=('Times New Roman', 20))


def sin_button(operation):
    return tk.Button(text=operation, bd=7, command=sin, fg = '#000', bg = '#fefefe', font=('Times New Roman', 20))


def tan_button(operation):
    return tk.Button(text=operation, bd=7, command=tan, fg = '#000', bg = '#fefefe', font=('Times New Roman', 20))


def ctg_button(operation):
    return tk.Button(text=operation, bd=7, command=ctg, fg = '#000', bg = '#fefefe', font=('Times New Roman', 20))


def log_button(operation):
    return tk.Button(text=operation, bd=7, command=log, fg = '#000', bg = '#fefefe', font=('Times New Roman', 20))


def ln_button(operation):
    return tk.Button(text=operation, bd=7, command=ln, fg = '#000', bg = '#fefefe', font=('Times New Roman', 20))

def sqrt_button(operation):
    return tk.Button(text=operation, bd=7, command=sqrt, fg = '#000', bg = '#fefefe', font=('Times New Roman', 20))

def x2_button(operation):
    return tk.Button(text=operation, bd=7, command=x2, fg = '#000', bg = '#fefefe', font=('Times New Roman', 20))

root = tk.Tk()
root['bg'] = '#fefefe'
root.title('Calculator')
root.wm_attributes('-alpha', 1)
root.geometry('400x500')
root.resizable(width=False, height=False)

calc = tk.Entry(root,bd=8, justify=tk.RIGHT, font=('Times New Roman', 24), width=19, fg = '#000')
calc.insert(0, '0')
calc.grid(row=1, column=0, columnspan=4, stick='we', padx=5)

abbreviation('1').grid(row=2, column=1, stick='wens', pady=2, padx=2)
abbreviation('2').grid(row=2, column=2, stick='wens', pady=2, padx=2)
abbreviation('3').grid(row=2, column=3, stick='wens', pady=2, padx=2)
abbreviation('4').grid(row=3, column=1, stick='wens', pady=2, padx=2)
abbreviation('5').grid(row=3, column=2, stick='wens', pady=2, padx=2)
abbreviation('6').grid(row=3, column=3, stick='wens', pady=2, padx=2)
abbreviation('7').grid(row=4, column=1, stick='wens', pady=2, padx=2)
abbreviation('8').grid(row=4, column=2, stick='wens', pady=2, padx=2)
abbreviation('9').grid(row=4, column=3, stick='wens', pady=2, padx=2)
abbreviation('0').grid(row=5, column=2, stick='wens', pady=2, padx=2)
abbreviation_clear_button('C').grid(row=2, column=0, stick='wens', pady=2, padx=2)


abbreviation_operation_button('+').grid(row=2, column=4, stick='wens', pady=2, padx=2)
abbreviation_operation_button('-').grid(row=3, column=4, stick='wens', pady=2, padx=2)
abbreviation_operation_button('/').grid(row=4, column=4, stick='wens', pady=2, padx=2)
abbreviation_operation_button('*').grid(row=5, column=4, stick='wens', pady=2, padx=2)
abbreviation_operation_button('%').grid(row=5, column=3, stick='wens', pady=2, padx=2)
abbreviation_calc_button('=').grid(row=6, column=4, stick='wens', pady=2, padx=2)

x2_button('x²').grid(row=5, column=1, stick='wens', pady=2, padx=2)
sqrt_button('√').grid(row=6, column=1, stick='wens', pady=2, padx=2)
cos_button('cos').grid(row=3, column=0, stick='wens', pady=2, padx=2)
sin_button('sin').grid(row=4, column=0, stick='wens', pady=2, padx=2)
tan_button('tan').grid(row=5, column=0, stick='wens', pady=2, padx=2)
ctg_button('ctg').grid(row=6, column=0, stick='wens', pady=2, padx=2)
log_button('log').grid(row=6, column=2, stick='wens', pady=2, padx=2)
ln_button('ln').grid(row=6, column=3, stick='wens', pady=2, padx=2)

root.grid_columnconfigure(0, minsize=65)
root.grid_columnconfigure(1, minsize=65)
root.grid_columnconfigure(2, minsize=65)
root.grid_columnconfigure(3, minsize=65)
root.grid_columnconfigure(4, minsize=65)

root.grid_rowconfigure(1, minsize=65)
root.grid_rowconfigure(2, minsize=65)
root.grid_rowconfigure(3, minsize=65)
root.grid_rowconfigure(4, minsize=65)
root.grid_rowconfigure(5, minsize=65)
root.grid_rowconfigure(6, minsize=65)

root.mainloop()