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

# List of medals for each country
# Country,  Gold,  Silver,  Bronze
canada = [0, 3, 0]
italy = [0, 0, 1]
germany = [0, 0, 1]
japan = [1, 0, 0]
russia = [3, 1, 1]
southkorea = [0, 1, 0]
us = [1, 0, 1]

# --------------------------------------------------------------------------
def print_table():
    '''
    This function prints a table, showing the medal count for each country.
    '''
    # Table header
    print("Gold", "Silver", "Bronze")

    # Table content
    print("Canada", canada)
    print("Italy", italy)
    print("Germany",germany)
    print("Japan", japan)
    print("Russia",russia)
    print("South Korea", southkorea)
    print("United States", us)

    print("*" * LINE_WIDTH)
    print("-" * (LINE_WIDTH // 2))

# --------------------------------------------------------------------------
def main():
    
    print_table()
    

# --------------------------------------------------------------------------
main()

print("Done!")

# --------------------------------------------------------------------------
'''
Output 1:


'''