# Ch.6, Ex.4 (extra credit)
# Saba Feilizadeh
# This program creates a table for the Figure Skating Medals

### TODO
#
# Create a table for the medals. (Use lists)
# Print the table.
# Print the total number of medals.
# Print the total number of gold, silver, and bronze medals.
# Remove countries without a gold medal from the table.
# Then print the new table.
# Use dictionaries to save the data for the countries and the medals and print it, 
# the key is the country name and the value is a list of medals or a dictionary of the medals name and count. 
# (This part is to compare using lists vs. dictionaries to save data)
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