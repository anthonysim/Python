""" 
Chapter 3, Page 140, Caffeine Absorption

After caffeine is absorbed into the body, 13% is eliminated from the body
each hour. Assume a person drinks an 8-oz cup of brewed coffee containing
130 mg of caffeine, and that the caffeine is absorbed immediately into the 
body. Write a program to calculate the following values:
 
a) the number of hours required until less than 65 mg (1/2 the original amount)
remain in the body.

b) the amount of caffeine in the body 24 hours after the person drinks the coffee.

c) Suppose the person drinks a cup of coffee at 7am and then drinks a cup of coffee 
at the end of the each hours until 7am the next day. How much caffeine will be in the 
body at the end of the 24 hours?
"""

caffeine = 130
absorption = 0.87
hours = 0
while caffeine > 65:
	caffeine *= absorption
	hours += 1	
print()
print("CAFFEINE VALUES")
print("One cup: less than 65 mg will remain after " + str(hours) + " hours.")

caffeine = 130
absorption = 0.87
for x in range(24):
	caffeine *= absorption
print("One cup: " + str(round(caffeine, 2)) + " will remain after 24 hours.")

caffeine = 130
absorption = 0.87
for y in range(24):
	caffeine *= absorption
	caffeine += 130
print("Hourly cups: " + str(round(caffeine,2)) + " mg will remain after 24 hours.")
