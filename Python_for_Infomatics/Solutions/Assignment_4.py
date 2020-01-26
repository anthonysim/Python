# Assignment 4: "Files, Lists, and Split"
# Student: Anthony Sim

fname = input("Please type in a filename: ")
substring = input("Please type in a substring: ")
fhand = open(fname)

line = fhand.read()
line_list = line.split()

script_list = list()
for item in line_list:
	lower_words = item.lower()
	if lower_words not in script_list:
		script_list.append(lower_words)
		script_list.sort()

def freq_count(word, substring):
	count = word.count(substring)
	print(word, count)

print()

for word in script_list:
	freq_count(word, substring)
