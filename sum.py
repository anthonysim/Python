# A function that adds up the total for
# multiples of 5 and 3.

# Number limit is set within the function.

def sum(limit):
    total = 0
    
    for i in range(1, limit +1):
        if i % 5 == 0 or i % 3 == 0:
            total += i

    return total

print(sum(10))
