# A function that takes the min and max then fills in the numbers in between.

def arrayFromRange(min, max):
    output = []

    for i in range(min, max + 1):
        print(i)
        output.append(i)
    print(output)

arrayFromRange(1, 4)