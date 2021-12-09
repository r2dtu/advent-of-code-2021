import numpy as np

with open( 'input.txt', 'r' ) as f:
    pos_arr = f.readline().strip().split( ',' )
    pos_arr = np.array( pos_arr ).astype( int )

pos_arr.sort()

# Find median
idx = 0
if len( pos_arr ) % 2 == 0:
    idx = len( pos_arr ) / 2
    median = (pos_arr[idx - 1] + pos_arr[idx]) / 2

else:
    idx = len( pos_arr ) / 2
    median = pos_arr[idx]

print( median )

# Calculate fuel cost. Get distance from each position.
final_pos = np.array( [median for _ in range( len(pos_arr) )] )

print( np.sum( np.abs( np.subtract( pos_arr, final_pos ) ) ) )
