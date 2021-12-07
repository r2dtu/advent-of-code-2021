"""
Day 2 Full Solution
"""

def part1():

    x_pos = 0
    y_pos = 0

    with open( 'input.txt', 'r+' ) as f:

        for line in f.readlines():

            command, units = line.split( ' ' )

            if command == "forward":
                x_pos += int( units )

            elif command == "down":
                y_pos += int( units )

            elif command == "up":
                y_pos -= int( units )

            else:
                print( 'Invalid command: ' + command )

    print( 'Final pos: (%d, %d)', x_pos, y_pos )
    print( 'Calculated: ' + str( x_pos * y_pos ) )


def part2():
    x_pos = 0
    y_pos = 0
    aim = 0

    with open( 'input.txt', 'r+' ) as f:

        for line in f.readlines():

            command, units = line.split( ' ' )

            if command == "forward":
                x_pos += int( units )
                y_pos += aim * int( units )

            elif command == "down":
                aim += int( units )

            elif command == "up":
                aim -= int( units )

            else:
                print( 'Invalid command: ' + command )

    print( 'Final pos: (%d, %d)', x_pos, y_pos )
    print( 'Calculated: ' + str( x_pos * y_pos ) )


part1()
part2()
