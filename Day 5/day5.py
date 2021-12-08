import numpy as np

vents_pos = np.zeros( (1000, 1000) )

with open( 'input.txt', 'r' ) as f:

    for line in f:
        # Parse the string: x1,y1 -> x2,y2
        endpoints = line.strip().split( " -> " )
        x1, y1 = endpoints[0].split( ',' )
        x1, y1 = int( x1 ), int( y1 )
        x2, y2 = endpoints[1].split( ',' )
        x2, y2 = int( x2 ), int( y2 )

        # Vertical line
        if x1 == x2:
            if y1 > y2:
                y2 -= 1
            else:
                y2 += 1

            for y in range( y1, y2, -1 if y1 > y2 else 1 ):
                vents_pos[y][x1] += 1

        # Horizontal line
        elif y1 == y2:
            if x1 > x2:
                x2 -= 1
            else:
                x2 += 1

            for x in range( x1, x2, -1 if x1 > x2 else 1 ):
                vents_pos[y1][x] += 1

        # Line is diagonal, but only consider if Part 2
        else:
            if y1 > y2:
                y2 -= 1
            else:
                y2 += 1

            if x1 > x2:
                x2 -= 1
            else:
                x2 += 1

            for y, x in zip( range( y1, y2, -1 if y1 > y2 else 1 ),
                             range( x1, x2, -1 if x1 > x2 else 1 ) ):
                vents_pos[y][x] += 1

# Find number of points that overlap at least 2
result = 0
for row in vents_pos:
    danger = [x for x in row if x >= 2]
    result += len( danger )

print( result )
