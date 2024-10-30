# Ch.4, Ex.5
# Saba Feilizadeh
# Calculate the overtime pay for working more than 40 hours per week
# And validate user inputs

from random import randint

# A constant for the overtime hour limit
OVERTIME = 40

# Overtime rate factor
OVERTIME_FACTOR = 1.5

# Constant for the floating point precision
PRECISION = 2


# Loop untill user enters valid numbers

flag = True


while flag:
    try:
        companyName = input("Enter your company name: ").strip()        
            
        try:
            hours = float(input("Enter Hours: "))

            try:
                rate = float(input("Enter Rate: "))
                
                if hours <= 0 or rate <= 0:
                    print("Please enter positive numbers!")
                        
                else:
                        
                    # Calculate pay
                    pay = hours * rate

                    # Overtime condition (the rate would be 50% more)
                    if hours > OVERTIME:
                        pay += (hours - OVERTIME) * ((OVERTIME_FACTOR - 1) * rate)

                    # Output for the user
                    print("\n\nCompany: ", companyName)
                        
                    print("Hours: ", round(hours , PRECISION))

                    print("Rate: ", round(rate , PRECISION))

                    print("\n**************************\n")

                    # A random number between 1000 to 2000 for the document number
                    print("Your document number is: ", randint(1000 , 2000))
                        
                    print("Your", companyName, "gross pay is", round(pay , PRECISION), "dollars.")


                    flag = False
                        
            except:
                print("Error, please enter a numeric input for rate!")
                
        except:
            print("Error, please enter a numeric input for hours!")
                
    except:
            print("Error, something went wrong!")

print("Done!")


'''
Outputs:

Enter your company name:  Google
Enter Hours: 42
Enter Rate: 17.25


Company:  Google
Hours:  42.0
Rate:  17.25

**************************

Your document number is:  1537
Your Google gross pay is 741.75 dollars.
Done!

---------------------------------------------------

Enter your company name: Apple
Enter Hours: 23
Enter Rate: five
Error, please enter a numeric input for rate!
Enter your company name: Apple
Enter Hours: 
Error, please enter a numeric input for hours!
Enter your company name: Apple
Enter Hours: fifty
Error, please enter a numeric input for hours!
Enter your company name: Apple
Enter Hours: -17
Enter Rate: 12.25
Please enter positive numbers!
Enter your company name: Apple
Enter Hours: 23.333
Enter Rate: 19.777


Company:  Apple
Hours:  23.33
Rate:  19.78

**************************

Your document number is:  1812
Your Apple gross pay is 461.46 dollars.
Done!

---------------------------------------------------

Enter your company name:      Microsoft   
Enter Hours:   16
Enter Rate:           23.456


Company:  Microsoft
Hours:  16.0
Rate:  23.46

**************************

Your document number is:  1190
Your Microsoft gross pay is 375.3 dollars.
Done!

'''
