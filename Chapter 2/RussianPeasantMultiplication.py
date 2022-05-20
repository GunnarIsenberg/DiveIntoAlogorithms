import math
import pandas as pd

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

# The inverse operation of the above
doubling = [n2]
while(len(doubling) < len(halving)):
    doubling.append(max(doubling) * 2)

# This creates a hashmap like data structure from the two lists
half_double = pd.DataFrame(zip(halving, doubling))

# We are now going to sort out all even results from the table created above
half_double = half_double.loc[half_double[0] % 2 == 1, :]
answer = sum(half_double.loc[:, 1])

# What can be learned from this solution is that things as simple
# as multiplication can be solved in many different manners in order
# to focus on time or memory constraints.
