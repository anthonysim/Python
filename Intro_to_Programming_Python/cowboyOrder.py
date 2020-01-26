"""
Cowboy Order
1) Create a file with the list '3', '2', '10', '1', '4' named Orders.txt.
2) Take the list of items in Cowboy.txt and calculate the list of items purchased
and calculate how much each item will cost plus the grand total.

Use Cowboy.txt
"""

def main():
	file = "Cowboy.txt"	
	cowboy = getData(file)

	outfile = open("Orders.txt", 'w')
	orders = createFile(outfile)

	order(cowboy, orders)

def getData(file):
	infile = open(file, 'r')
	cowboy = [line.rstrip().split(',') for line in infile]
	infile.close()
	
	for i in range(len(cowboy)):
		cowboy[i][1] = eval(cowboy[i][1])

	return cowboy

def createFile(outfile):
	orderAmts = ['3', '2', '10', '1', '4']

	for i in range(len(orderAmts)):
		orderAmts[i] = 	orderAmts[i] + "\n"

	outfile.writelines(orderAmts)
	outfile.close()

	infile = open("Orders.txt", 'r')
	orders = [line.rstrip() for line in infile]
	infile.close()

	for i in range(len(orders)):
		orders[i] = eval(orders[i])

	return orders

def order(cowboy, orders):
	total = 0
	for i in range(5):
		print(str(orders[i]) + " " + str(cowboy[i][0]) + ": ", end='')
		print("${0:,.2f}".format(orders[i] * cowboy[i][1]))
		total += (orders[i] * cowboy[i][1])	
	print("TOTAL: ${0:,.2f}".format(total))

main()
