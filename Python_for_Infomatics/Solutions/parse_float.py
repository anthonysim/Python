# Assignment 3 - Looping, Searching, & Slicing
# File: parse_float.py
# Student: Anthony Sim

# Extract the float

avg_str = 'Average value read: 0.72903'

start = avg_str.find(':')
print(float(avg_str[start + 1:]))
