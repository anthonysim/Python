""" 
Salary Options

Option 1: $1 / day for 10 days
or 
Option 2: $1 first day, then doubles per day until 10 days. 
"""

def main():
	first = option1()
	print("Option 1 pay: ${0:,.2f}".format(first))
	
	second = option2()
	print("Option 2 pay: ${0:,.2f}".format(second))

def option1():
	option1Pay = 0
	for i in range(10):
		option1Pay += 100
	return option1Pay

def option2():
	option2Pay = 1
	for i in range(10):
		option2Pay *=  2
	return option2Pay

main()
