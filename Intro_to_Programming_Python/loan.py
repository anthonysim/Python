# Loan Calculator Function

def main():
	(loan, RATE, MONTHS) = getData()

	payments = monthlyPayments(loan, RATE, MONTHS)
	
	totalInterest = paymentDetails(payments, loan, RATE, MONTHS)
	
	printDetails(totalInterest, payments, loan)

def getData():
	loan = eval(input("Enter the amount of the loan:\t"))
	RATE = eval(input("Enter the interest RATE:\t"))
	RATE = (RATE / 12) * 0.01
	MONTHS = eval(input("Enter the duration in months:\t"))
	return (loan, RATE, MONTHS)

def monthlyPayments(loan, RATE, MONTHS):
	payments = (loan * RATE) / (1 - (1 + RATE) ** -MONTHS)
	return payments

def paymentDetails(payments, loan, RATE, MONTHS):
	print()
	totalInterest = 0
	for i in range(MONTHS):
		intPaid = loan * RATE
		totalInterest += intPaid
		principal = payments - intPaid
		loan = loan - payments + intPaid
		print("Payment No:", i + 1)
		print("***************")
		print("Principal: ${0:,.2f}".format(principal))
		print("Interest:  ${0:,.2f}".format(intPaid))
		print("Balance:   ${0:,.2f}".format(loan))
		print()
	return totalInterest
	
def printDetails(totalInterest, payments, loan):
	print("Monthly Payments:    ${0:,.2f}".format(payments))
	print("Total Amount Paid:   ${0:,.2f}".format(totalInterest + loan))
	print("Total Interest Paid: ${0:,.2f}".format(totalInterest))
	
main()
