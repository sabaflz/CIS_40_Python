# Test opening a file
file_name = "temp.txt"

try:
    with open(file_name, 'r') as file:
        print(f"File '{file_name}' opened successfully!")
        print("Here are the first few lines of the file:\n")
        for i, line in enumerate(file):
            if i >= 5:  # Show only the first 5 lines
                break
            print(line.strip())
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except PermissionError:
    print(f"Error: Permission denied to open the file '{file_name}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
#####################################################
# Ch.2, Ex.3 (extra credit)
# Saba Feilizadeh
# This program draws a circle at the center of the graphics window and
# prints out the circumference and the area of the circle based on user input.

import tkinter as tk
import math

# --------------------------------------------------------------------------
def draw_circle(user_input):

    # initialize variables based on user input
    window_width, window_height, radius,\
        outline_color, fill_color,user_name = user_input
    
    # Create the main tkinter window
    root = tk.Tk()
    canvas = tk.Canvas(root, width = window_width, height = window_height)
    canvas.pack()
    canvas.create_oval(100, 100, 300, 300, fill="red")
    root.mainloop()
# --------------------------------------------------------------------------
def get_user_input():
    # Get user inputs
    window_width = float(input("Enter Width: "))
    window_height = float(input("Enter Height: "))
    radius = float(input("Enter Radius: "))
    outline_color = float(input("Enter Outline Color: "))
    fill_color = float(input("Enter Fill Color: "))
    # user_name = float(input("Enter your name: "))
    user_name = "Saba Feilizadeh"

    return window_width, window_height, \
        radius, outline_color, fill_color,user_name
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
def main():
    # Get data from the user
    user_input = get_user_input()
    draw_circle(user_input)
    
# --------------------------------------------------------------------------
if __name__ == "__main__":
    main()
# --------------------------------------------------------------------------

# win = GraphicsWindow()
# canvas = win.canvas()

# canvas.drawRect(10, 20, 10, 10)

# width = float(input("Enter Width: "))
# height = float(input("Enter Height: "))
# radius = float(input("Enter Radius: "))
# outline_color = float(input("Enter Outline Color: "))
# fill_color = float(input("Enter Fill Color: "))



# canvas.setBackground(255, 255, 224)
# print("width: ", width)


'''
Outputs:


'''