# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

# Area = πr^2
# Circumference = 2πr
import math
from tkinter import simpledialog, messagebox

Radius = simpledialog.askinteger("Question", "Enter the radius")
Answer = simpledialog.askstring("Prompt", "Area or circumference?").lower()
if Answer == "area":
	messagebox.showinfo("Message", Radius ** 2 * math.pi)
elif Answer == "circumference":
	messagebox.showinfo("Message", 2 * math.pi * Radius)
else:
	messagebox.showinfo("Message", "Bad answer")