# Ch.2, Ex.3 (extra credit)
# Saba Feilizadeh
# This program draws a circle at the center of the graphics window and
# prints out the circumference and the area of the circle based on user input.

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
