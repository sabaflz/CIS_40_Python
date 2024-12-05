# Ch.9 (extra credit)
# Saba Feilizadeh
# This program creates a table for the Figure Skating Medals

### TODO
#
# P9.12 Write a class Bug that models a bug moving along a horizontal line.
# The bug moves either to the right or left. Initially,
# the bug moves to the right, but it can turn to change its direction.
# In each move, its position changes by one unit in the current direction.
# Provide a constructor def __init__ (self, initialPosition) and methods
# def turn(self)
# def move(self)
# def getPosition(self)
# Sample usage:
# bugsy = Bug (10)
# bugsy.move() # Now the position is 11
# bugsy.turn()
# bugsy.move() # Now the position is 10

# Your driver program should construct a bug,
# make it move and turn a few times, and print the actual and expected positions.
###

# Constant for the width of the line for the output
LINE_WIDTH = 50
# --------------------------------------------------------------------------
class Bug:
    def __init__(self, initialPosition):
        """
        Initializes the bug's position and direction.
        The bug moves to the right by default
        """
        self.position = initialPosition
        self.direction = "right"

    def turn(self):
        """
        Riverses the direction of the bug.
        If it's moving right, it will start moving left, and vice versa.
        """
        if self.direction == "right":
            self.direction = "left"
        else:
            self.direction = "right"

        print("Turned ...")

    def move(self):
        """
        Moves the bug one unit in it's current direction
        """
        if self.direction == "right":
            self.position += 1
        else:
            self.position -= 1
        print("Moved  ...")

    def getPosition(self):
        """
        Returns the current position of the bug.
        """
        return self.position

# --------------------------------------------------------------------------
def main():
    # Create an instance of the Bug class
    bugsy = Bug(10)

    # Print the start position
    print(f"Bug's start position: {bugsy.getPosition()}")
    
    # Move the bug
    bugsy.move() # Now the position should be 11
    print(f"Bug's expected position: 11")
    print(f"Bug's actual position:   {bugsy.getPosition()}")

    # Turn the bug and move again
    bugsy.turn()
    bugsy.move() # Now the position should be 10
    print(f"Bug's expected position: 10")
    print(f"Bug's actual position:   {bugsy.getPosition()}")

    # Turn and move a few more times
    bugsy.turn()
    bugsy.move() # 11
    bugsy.move() # 12
    bugsy.move() # 13
    bugsy.move() # 14
    bugsy.move() # 15
    bugsy.turn()
    bugsy.move() # 14
    print(f"Bug's expected position: 14")
    print(f"Bug's actual position:   {bugsy.getPosition()}")

# --------------------------------------------------------------------------
main()
print("Done!")
# --------------------------------------------------------------------------
'''
Output:

Bug's start position: 10
Moved  ...
Bug's expected position: 11
Bug's actual position:   11
Turned ...
Moved  ...
Bug's expected position: 10
Bug's actual position:   10
Turned ...
Moved  ...
Moved  ...
Moved  ...
Moved  ...
Moved  ...
Turned ...
Moved  ...
Bug's expected position: 14
Bug's actual position:   14
Done!

'''