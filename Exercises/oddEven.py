/* 
Odd Even. 

a function that iterates through, while specifying 
what number of the iteration is odd or even.
*/

def showNumber(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            print(str(i) + " EVEN")
        else:
            print(str(i) + " ODD")

showNumber(10)
