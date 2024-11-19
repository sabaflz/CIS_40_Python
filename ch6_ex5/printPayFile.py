# Ch.6, Ex.5
# Saba Feilizadeh
# This module prints the pay stub.

# Constant for the width of the line for the output
LINE_WIDTH = 30
HEADER = (LINE_WIDTH - len("Pay Stub")) // 4

# Constant for the floating point precision
PRECISION = 2
# --------------------------------------------------------------------------
def printPay(data):
    print("-" * LINE_WIDTH)
    print("-" * (HEADER),"Pay Stub","-" * (HEADER))
    print(f"Company: {data['company']}")
    print(f"Hourly Rate: ${round(data['rate'],PRECISION)}")
    print(f"Hours Worked: {round(data['hours'],PRECISION)}")
    print(f"Total Pay:   ${round(data['total_pay'],PRECISION)}")
    print("-" * LINE_WIDTH)
 