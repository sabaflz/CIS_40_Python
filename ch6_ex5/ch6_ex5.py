# Ch.6, Ex.5
# Saba Feilizadeh
# This program asks the user for company input, validates it,
# takes rate and hours, computes the pay (including overtime),
# and prints a pay stub.

from getInputsFile import getInputs
from computePayFile import computePay
from printPayFile import printPay

# --------------------------------------------------------------------------
def payProcess():
      '''
      This function processes all inputs, calculates the pay,
      and prints the pay stub.
      '''
      theDict = getInputs()
      theDict = computePay(theDict)
      printPay(theDict)

# --------------------------------------------------------------------------
if __name__ == '__main__':
      payProcess()
# --------------------------------------------------------------------------
print("Done!")

# --------------------------------------------------------------------------
'''
=============================================================
Output 1:
=============================================================
Enter your company name: Google
Enter your hourly rate: 17.25
Enter hours worked: 42
------------------------------
----- Pay Stub -----
Company: Google
Hourly Rate: $17.25
Hours Worked: 42.0
Total Pay:   $741.75
------------------------------
Done!

=============================================================
Output 2:
=============================================================
Enter your company name: APPLE
Enter your company name: apple
Invalid company name. Available companies are: ['Amazon', 'Apple', 'Facebook', 'Google', 'Uber']
Please choose from the list above: Apple
Enter your hourly rate: a
Invalid input. Please enter a numeric value.
Enter your hourly rate: -12
Rate must be a positive number.
Enter your hourly rate: 19.777
Enter hours worked: fifty
Invalid input. Please enter a numeric value.
Enter hours worked: -20
Hours must be a positive number.
Enter hours worked: 23.333
------------------------------
----- Pay Stub -----
Company: Apple
Hourly Rate: $19.78
Hours Worked: 23.33
Total Pay:   $461.46
------------------------------
Done!

'''