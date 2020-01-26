"""
Top Hitters

A program to show the batting averages of the 3 baseball players.
"""

def main():
	topHitters = {"Gehrig":{"atBats":8061, "hits":2721},
		     "Ruth":{"atBats":8399, "hits":2873},
		     "Williams":{"atBats":7706, "hits":2654},}

	battingAverages(topHitters)

def battingAverages(topHitters):
	for hitter in topHitters:
		print("{0:10}{1:,.3f}".format(hitter, topHitters[hitter]["hits"] / topHitters[hitter]["atBats"]))

main()
