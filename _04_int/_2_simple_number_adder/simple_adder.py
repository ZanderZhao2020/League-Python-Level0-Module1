"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import messagebox, simpledialog

messagebox.showinfo("Message", str(simpledialog.askinteger("Prompt", "Enter number 1") + simpledialog.askinteger("Prompt", "Enter number 2")))