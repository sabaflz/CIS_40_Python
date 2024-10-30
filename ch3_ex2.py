# Ch.3, Ex.2
# Saba Feilizadeh
# Calculate the overtime if the hours is greater than 40 per week
# Overtime rate 1.5

hours = float(input("Enter Hours: "))

rate = float(input("Enter Rate: "))

# Calculate pay
pay = hours * rate

# Overtime condition (the rate would be 50% more)
if hours > 40:
    pay += (hours - 40) * (0.5 * rate)



print("Pay: ", pay)

print("Done!")


'''
Outputs:

Enter Hours: 37
Enter Rate: 24.25
Pay:  897.25
Done!

------------------

Enter Hours: 42
Enter Rate: 17.25
Pay:  741.75
Done!

'''
