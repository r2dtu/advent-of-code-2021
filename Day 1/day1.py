"""
Day 1 Solution
"""

prev_m = 32767
current_m = 0

num_inc = 0

with open( 'input.txt', 'r+' ) as f:

    for line in f.readlines():
        current_m = int( line )

        if current_m > prev_m:
            num_inc += 1

        prev_m = current_m

print( 'Answer: ' + str( num_inc ) )

"""
Day 1, Part 2 Solution
"""
from itertools import islice

WINDOW_SIZE = 3

# Each "m" is now sum of WINDOW_SIZE "m"'s
prev_m = [ 32767 ] * WINDOW_SIZE
current_m = [ 32767 ] * WINDOW_SIZE

num_inc = 0

with open( 'input.txt', 'r+' ) as f:

    for line in f.readlines():
        current_m[-1] = int( line )

        if sum( current_m ) > sum( prev_m ):
            num_inc += 1

        prev_m = current_m
        current_m = current_m[1:] + current_m[-1:]

print( 'Answer: ' + str( num_inc ) )
