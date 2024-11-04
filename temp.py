# Midterm - part 1
# Saba Feilizadeh
# A Menu-Driven Program for De Anza College Food Court


# A list for prices
PRICES = [5.25, 5.75, 5.95, 5.95, 5.95]

# A list for name of the burgers
BURGERS = ["De Anza Burger",
           "Bacon Cheese",
           "Mushroom Swiss",
           "Western Burger",
           "Con Cali Burger"
           ]

# Constant for tax (only for staff)
TAX = 0.09

# Constant for the floating point precision
PRECISION = 2

# Define column widths for the tables in the output
ITEM_WIDTH = 20
QTY_WIDTH = 12
PRICE_WIDTH = 12
TOTAL_WIDTH = 12
LINE_WIDTH = ITEM_WIDTH + QTY_WIDTH + PRICE_WIDTH + TOTAL_WIDTH + 5

# --------------------------------------------------------------------------

def show_menu():
    """
    This function displays the menu to the user
    """
    print("-" * LINE_WIDTH)
    print("<<" + "-" * ((LINE_WIDTH - 29) // 2) + " De Anza Food Court Menu " + "-" * ((LINE_WIDTH - 29) // 2)+ ">>\n")
    print("1.", BURGERS[0], "." * (LINE_WIDTH - len(BURGERS[0]) - len(str(PRICES[0])) - 7), "$", PRICES[0])
    print("2.", BURGERS[1], "." * (LINE_WIDTH - len(BURGERS[1]) - len(str(PRICES[1])) - 7), "$", PRICES[1])
    print("3.", BURGERS[2], "." * (LINE_WIDTH - len(BURGERS[2]) - len(str(PRICES[2])) - 7), "$", PRICES[2])
    print("4.", BURGERS[3], "." * (LINE_WIDTH - len(BURGERS[3]) - len(str(PRICES[3])) - 7), "$", PRICES[3])
    print("5.", BURGERS[4], "." * (LINE_WIDTH - len(BURGERS[4]) - len(str(PRICES[4])) - 7), "$", PRICES[4])
    print("6. Exit")
    print("-" * LINE_WIDTH)

# --------------------------------------------------------------------------

def get_inputs():
    
    """
    This function gets the user's order and the status
    """

    # A list for the quantity of each item
    quantities = [0, 0, 0, 0, 0]

    # Staff or student status
    status = -1

    # Flag to check if user wants to order (doesn't enter 6 at the beginning)
    wants_to_order = False

    # Get the order and the quantity from the user and validate inputs
    while True:
        try:
            user_choice = int(input("What would you like to order?\n(Enter a number between 1 to 5 to select your order or enter 6 to exit):  "))
            if user_choice == 6:
                break

            elif 1 <= user_choice <= 5:
                wants_to_order = True
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
            
        print("-" * LINE_WIDTH)

    print("-" * LINE_WIDTH)
    
    # Get the status of the user
    while wants_to_order and status != 1 and status != 0:
        try:
            # Set the status of the user (student or staff)
            status = int(input("Are you a staff or a student? (enter 1 for staff, 0 for student): "))

            # Validate the status
            if status != 1 and status != 0:
                print("Please enter a valid option for your status!")
        except:
            print("Error, please enter a numeric input!")

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

    # Calculate the bill after tax
    bill_after_tax = bill_before_tax + bill_before_tax * status * TAX

    return bill_before_tax, bill_after_tax

# --------------------------------------------------------------------------

def print_bill(quantities, status, bill_before_tax, bill_after_tax):
    """
    This function prints the total amount the user has to pay
    """

    print("\n" +"*" * LINE_WIDTH)
    print("<<" + "-" * ((LINE_WIDTH - 15) // 2) + " Your Bill " + "-" * ((LINE_WIDTH - 15) // 2) + ">>\n")

     # Print header with fixed widths
    print(f"{'Item':<{ITEM_WIDTH}} {'Quantity':<{QTY_WIDTH}} {'Price':<{PRICE_WIDTH}} {'Total':<{TOTAL_WIDTH}}")
    print("-" * LINE_WIDTH)

    # Print items with fixed widths
    for i in range(5):
        if quantities[i] != 0:
            print(f"{BURGERS[i]:<{ITEM_WIDTH}} {quantities[i]:<{QTY_WIDTH}} ${round(PRICES[i], PRECISION):<{PRICE_WIDTH-1}} ${round(PRICES[i] * quantities[i], PRECISION):<{TOTAL_WIDTH-1}}")
    
    print("-" * LINE_WIDTH)
    print(f"{'Bill before tax:':>{(LINE_WIDTH // 2)}}   ${round(bill_before_tax, PRECISION):<{PRICE_WIDTH}}")
    print(f"{'Tax:':>{(LINE_WIDTH // 2)}}   ${round(bill_after_tax - bill_before_tax, PRECISION):<{PRICE_WIDTH}}")
    print(f"{'Bill after tax:':>{(LINE_WIDTH // 2)}}   ${round(bill_after_tax, PRECISION):<{PRICE_WIDTH}}")
    print(f"{'Total:':>{(LINE_WIDTH // 2)}}   ${round(bill_after_tax, PRECISION):<{PRICE_WIDTH}}")
    print("*" * LINE_WIDTH)
    
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
=============================================================
Output 1:
=============================================================

-------------------------------------------------------------
<<---------------- De Anza Food Court Menu ---------------->>

1. De Anza Burger .................................... $ 5.25
2. Bacon Cheese ...................................... $ 5.75
3. Mushroom Swiss .................................... $ 5.95
4. Western Burger .................................... $ 5.95
5. Con Cali Burger ................................... $ 5.95
6. Exit
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  6
-------------------------------------------------------------
Done!

=============================================================
Output 2:
=============================================================

-------------------------------------------------------------
<<---------------- De Anza Food Court Menu ---------------->>

1. De Anza Burger .................................... $ 5.25
2. Bacon Cheese ...................................... $ 5.75
3. Mushroom Swiss .................................... $ 5.95
4. Western Burger .................................... $ 5.95
5. Con Cali Burger ................................... $ 5.95
6. Exit
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  3
How many of Mushroom Swiss would you like to order? 5
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  1
How many of De Anza Burger would you like to order? 2
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  5
How many of Con Cali Burger would you like to order? 4
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  6
-------------------------------------------------------------
Are you a staff or a student? (enter 1 for staff, 0 for student): 1

*************************************************************
<<----------------------- Your Bill ----------------------->>

Item                 Quantity     Price        Total       
-------------------------------------------------------------
De Anza Burger       2            $5.25        $10.5       
Mushroom Swiss       5            $5.95        $29.75      
Con Cali Burger      4            $5.95        $23.8       
-------------------------------------------------------------
              Bill before tax:   $64.05       
                          Tax:   $5.76        
               Bill after tax:   $69.81       
                        Total:   $69.81       
*************************************************************
Done!

=============================================================
Output 3:
=============================================================

-------------------------------------------------------------
<<---------------- De Anza Food Court Menu ---------------->>

1. De Anza Burger .................................... $ 5.25
2. Bacon Cheese ...................................... $ 5.75
3. Mushroom Swiss .................................... $ 5.95
4. Western Burger .................................... $ 5.95
5. Con Cali Burger ................................... $ 5.95
6. Exit
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  de anza
Error, please enter a numeric input!
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  -9
Please enter a valid option from the menu!
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  0
Please enter a valid option from the menu!
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  1
How many of De Anza Burger would you like to order? two
Please enter a numeric value!
How many of De Anza Burger would you like to order? -1
Please enter a positive number!
How many of De Anza Burger would you like to order? 2
-------------------------------------------------------------
What would you like to order?
(Enter a number between 1 to 5 to select your order or enter 6 to exit):  6
-------------------------------------------------------------
Are you a staff or a student? (enter 1 for staff, 0 for student): staff
Error, please enter a numeric input!
Are you a staff or a student? (enter 1 for staff, 0 for student): -3
Please enter a valid option for your status!
Are you a staff or a student? (enter 1 for staff, 0 for student): 7
Please enter a valid option for your status!
Are you a staff or a student? (enter 1 for staff, 0 for student): 0

*************************************************************
<<----------------------- Your Bill ----------------------->>

Item                 Quantity     Price        Total       
-------------------------------------------------------------
De Anza Burger       2            $5.25        $10.5       
-------------------------------------------------------------
              Bill before tax:   $10.5        
                          Tax:   $0.0         
               Bill after tax:   $10.5        
                        Total:   $10.5        
*************************************************************
Done!




'''
