""" 
US Presidents

Takes the names, sorts the order by first name, then by last name.
From there, the last name is placed in front of the first name, then printed
"""

def main():
	names = [("Lyndon, Johnson"), ("John, Kennedy"), ("Andrew, Johnson")]

	names.sort(key=lambda name: name.split()[0])
	names.sort(key=lambda name: name.split()[1])

	for name in names:
		space = name.find(" ")
		print(name[space + 1:] + ", " + name[ : space-1])

main()
