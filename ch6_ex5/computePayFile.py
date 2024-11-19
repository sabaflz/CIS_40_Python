# Ch.6, Ex.5
# Saba Feilizadeh
# This module calculates the total pay, including overtime.

# A constant for the overtime hour limit
OVERTIME = 40

# Overtime rate factor
OVERTIME_FACTOR = 1.5
# --------------------------------------------------------------------------
def computePay(data):
    rate = data["rate"]
    hours = data["hours"]

    # Calculate regular and overtime pay
    if hours > OVERTIME:
        overtime_hours = hours - OVERTIME
        overtime_pay = overtime_hours * (rate * OVERTIME_FACTOR)
        regular_pay = OVERTIME * rate
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours * rate

    data["total_pay"] = total_pay
    return data 