# Ch.5, Ex.2
# Saba Feilizadeh
# Write three functions to:
# - Get the hours and rate from the user
# - Validate the inputs
# - Calculate the  gross pay
# - Print the gross pay for the user


# A constant for the overtime hour limit
OVERTIME = 40

# Overtime rate factor
OVERTIME_FACTOR = 1.5

# Constant for the floating point precision
PRECISION = 2

# --------------------------------------------------------------------------

def get_input():
    
    """
    This function gets the rate and the hours from the user
    """

    # Get the user's input with a while loop

    flag = True

    while flag:
        try:
            hours = float(input("Enter Hours: "))

            try:
                rate = float(input("Enter Rate: "))
                
                if hours <= 0 or rate <= 0:
                    print("Please enter positive numbers!")
                        
                else:
                    flag = False
                        
            except:
                print("Error, please enter a numeric input for rate!")
                
        except:
            print("Error, please enter a numeric input for hours!")
        

    return hours, rate

# --------------------------------------------------------------------------

def compute_pay(hours, rate):
    """
    This function computes the overall pay (including the overtime)
    """

    # Calculate pay
    pay = hours * rate

    # Overtime condition (the rate would be 50% more)
    if hours > OVERTIME:
        pay += (hours - OVERTIME) * ((OVERTIME_FACTOR - 1) * rate)
    
    return pay

# --------------------------------------------------------------------------

def print_output(pay):
    """
    This function prints the total pay
    """
    # Output for the user
    
    print("Your gross pay is", round(pay , PRECISION), "dollars.")
    
# --------------------------------------------------------------------------

def main():
    
    the_hours, the_rate = get_input()

    the_pay = compute_pay(the_hours, the_rate)

    print_output(the_pay)
    
# --------------------------------------------------------------------------

main()

print("Done!")    



'''
Outputs:

Enter Hours: 42
Enter Rate: 17.25
Your gross pay is 741.75 dollars.
Done!

---------------------------------------------------

Enter Hours: 23
Enter Rate: five
Error, please enter a numeric input for rate!
Enter Hours: 
Error, please enter a numeric input for hours!
Enter Hours: fifty
Error, please enter a numeric input for hours!
Enter Hours: -17
Enter Rate: 12.25
Please enter positive numbers!
Enter Hours: 23.3333
Enter Rate: 19.7777
Your gross pay is 461.48 dollars.
Done!

'''
