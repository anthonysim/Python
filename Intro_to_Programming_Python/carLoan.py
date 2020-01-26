"""
Chapter 3, Page 139, Car Loan Program 

This is a program written in Python to find out the Monthly Payment and Total Interest Paid for a Loan.
This program also figures out the Principal, Interest Paid, and Balance amount for each payment.
"""

loan = eval(input("Enter the amount of the loan: "))
rate = eval(input("Enter the interest rate: "))
months = eval(input("Enter the duration in months: "))

rate = (rate / 12) * 0.01
monthlyPay = (loan * rate) / (1 - (1 + rate) ** -months)
interest = (months * monthlyPay) - loan

print()
print("Monthly payment:     ${0:,.2f}".format(monthlyPay))
print("Total interest paid: ${0:,.2f}".format(interest))

for i in range(1, months + 1):
	intPaid = loan * rate
	principal = monthlyPay - intPaid
	loan = loan - monthlyPay + intPaid
	print()
	print("Payment:  ", i) 
	print()
	print("Monthly \nPayment:   ${0:,.2f}".format(monthlyPay))
	print("Principal: ${0:,.2f}".format(principal))
	print("Interest:  ${0:,.2f}".format(intPaid))
	print("Balance:   ${0:,.2f}".format(loan))
	print()
