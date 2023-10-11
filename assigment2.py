def computepay(hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)

        if hours > 40:
            regular_pay = 40 * rate
            overtime_pay = (hours - 40) * rate * 1.5
            total_pay = regular_pay + overtime_pay
        else:
            total_pay = hours * rate

        return total_pay
    except ValueError:
        return "Error!!! Please enter numeric values."

try:
    hours = input("Enter the number of hours worked: ")
    rate = input("Enter the hourly rate: ")
    salary = computepay(hours, rate)

    if type(salary) == float:
        print(f"Salary: ${salary:.2f}")
    else:
        print(salary)
except KeyboardInterrupt:
    print("Program terminated.")
