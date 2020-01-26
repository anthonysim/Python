#Assignment 2 Functions
#Student: Anthony Sim

def to_number(str):
    integer = int(str)
    return integer


def add_two(n1, n2):
	added = n1 + n2
	return added


def cube(n):
	cubed = (n **3)
	return cubed

print(cube((add_two(to_number('7'), to_number('6')))))
