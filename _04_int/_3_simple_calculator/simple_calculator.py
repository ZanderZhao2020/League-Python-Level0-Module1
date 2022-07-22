"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
from tkinter import simpledialog, messagebox

Num1 = simpledialog.askinteger("Prompt", "Enter number 1")
Num2 = simpledialog.askinteger("Prompt", "Enter number 2")
Answer = simpledialog.askstring("Prompt", "Enter operation (add, sub, mult, div)").lower()
if Answer == "add":
	messagebox.showinfo("Message", str(Num1 + Num2))
elif Answer == "sub":
	messagebox.showinfo("Message", str(Num1 - Num2))
elif Answer == "mult":
	messagebox.showinfo("Message", str(Num1 * Num2))
elif Answer == "div":
	messagebox.showinfo("Message", str(Num1 / Num2))
else:
	messagebox.showerror("Error", "Bad operation")