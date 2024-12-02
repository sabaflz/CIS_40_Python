# Ch.2, Ex.3 (extra credit)
# Saba Feilizadeh
# This program draws a circle at the center of the graphics window and
# prints out the circumference and the area of the circle based on user input.

#------------------------------------------------

# prompts the user to enter the
# width
# height of the graphics window
# The radius of a circle
# outline color and
# fill color of the circle

# Then draws the circle at the center of the graphics window and
# prints out the
# - circumference and
# - the area of the circle.

# Extra credit:
# Draw your name, the area and circumference at the coordinate:
# x = %1 of the width of the graphics window (text_x = 0.01 * gw_width) and
# y = %1 of the height of the graphics window (text_y = 0.01 * gw_height) 

# Run your code and put at least two results (outputs) with 
# two different numbers(inputs)  (results after you run your code) 
# at the end of your code as a multi-line comment.

# You can use

#     canvas.setBackground(255, 255, 224) to set the background color.
#     canvas.setTextAnchor("nw") to set the text anchor to north-west.
#     canvas.setLineWidth(5) to set a width for the lines (making the circle border thicker)
#     win.setTitle("CIS40 - Ch2 Ex3") to set a title for the graphics window.
#     text_x = 0.01* gw_width
#     text_y = 0.01* gw_height
#     Ask the user to enter the user_name
#     message = user_name + "\nThe circumference:" + str(circumference) + "\nThe area:" + str(area)
#     canvas.drawText(text_x , text_y , message)

#------------------------------------------------

from graphics import GraphicsWindow
import math

win = GraphicsWindow()
canvas = win.canvas()

canvas.drawRect(10, 20, 10, 10)

width = float(input("Enter Width: "))
height = float(input("Enter Height: "))
radius = float(input("Enter Radius: "))
outline_color = float(input("Enter Outline Color: "))
fill_color = float(input("Enter Fill Color: "))



canvas.setBackground(255, 255, 224)
print("width: ", width)


'''
Outputs:


'''
