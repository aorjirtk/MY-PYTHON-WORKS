name = str(input('Enter Employee name: '))
hours_worked = float(input('Enter the number of hours worked: '))
hourly_rate = float(input('Enter the hourly pay rate: '))
withholding_tax_rate = float(input('Enter the federal withholding tax rate: '))
state_tax_rate = float(input('Enter the state withholding tax rate: '))

gross_pay = hourly_rate * hours_worked
tax = withholding_tax_rate * gross_pay
state_tax = state_tax_rate * gross_pay
deductions = state_tax + tax
net_pay = gross_pay - deductions

print('Mr',name)
print('Hours worked:',hours_worked)
print('Pay Rate:',hourly_rate)
print('Gross pay:',gross_pay)

print('Deductions:')
print('Federal withholding (20.0%):',tax)
print('total deductions:',deductions)
print('Net Pay:',net_pay)
