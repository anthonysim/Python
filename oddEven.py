# Odd and Even

def showNumber(number):
    for i in range(number + 1):
        if i % 2 == 0:
            print(str(i) + " EVEN")
        else:
            print(str(i) + " ODD")

showNumber(10)
