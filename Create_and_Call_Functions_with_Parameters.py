# Sergio Marquez, CIS261, Create and Call Functions with Parameters

def get_employee_name():
    name = input("Enter employee name: ")
    return name

def get_hours_worked():
    hours = float(input("Enter hours worked: "))
    return hours

def get_hourly_rate():
    rate = float(input("Enter hourly rate: "))
    return rate

def get_tax_rate():
    tax_rate = float(input("Enter income tax rate: "))
    return tax_rate

def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    tax = gross_pay * tax_rate
    net_pay = gross_pay - tax
    return gross_pay, tax, net_pay

def display_employee_info(name, hours, rate, gross_pay, tax_rate, tax, net_pay):
    print(f"Employee Name: {name}")
    print(f"Hours worked: {hours}")
    print(f"Hourly rate: {rate}")
    print(f"Gross pay: {gross_pay}")
    print(f"Income tax rate: {tax_rate}")
    print(f"Income tax: {tax}")
    print(f"Net pay: {net_pay}")

def display_totals(num_employees, total_hours, total_gross_pay, total_tax, total_net_pay):
    print("")
    print(f"Total number of employees: {num_employees}")
    print(f"Total hours worked: {total_hours}")
    print(f"Total gross pay: {total_gross_pay}")
    print(f"Total income tax: {total_tax}")
    print(f"Total net pay: {total_net_pay}")

num_employees = 0
total_hours = 0
total_gross_pay = 0
total_tax = 0
total_net_pay = 0

while True:
    print("")
    name = get_employee_name()
    if name.lower() == "end":
        break

    hours = get_hours_worked()
    rate = get_hourly_rate()
    tax_rate = get_tax_rate()
    gross_pay, tax, net_pay = calculate_pay(hours, rate, tax_rate)

    display_employee_info(name, hours, rate, gross_pay, tax_rate, tax, net_pay)

    num_employees += 1
    total_hours += hours
    total_gross_pay += gross_pay
    total_tax += tax
    total_net_pay += net_pay

display_totals(num_employees, total_hours, total_gross_pay, total_tax, total_net_pay)
