# Sergio Marquez, CIS261, Create and Call Functions with Parameters

def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

def GetHoursWorked():
    hours = float(input("Enter hours worked: "))
    return hours

def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input("Enter income tax rate: "))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay):
    print("Name:  ", empname) 
    print("Hours Worked: ", f"{hours:,.2f}")
    print("Hourly Rate:  $", f"{hourlyrate:,.2f}")
    print("Gross Pay:  $", f"{grosspay:,.2f}")
    print("Tax Rate:  ", f"{taxrate:.1%}")
    print("Income Tax:  $", f"{incometax:,.2f}")
    print("Net Pay:  $", f"{netpay:,.2f}")
    print()

def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")
    print("Total Gross Pay:  $", f"{TotGrossPay:,.2f}")
    print("Total Tax:  $", f"{TotTax:,.1f}")
    print("Total Net Pay:  $", f"{TotNetPay:,.2f}")

if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay

    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)
