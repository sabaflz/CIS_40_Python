# Ch.2, Ex.3 (extra credit)
# Saba Feilizadeh
# This program draws a circle at the center of the graphics window and
# prints out the circumference and the area of the circle based on user input.

import tkinter as tk
import math

# Constants
BACKGROUND_COLOR = "white"
FONT = ("Arial", 12)
LINE_WIDTH = 5

# --------------------------------------------------------------------------
def get_user_input():
    """
    This function prompts the user for the graphics window size,
    circle properties, and colors.
    Returns a dictionary of user inputs.
    """
    gw_width = int(input("Enter the width of the graphics window: "))
    gw_height = int(input("Enter the height of the graphics window: "))
    radius = float(input("Enter the radius of the circle: "))
    outline_color = input("Enter the outline color of the circle: ")
    fill_color = input("Enter the fill color of the circle: ")

    return {
        "gw_width": gw_width,
        "gw_height": gw_height,
        "radius": radius,
        "outline_color": outline_color,
        "fill_color": fill_color,
    }

# --------------------------------------------------------------------------
def calculate_circle_properties(radius):
    """
    This function calculates and returns the circumference and area 
    of a circle based on its radius.
    """
    # Calculate the circumference of a circle
    circumference = 2 * math.pi * radius
    # Calculate the area of a circle
    area = math.pi * radius**2
    return circumference, area

# --------------------------------------------------------------------------
def display_circle_info_console(name, gw_width, gw_height,
                                radius, circumference, area):
    """
    This function prints the circle information
    (name, window size, radius, circumference, area) to the console.
    """
    print(f"\n{name}'s Circle")
    print(f"Graphics window dimensions: {gw_width}x{gw_height}")
    print(f"Circle radius: {radius}")
    print(f"Circumference: {circumference:.2f}")
    print(f"Area: {area:.2f}")

# --------------------------------------------------------------------------
def setup_canvas(window, width, height):
    """
    This function sets up and returns a tkinter Canvas object with
    the given width and height.
    """
    canvas = tk.Canvas(window, width=width, height=height, bg=BACKGROUND_COLOR)
    canvas.pack()
    return canvas

# --------------------------------------------------------------------------
def draw_circle(canvas, center_x, center_y, radius, outline_color, fill_color):
    """
    This function draws a circle on the canvas with the given parameters.
    """
    canvas.create_oval(
        center_x - radius, center_y - radius,
        center_x + radius, center_y + radius,
        outline=outline_color, fill=fill_color, width=LINE_WIDTH
    )

# --------------------------------------------------------------------------
def display_text(canvas, text_x, text_y, message):
    """
    This function displays text on the canvas at the specified position.
    """
    canvas.create_text(
        text_x, text_y, anchor="nw", text=message, fill="black", font=FONT
    )

# --------------------------------------------------------------------------
def main():
    
    name = "Saba Feilizadeh"

    # Get user input
    user_input = get_user_input()
    # Initialize variables based on user's input
    gw_width = user_input["gw_width"]
    gw_height = user_input["gw_height"]
    radius = user_input["radius"]
    outline_color = user_input["outline_color"]
    fill_color = user_input["fill_color"]

    # Calculate circle's circumference and area 
    circumference, area = calculate_circle_properties(radius)

    # Display results in the console
    display_circle_info_console(name, gw_width, gw_height,
                                radius, circumference, area)

    # Create the graphics window
    root = tk.Tk()
    root.title(f"{name}")

    # Setup canvas
    canvas = setup_canvas(root, gw_width, gw_height)

    # Draw the circle
    center_x = gw_width / 2
    center_y = gw_height / 2
    draw_circle(canvas, center_x, center_y, radius, outline_color, fill_color)

    # Display text on the canvas
    text_x = 0.01 * gw_width  # 1% of the width
    text_y = 0.01 * gw_height  # 1% of the height
    message = f"{name}\nCircumference: {circumference:.2f}\nArea: {area:.2f}"
    display_text(canvas, text_x, text_y, message)

    # Start tkinter loop
    root.mainloop()
# --------------------------------------------------------------------------
if __name__ == "__main__":
    main()
# --------------------------------------------------------------------------
'''
# ------------------------------------------------------
                        Output 1
# ------------------------------------------------------
Enter the width of the graphics window: 400
Enter the height of the graphics window: 300
Enter the radius of the circle: 30
Enter the outline color of the circle: teal        
Enter the fill color of the circle: mediumaquamarine

Saba Feilizadeh's Circle
Graphics window dimensions: 400x300
Circle radius: 30.0
Circumference: 188.50
Area: 2827.43
# ------------------------------------------------------
                        Output 2
# ------------------------------------------------------
Enter the width of the graphics window: 600
Enter the height of the graphics window: 600
Enter the radius of the circle: 55
Enter the outline color of the circle: maroon
Enter the fill color of the circle: orange

Saba Feilizadeh's Circle
Graphics window dimensions: 600x600
Circle radius: 55.0
Circumference: 345.58
Area: 9503.32

'''