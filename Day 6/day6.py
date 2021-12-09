import numpy as np

NUM_DAYS = 50

with open( 'input.txt', 'r' ) as f:

    timers = f.readline().strip().split( ',' )
    timers = np.array( timers ).astype( int )

timers = np.array( [3] )
for day in range( NUM_DAYS ):
    new_fish_timers = np.array( [] )

    for i, t in enumerate( timers ):
        if t == 0:
            # Reset to 7 (instructions say 6, but we're decrementing after)
            timers[i] = 7

            # Add new timer
            new_fish_timers = np.append( new_fish_timers, 8 )

    timers = timers - 1

    if len( new_fish_timers ) > 0:
        timers = np.concatenate( (timers, new_fish_timers) )

    print( timers )

print( len( timers ) )

# Note: The above takes absurdly long (exponential) as NUM_DAYS increases
# We can rather, calculate the number of offspring based on the current
# starting state.
#
# For example, if the initial state is 3, after 4 days, it will be back at 6, 
# with 1 offspring. After 11 days (7 more), it will be back at 6, with one
# more offspring.
#
# The relationship between internal timers of parent and offspring is 2. In
# other words, the offspring with have another offspring 2 days after the parent
# did.

num_offspring = ((6 - initial_state) + NUM_DAYS) / 7

# For new offspring, it takes 8 days to make another offspring.

"""
0    3
1    2
2    1
3    0
4    6,8                            4 days: 1
5    5,7                            11 days: 2
6    4,6                            13 days: 3
7    3,5                            18 days: 4
8    2,4                            20 days: 6
9    1,3                            22 days: 7
10   0,2
11   6,1,8
12   5,0,7
13   4,6,6,8
14   3,5,5,7
15   2,4,4,6
16   1,3,3,5
17   0,2,2,4
18   6,1,1,3,8
"""


num_offspring = ((6 - initial_state) + NUM_DAYS) / 7
num_offspring = ((6 - 8) + NUM_DAYS - birth_day) / 7

initial_bday = initial_state + 1
future_bdays = initial_bday + 7

