# Ch.5, Ex.1
# Saba Feilizadeh
# Write two functions: main calls get_inputs to get and print user's inputs


# Constant for the floating point precision
PRECISION = 2

def get_inputs():
    """
    This function gets the rate and the hours from the user
    """

    # Get the user's input
    hours = float(input("Enter Hours: "))
    
    rate = float(input("Enter Rate: "))

    # Output for the user
    print("Hours: ", round(hours , PRECISION))
                                     
    print("Rate: ", round(rate , PRECISION))

    
def main():
    get_inputs()


main()

print("Done!")    



'''
Outputs:

Enter Hours: 23.33333
Enter Rate: 19.77777
Hours:  23.33
Rate:  19.78
Done!

---------------------------------------------------

Enter Hours: 16
Enter Rate: 23.456
Hours:  16.0
Rate:  23.46
Done!

'''
