import numpy as np
from bitstring import BitArray

def part1():

    total_bit_counts = []
    num_inputs = 0

    with open( 'input.txt', 'r+' ) as f:

        tmp = f.readline().strip()
        total_bit_counts = np.array( [int(x) for x in list(tmp)] )
        num_inputs = 1

        for line in f:

            tmp = line.strip()
            tmp = np.array( [int(x) for x in list(tmp)] )
            total_bit_counts = np.add( total_bit_counts, tmp )
            num_inputs += 1


    result = total_bit_counts.astype( float )
    result = result / num_inputs
    gamma = [1 if b > 0.5 else 0 for b in result]
    epsilon = [1 if b < 0.5 else 0 for b in result]

    gamma_ba = BitArray( gamma )
    epsilon_ba = BitArray( epsilon )

    print( gamma_ba.uint )
    print( epsilon_ba.uint )

    print( gamma_ba.uint * epsilon_ba.uint )


"""
Base case:
    1 element: return the element

Returns:
    The bit determined by bit criteria
"""
def part2_o2_helper( o2_arr, bit_pos ):

    # Base case: 1 element / 1 bit
    if len( o2_arr ) == 1:
        return o2_arr[0]

    # Sum up the column, and divide by num_inputs
    col_sum = np.sum( o2_arr[:,bit_pos] ) / len( o2_arr )

    # Bit criteria - MOST COMMON, or 1 if tied.
    o2_bit = 1 if col_sum >= 0.5 else 0

    # Create new set for O2 entries. Remove (from original input) elements that
    # don't follow the rule.
    o2_arr = np.array( [x for x in o2_arr if x[bit_pos] == o2_bit] )

    return part2_o2_helper( o2_arr, bit_pos + 1 )


"""
Base case:
    1 element: return the element

Returns:
    The bit determined by bit criteria
"""
def part2_co2_helper( co2_arr, bit_pos ):

    # Base case: 1 element / 1 bit
    if len( co2_arr ) == 1:
        return co2_arr[0]

    # Sum up the column, and divide by num_inputs
    col_sum = np.sum( co2_arr[:,bit_pos] ) / len( co2_arr )

    # Bit criteria - LEAST COMMON, or 0 if tied.
    co2_bit = 0 if col_sum >= 0.5 else 1

    # Create new set for CO2 entries. Remove (from original input) elements that
    # don't follow the rule.
    co2_arr = np.array( [x for x in co2_arr if x[bit_pos] == co2_bit] )

    return part2_co2_helper( co2_arr, bit_pos + 1 )


def part2():

    # Need to read whole file into memory
    all_bits = []

    with open( 'input.txt', 'r+' ) as f:
        for line in f:
            tmp = line.strip()
            all_bits.append( [int(x) for x in list(tmp)] )

    all_bits = np.array( all_bits ).astype( float )

    # Calculate O2 and CO2 ratings recursively
    o2_rating = part2_o2_helper( all_bits, 0 )
    co2_rating = part2_co2_helper( all_bits, 0 )

    # Convert to decimal and multiply together
    o2_ba = BitArray( o2_rating )
    co2_ba = BitArray( co2_rating )

    print( o2_ba.uint )
    print( co2_ba.uint )
    print( 'Life Support Rating: ' + str( o2_ba.uint * co2_ba.uint ) )


part1()
part2()
