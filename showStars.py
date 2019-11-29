# A function that forms a "tree" based on
# the amount of rows specified.

def showStars(row):
    for i in range(1, row + 1):
        stars =  '*' * i
        print(stars)
        
showStars(5)
