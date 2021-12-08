from bitarray import bitarray

def unique_digits( d ):
    return len(d) == 2 or len(d) == 3 or len(d) == 4 or len(d) == 7

def part1():

    result = 0

    with open( 'input.txt', 'r' ) as f:

        for line in f:
            digits = line.strip().split()
            output = digits[digits.index( "|" ) + 1:]

            result += len( [1 for d in output if unique_digits( d )] )

    print( "Part 1: " + str( result ) )


"""
Segments will be stored in the following array index format:

 --          0
|  |       5   1
 --          6
|  |       4   2
 --          3
"""

def fill_1( opt_arr, clue ):
    for i in range( len(opt_arr) ):
        opt_arr[i][1] = clue[i % 2]
        opt_arr[i][2] = clue[(i + 1) % 2]


def fill_7( opt_arr, clue ):
    # Need to figure out which letter isn't used yet
    ch = ''
    for c in clue:
        if c not in opt_arr[0]:
            ch = c
            break

    for i in range( len(opt_arr) ):
        opt_arr[i][0] = ch


def fill_4( opt_arr, clue ):
    # Need to figure out which 2 letters aren't used yet
    chs = []
    for c in clue:
        if c not in opt_arr[0]:
            chs.append( c )

    for i in range( len(opt_arr) ):
        if i > 1:
            opt_arr[i][5] = chs[0]
            opt_arr[i][6] = chs[1]
        else:
            opt_arr[i][5] = chs[1]
            opt_arr[i][6] = chs[0]


def is_1( segment, clue ):
    if len(clue) == 2:
        return True
    return False

def is_4( segment, clue ):
    if len(clue) == 4:
        return True
    return False

def is_7( segment, clue ):
    if len(clue) == 3:
        return True
    return False

def is_8( segment, clue ):
    if len(clue) == 7:
        return True
    return False

def setup_lit_segs( segment, clue ):
    lit_pos = [0 for _ in range( len(segment) )]
    for ch in clue:
        lit_pos[segment.index( ch )] = 1
    return lit_pos

def is_2( segment, clue ):
    lit_pos = setup_lit_segs( segment, clue )
    return lit_pos[0] and lit_pos[1] and lit_pos[3] and lit_pos[4] and lit_pos[6]\
            and not lit_pos[2] and not lit_pos[5]

def is_3( segment, clue ):
    lit_pos = setup_lit_segs( segment, clue )
    return lit_pos[0] and lit_pos[1] and lit_pos[2] and lit_pos[3] and lit_pos[6]\
            and not lit_pos[4] and not lit_pos[5]

def is_5( segment, clue ):
    lit_pos = setup_lit_segs( segment, clue )
    return lit_pos[0] and lit_pos[2] and lit_pos[3] and lit_pos[5] and lit_pos[6]\
            and not lit_pos[1] and not lit_pos[4]

def is_0( segment, clue ):
    lit_pos = setup_lit_segs( segment, clue )
    return lit_pos[0] and lit_pos[1] and lit_pos[2] and lit_pos[3] and lit_pos[4] and lit_pos[5]\
            and not lit_pos[6]

def is_6( segment, clue ):
    lit_pos = setup_lit_segs( segment, clue )
    return lit_pos[0] and lit_pos[6] and lit_pos[2] and lit_pos[3] and lit_pos[4] and lit_pos[5]\
            and not lit_pos[1]

def is_9( segment, clue ):
    lit_pos = setup_lit_segs( segment, clue )
    return lit_pos[0] and lit_pos[1] and lit_pos[2] and lit_pos[3] and lit_pos[6] and lit_pos[5]\
            and not lit_pos[4]


def can_fit_3( opt_arr, clue ):
    # All characters in clue need to be in opt_arr
    for ch in clue:
        if ch != opt_arr[0] and ch != opt_arr[1] and ch != opt_arr[2]\
            and ch != opt_arr[3] and ch != opt_arr[6]:
            return False

    return True

