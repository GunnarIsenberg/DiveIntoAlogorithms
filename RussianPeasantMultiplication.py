import math

# We want to multiply these two numbers
n1 = 89
n2 = 18

# This is a list of descending values corresponding to column 1
# All of the halved values stemming from 89
halving = [n1]

# This loops until the most recent number is greater than 1
# It halves the values dropping any remainder
# Then appends the value to the end of the list representing our column

while(min(halving) > 1):
    halving.append(math.floor(min(halving)/2))
