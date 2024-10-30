# Midterm - part 1
# Saba Feilizadeh
# A Menu-Driven Program for De Anza College Food Court


# Constants for prices
PRICES = {
    "price_1": 5.25,
    "price_2": 5.75,
    "price_3": 5.95,
    "price_4": 5.95,
    "price_5": 5.95,
}

# Cnstants for name of the burgers
BURGERS = {
    "burger_1": "De Anza Burger ",
    "burger_2": "Bacon Cheese   ",
    "burger_3": "Mushroom Swiss ",
    "burger_4": "Western Burger ",
    "burger_5": "Con Cali Burger",
}

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
    print("1.", BURGERS["burger_1"], "................... $", price_1)
    print("2.", BURGERS[burger_2], "................... $", price_2)
    print("3.", BURGERS[burger_3], "................... $", price_3)
    print("4.", BURGERS[burger_4], "................... $", price_4)
    print("5.", BURGERS[burger_5], "................... $", price_5)
    print("6. Exit")
    print("---------------------------------------------")

# --------------------------------------------------------------------------

def get_inputs():
    
    """
    This function gets the user's order
    """

    # Define a dictionary for the order quantity
    orders = {
        "quantity_1": 0,
        "quantity_2": 0,
        "quantity_3": 0,
        "quantity_4": 0,
        "quantity_5": 0,
    }

    # Get the order and the quantity from the user (also validate inputs)
    try:
        order = int(input("Please enter a number between 1 to 5 to select your order.(or enter 6 to exit):  "))

        if order == 6:
            print("Have a nice day!")
            
        elif order >= 1 and order < 6:
            choice = "BURGER_" + order
                
            quantity = int(input( "How many of", choice, "would you like to order? "))

            # Set the correct quantity for the order
            orders["quantity_" + quantity] += 1

            # Set the status of the user (student or staff)
            status = int(input("Are you a student? (enter 1 for yes, 0 for no): "))
                
        else:
            print("Please enter a valid option from the menu!")
                
    except:
        print("Error, please enter a numeric input!")
        

    return orders, status

# --------------------------------------------------------------------------

def compute_bill(orders, status):
    """
    This function computes the total amount the user has to pay
    """

    # Calculate bill
    bill_before_tax = 0

    for i in range(5):
        bill_before_tax += orders["quantity_" + str(i)] * (PRICE_ + i)

    bill_after_tax = bill_before_tax * status * (1 + TAX)

    return bill_before_tax, bill_after_tax

# --------------------------------------------------------------------------

def print_bill(orders, status, bill_before_tax, bill_after_tax):
    """
    This function prints the total amount the user has to pay
    """
    print("---------------------------------------------")
    print(" << ----------- Your Bill ----------- >>   \n")

    for i in range(5):
        if orders["quantity_" + i] != 0:
            
            print("1.", BURGER_1, "................... $", PRICE_1)
    
    print("1.", BURGER_1, "................... $", PRICE_1)
    print("2.", BURGER_2, "................... $", PRICE_2)
    print("3.", BURGER_3, "................... $", PRICE_3)
    print("4.", BURGER_4, "................... $", PRICE_4)
    print("5.", BURGER_5, "................... $", PRICE_5)
    print("6. Exit")
    print("---------------------------------------------")
    
    print("Your bill is $", round(bill , PRECISION))
    
# --------------------------------------------------------------------------

def main():
    
    show_menu()

    orders, status = get_inputs()

    bill_before_tax, bill_after_tax = compute_bill(orders, status)

    print_bill(orders, status, bill_before_tax, bill_after_tax)
    
# --------------------------------------------------------------------------

main()

print("Done!")    



'''
Outputs:

---------------------------------------------------


'''
