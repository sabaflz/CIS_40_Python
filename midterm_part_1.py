# Midterm - part 1
# Saba Feilizadeh
# A Menu-Driven Program for De Anza College Food Court


# A list for prices
PRICES = [5.25, 5.75, 5.95, 5.95, 5.95]

# A list for name of the burgers
BURGERS = ["De Anza Burger", "Bacon Cheese",
           "Mushroom Swiss", "Western Burger",
           "Con Cali Burger"]

# Constant for tax (for staff)
TAX = 0.09

# Constant for the floating point precision
PRECISION = 2

# --------------------------------------------------------------------------

def show_menu():
    """
    This function displays the menu to the user
    """
    print("---------------------------------------------")
    print(" << ----- De Anza Food Court Menu ----- >>   \n")
    print("1.", BURGERS[0], ".................... $", PRICES[0])
    print("2.", BURGERS[1], "...................... $", PRICES[1])
    print("3.", BURGERS[2], ".................... $", PRICES[2])
    print("4.", BURGERS[3], ".................... $", PRICES[3])
    print("5.", BURGERS[4], "................... $", PRICES[4])
    print("6. Exit")
    print("---------------------------------------------")

# --------------------------------------------------------------------------

def get_inputs():
    
    """
    This function gets the user's order
    """

    # A list for the quantity of each item
    quantities = [0, 0, 0, 0, 0]

    # Get the order and the quantity from the user and validate inputs
    user_choice = int(input("What would you like to order?\n(Enter a number between 1 to 5 to select your order or enter 6 to exit):  "))
    if user_choice == 6:
        status = -1
        print("*********************************************")
        print("Have a nice day!")
        print("*********************************************")

    else:

        while user_choice != 6:
            print("---------------------------------------------")
            try:
                user_choice = int(input("What would you like to order?\n(Enter a number between 1 to 5 to select your order or enter 6 to exit):  "))
                    
                if user_choice >= 1 and user_choice < 6:

                    item_index = user_choice - 1

                    flag = True
                    while flag:
                        try:
                            item_quantity = int(input(f"How many of {BURGERS[item_index]} would you like to order? "))

                            if item_quantity <= 0:
                                print("Please enter a positive number!")

                            else:
                                # Set the correct quantity for the order
                                quantities[item_index] += item_quantity

                                flag = False
                        except:
                            print("Please enter a numeric value!")
                        
                else:
                    print("Please enter a valid option from the menu!")
                        
            except:
                print("Error, please enter a numeric input!")
        
        try:
            # Set the status of the user (student or staff)
            status = int(input("Are you a staff or a student? (enter 1 for staff, 0 for student): "))
            while status != 1 and status != 0:
                print("Please enter a valid option for your status!")
                status = int(input("Are you a staff or a student? (enter 1 for staff, 0 for student): "))
        except:
            print("invalid input for status!")

    return quantities, status

# --------------------------------------------------------------------------

def compute_bill(quantities, status):
    """
    This function computes the total amount the user has to pay
    """

    # Calculate bill
    bill_before_tax = 0

    for i in range(5):
        bill_before_tax += quantities[i] * PRICES[i]

    bill_after_tax = bill_before_tax + bill_before_tax * status * TAX

    return bill_before_tax, bill_after_tax

# --------------------------------------------------------------------------

def print_bill(quantities, status, bill_before_tax, bill_after_tax):
    """
    This function prints the total amount the user has to pay
    """
    print("\n*********************************************")
    print("   << ----------- Your Bill ----------- >>   \n")

    for i in range(5):
        if quantities[i] != 0:
            print(f"{BURGERS[i]} * {quantities[i]}  ................... ${PRICES[i] * quantities[i]}")
    
    print("\n   Bill before tax  .................. $", round(bill_before_tax , PRECISION))
    print("   Bill after tax  ................... $", round(bill_after_tax , PRECISION))
    print("   Total  ............................ $", round(bill_after_tax , PRECISION))


    print("*********************************************\n")
    
# --------------------------------------------------------------------------

def main():
    
    show_menu()

    quantities, status = get_inputs()

    bill_before_tax, bill_after_tax = compute_bill(quantities, status)

    # Don't show the bill if they didn't order anything
    if sum(quantities) != 0:
        print_bill(quantities, status, bill_before_tax, bill_after_tax)
    
# --------------------------------------------------------------------------

main()

print("Done!")    



'''
Outputs:
---------------------------------------------
 << ----- De Anza Food Court Menu ----- >>   

1. De Anza Burger .................... $ 5.25
2. Bacon Cheese ...................... $ 5.75
3. Mushroom Swiss .................... $ 5.95
4. Western Burger .................... $ 5.95
5. Con Cali Burger ................... $ 5.95
6. Exit
---------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  6
*********************************************
Have a nice day!
*********************************************
Done!
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------




'''
