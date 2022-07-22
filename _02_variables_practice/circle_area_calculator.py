import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
	window = Tk()
	window.withdraw()

	# Ask the user for the radius in pixels and store it in a variable
	# simpledialog.askinteger()
	Radius = simpledialog.askinteger("Prompt", "Enter the radius")
	# Make a new turtle
	Bob = turtle.Turtle()
	# Have your turtle draw a circle with the correct radius
	# my_turtle.circle()
	Bob.circle(5)
	# Call the turtle .penup() method
	Bob.penup()
	# Move your turtle to a new x,y position using .goto()
	Bob.goto(-10, -10)
	# Calculate the area of your circle and store it in a variable
	# Hint, you can use math.pi
	Area = Radius ** 2 * math.pi
	# Write the area of your circle using the turtle .write() method
	Bob.write(arg="area = " + str(Area), move=True, align='left', font=('Arial',8,'normal'))

	# Hide your turtle
	Bob.hideturtle()
	# Call turtle.done()
	turtle.done()