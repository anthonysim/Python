"""
Academy Awards

 A program that displays the different film genres, 
 requests a genre as input, and then diplays the Oscar-winning films 
 of that genre.
 Use Oscars.txt
"""

def main():
	oscars = getData("Oscars.txt")
	print()
	
	genre = input("Enter a genre: ")
	genre = genre.lower()

	winners(oscars, genre)

def getData(f):
	infile = open(f, 'r')
	genres = [line.rstrip().split(',')[-1] for line in infile]	
	infile.close()

	genres = set(genres)
	genres = list(genres)
	genres.sort()
	print()

	print("The different film genres are as follows: ")
	for item in genres:
		print("   " + item)

	infile = open(f, 'r')
	oscars = [line.rstrip().split(',') for line in infile]	
	infile.close()

	return oscars

def winners(oscars, genre):
	for item in oscars:
		if item[1] == genre:
			print("   " + item[0])
		else:
			pass
	
main()