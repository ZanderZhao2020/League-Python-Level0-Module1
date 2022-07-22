import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
	window = Tk()
	window.withdraw()

	# Make a new turtle
	Bob = turtle.Turtle()
	# Ask the user what shape they want to draw and store it in a variable
	Answer = simpledialog.askstring("Prompt", "Enter the shape (triangle, circle, square)").lower()
	# Draw the shape requested by the user using if-elif-else statements
	if Answer == "triangle":
		Bob.circle(50, 360, 3)
	elif Answer == "circle":
		Bob.circle(50, 360, 50)
	elif Answer == "square":
		Bob.circle(50, 360, 4)
	else:
		messagebox.showinfo("Message", "Bad shape")
	# Call the turtle .done() method
	turtle.done()