# Ch.6, Ex.5
# Saba Feilizadeh
# This module gets and validates user inputs.

# Company database
COMPANYLIST = ["Amazon", "Apple", "Facebook", "Google", "Uber"]

# --------------------------------------------------------------------------
def getInputs():
    # Validate company input
    attempts = 0
    while attempts < 2:
        company = input("Enter your company name: ")
        if company in COMPANYLIST:
            break
        attempts += 1
        if attempts == 2:
            print("Invalid company name. Available companies are:", COMPANYLIST)
            company = input("Please choose from the list above: ")

    # Validate rate input
    flag = True
    while flag:
        try:
            rate = float(input("Enter your hourly rate: "))
            if rate > 0:
                flag = False
            else:
                print("Rate must be a positive number.")
        except:
            print("Invalid input. Please enter a numeric value.")

    # Validate hours input
    flag = True
    while flag:
        try:
            hours = float(input("Enter hours worked: "))
            if hours > 0:
                break
            else:
                print("Hours must be a positive number.")
        except:
            print("Invalid input. Please enter a numeric value.")

    return {"company": company, "rate": rate, "hours": hours}