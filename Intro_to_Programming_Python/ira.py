"""
Chapter 3, pg 140-141, Individual Retirement Accounts

Earl and Larry each begin full-time jobs in Jan 2015 and plan to retire 
in Jan 2063 after working for 48 years. 

4% interest compounded annually. 

Earl opens a traditional IRA account deposits $5000 into his account at the 
end of each year for 15 years. After that he plans to make no further deposits 
and just let the money earn interest. Larry plans to wait 15 years before 
opening his traditional IRA and then deposit $5000 into the account at the 
end of each year until he retires. Write a program that calculated the amount 
of money each person has deposited into his account and the amount of money in 
each account upon retirement.
"""
# Earl's Analysis
rate = 1.04
balance = 0
deposit = 0
year = 1

while year < 16:
	deposit += 5000
	balance += 5000
	balance *= rate
	year += 1
print()
print("Earl's Deposits:\n${0:,.2f}".format(deposit))

while year < 48:
	balance *= rate
	year += 1
print()
print("Earl's Amounts in IRA Upon Retirement:\n${0:,.2f}".format(balance))

# Larry's Analysis
rate = 1.04
balance = 0
deposit = 0
year = 1

while year < 34:
	deposit += 5000
	balance += 5000
	if year == 33:
		break
	balance *= rate
	year += 1
print()
print("Larrys's Deposits:\n${0:,.2f}".format(deposit))
print()
print("Larry's Amounts in IRA Upon Retirement:\n${0:,.2f}".format(balance))