def can_fit_5( opt_arr, clue ):
    # All characters in clue need to be in opt_arr
    for ch in clue:
        if ch != opt_arr[0] and ch != opt_arr[5] and ch != opt_arr[2]\
            and ch != opt_arr[3] and ch != opt_arr[6]:
            return False

    return True


def part2():

    with open( 'input.txt', 'r' ) as f:

        results = []

        for line in f:
            real_segment = []
            letters_left = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

            digits = line.strip().split()
            clues = digits[:digits.index( "|" )]
            output = digits[digits.index( "|" ) + 1:]

            # Sort the clues from shortest to longest
            clues.sort(key=len)

            # First is always 1
            # Second is always 7
            # Third is always 4
            # But there are still unknown segment positions. Always 4 options.
            options = [ ['' for _ in range(7) ] for _ in range( 4 ) ]

            fill_1( options, clues.pop( 0 ) )
            fill_7( options, clues.pop( 0 ) )
            fill_4( options, clues.pop( 0 ) )

            # Remove clues from letters_left
            for ch in options[0]:
                if ch:
                    letters_left.remove( ch )

            # Now onto the 5 segment digits. Figure out which isn't used, and
            # place where it would make sense. Should only make sense with 2
            # options (of the 4)
            # At this point, we have 5 segments. So we actually need to fill
            # option[3], since option[4] wouldn't provide us with any digit.
            # The only 5 segment digits that could fit here are 3 and 5.
            # If we have 2 unknown characters, we need to skip it...

            c_i = 0
            fit_3 = None
            fit_5 = None
            while c_i < len( clues ):
                clue = clues[c_i]
                # Need to figure out which letter(s) aren't used yet
                chs = []
                for c in clue:
                    if c in letters_left:
                        chs.append( c )

                if len(chs) > 1:
                    # That number is a 2...
                    c_i += 1
                    continue

                # Safe to remove clue
                clues.pop( c_i )

                # Try to fit letter in segment 3
                ch = chs[0]
                o_i = 0
                while o_i < len( options ):
                    options[o_i][3] = ch

                    if can_fit_3( options[o_i], clue ):
                        fit_3 = clue
                        # Erase ch for next clue, or else we won't know the 2
                        options[o_i][3] = ''
                        o_i += 1

                    elif can_fit_5( options[o_i], clue ):
                        fit_5 = clue
                        # Erase ch for next clue, or else we won't know the 2
                        options[o_i][3] = ''
                        o_i += 1

                    else:
                        options.pop( o_i )

                # At this point, we'll have 2 options.
                # If both fit_3 and fit_5 have been set, then there's only
                # 1 option left, since it fits both 3 and 5.
                if fit_3 and fit_5:
                    options[0][3] = ch
                    letters_left.remove( ch )
                    break

                # Keep looping

            real_segment = options[0]
            # The first clue now is a 2 or 5. Just need to fill in the last letter!
            if '' in real_segment:
                real_segment[real_segment.index( '' )] = letters_left.pop()
#            print( real_segment )

            # Now let's determine the output numbers!
            result = []
            for out in output:
                if is_1( real_segment, out ):
                    result.append( '1' )
                elif is_2( real_segment, out ):
                    result.append( '2' )
                elif is_3( real_segment, out ):
                    result.append( '3' )
                elif is_4( real_segment, out ):
                    result.append( '4' )
                elif is_5( real_segment, out ):
                    result.append( '5' )
                elif is_6( real_segment, out ):
                    result.append( '6' )
                elif is_7( real_segment, out ):
                    result.append( '7' )
                elif is_8( real_segment, out ):
                    result.append( '8' )
                elif is_9( real_segment, out ):
                    result.append( '9' )
                elif is_0( real_segment, out ):
                    result.append( '0' )
                else:
                    print( "SOMETHING BAD HAPPENED. ABORTING." )

#            print( ''.join( result ) )
            results.append( int( ''.join( result ) ) )

        print( "Part 2: " + str( sum( results ) ) )

"""
MAIN DRIVER
"""
part1()
part2()
