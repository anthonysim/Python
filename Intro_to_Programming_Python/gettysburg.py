"""
Gettyburg Address

File: Gettysburg.txt
a) code that displays the first 89 characters of the Gettysburg Adress,
b) the number of words in the Gettysburg Address, and
c) the number of different words.
"""

infile = open("Gettysburg.txt", 'r')
print()

for line in infile:
	print(line[0:89])
	line = line.lower()
	words = line.split()
	print("The Gettysburg Address contains", len(words), "words.")
	
	setList = list()
	for word in words:
		word = word.replace(",", "")
		word = word.replace(".", "")
		word = word.replace(":", "")
		setList.append(word)
	setList = set(setList)
	print("The Gettysburg address contains", len(setList), "different words.")

infile.close()
