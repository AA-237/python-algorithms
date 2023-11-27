def calculate_salary(bookings, shifts):
    #  Getting  all the bookings done by the agent and seperating between residence and commercial
    residence_bookings = [booking for booking in bookings if booking['type'] == 'residence']
    commercial_bookings = [booking for booking in bookings if booking['type'] == 'commercial']

    #this bonus format is derived from the problem statement provided
    total_residence_bonus = calculate_bonus(residence_bookings, 20, 10, 5, 50)
    total_commercial_bonus = calculate_bonus(commercial_bookings, 5, 3, 1, 100)

    total_shifts = len(shifts)

    # Total_Salary = Total shift done by agent * 500 + (Total_Bonus)
    total_salary = total_shifts * 500 + total_residence_bonus + total_commercial_bonus

    return total_salary

def calculate_bonus(bookings, bonus1, bonus2, bonus3, base):
    length = len(bookings)
    result1 = length // bonus1
    remainder1 = length % bonus1
    if remainder1 > 0:
        result2 = remainder1 // bonus2
        remainder2 = remainder1 % bonus2
        if remainder2 > 0:
            result3 = remainder2 // bonus3
            remainder3 = remainder2 % bonus3
        else:
            result3 = remainder3 = 0
    else:
        result2 = result3 = remainder3 = 0

    total_bonus = bonus1 * result1 + bonus2 * result2 + bonus3 * result3 + remainder3 * base
    return total_bonus



# hard coded data use for testing
bookings = [
    {'type': 'residence'},
    {'type': 'residence'},
    {'type': 'residence'},
    {'type': 'residence'},
    {'type': 'residence'},
    {'type': 'residence'},
    {'type': 'commercial'},
    {'type': 'commercial'},
    {'type': 'commercial'},
    {'type': 'commercial'},
    {'type': 'commercial'},
    {'type': 'commercial'},
    {'type': 'commercial'},
    {'type': 'commercial'},
    {'type': 'commercial'},
]

shifts = ['morning', 'afternoon', 'morning', 'morning', 'morning', 'afternoon']

# Calculate salary
salary = calculate_salary(bookings, shifts)

print(f"The total salary for the month is {salary} XAF")
