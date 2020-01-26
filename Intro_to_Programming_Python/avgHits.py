"""
Average Number of Hits

A program to shows the average number of hits by the 3 players.
"""

def main():
	topHitters = {"Gehrig":{"atBats":8061, "hits":2721},
		     "Ruth":{"atBats":8399, "hits":2873},
	      	     "Williams":{"atBats":7706, "hits":2654},}

	averageHits(topHitters)

def averageHits(topHitters):
	total = 0
	for hitter in topHitters:
		total += topHitters[hitter]["hits"]

	avgHits = total / len(topHitters)
	
	print("The average number of hits by")
	print("the baseball player was {0:.1f}".format(avgHits) + ".")

main()
