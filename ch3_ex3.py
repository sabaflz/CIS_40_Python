# Ch.3, Ex.3
# Saba Feilizadeh
# Calculate the overtime if the hours is greater than 40 per week
# Overtime rate 1.5
# Handle the non-numeric inputs



try:
    hours = float(input("Enter Hours: "))

    try:
        rate = float(input("Enter Rate: "))
    
        if hours >= 0 and rate >= 0:

            # Calculate pay
            pay = hours * rate

            # Overtime condition (the rate would be 50% more)
            if hours > 40:
                pay += (hours - 40) * (0.5 * rate)


            print("Pay: ", pay)
            
        else:
            print("Please enter positive numbers!")
            
    except:
        print("Error, please enter a numeric input for rate!")
    
except:
    print("Error, please enter a numeric input for hours!")

print("Done!")


'''
Outputs:

Enter Hours: 42
Enter Rate: 17.25
Pay:  741.75
Done!

------------------

Enter Hours: 23
Enter Rate: five
Error, please enter a numeric input for rate!
Done!

------------------

Enter Hours: fifty
Error, please enter a numeric input for hours!
Done!

------------------

Enter Hours: -17
Enter Rate: 12.25
Please enter positive numbers!
Done!

'''
