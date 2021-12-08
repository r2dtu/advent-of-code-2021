import numpy as np

def check_bingo( board ):

    # Check all horizontal
    for row in board:
        if 0 in row:
            continue

        return True

    # Check all vertical
    for row in np.transpose( board ):
        if 0 in row:
            continue

        return True

    """
    JK DIAGONALS DON'T COUNT
    # Check diagonals
    no_bingo = False
    for i,val in enumerate( board ):
        if board[i][i] == 0:
            no_bingo = True
            break

    # If boolean is still false, then the break never happened
    if not no_bingo:
        return True

    no_bingo = False
    for i,val in enumerate( board ):
        if board[i][len( board[i] ) - 1 - i] == 0:
            no_bingo = True
            break

    # If boolean is still false, then the break never happened
    if not no_bingo:
        return True
    """

    return False


def mark_board( board, marked_board, drawing ):
    for i,row in enumerate( board ):
        for j,num in enumerate( row ):
            if drawing == num:
                marked_board[i][j] = 1
                return


def calculate_final_score( board, marked_board, drawing ):

    final_score = 0

    # Calculate final score: sum of all unmarked numbers on that 
    # board times the number just called
    for val,x in zip( board.flatten(), marked_board.flatten() ):
        if x == 0:
            final_score += int( val )

    return final_score * int( drawing )


# Main Function
if __name__ == '__main__':

    drawings = None
    boards = []
    marked_boards = []

    with open( 'input.txt', 'r' ) as f:

        drawings = f.readline().strip().split( ',' )
        f.readline()

        # Bingo is 5x5
        board = []
        for line in f:

            tmp = line.strip()
            if not tmp:
                boards.append( board )
                board = []
                continue

            board.append( tmp.split() )

        # Since there's no new line at the end
        boards.append( board )

    boards = np.array( boards )
    marked_boards = np.zeros( boards.shape )

    # For each drawing, mark every board
    bingos = []
    all_bingo = False

    for drawing in drawings:
        if all_bingo:
            break

        for i,board in enumerate( boards ):

            # Board already received bingo, next
            if i in bingos:
                continue

            # Mark board if drawing number exists
            mark_board( boards[i], marked_boards[i], drawing )

            # @better is there a case where 2 boards get bingo at the same time?
            if (check_bingo( marked_boards[i] )):

                # Print final score
                score = calculate_final_score( boards[i], marked_boards[i],
                                               drawing )
                print( score )

                bingos.append( i )

                if len( bingos ) == len( boards ):
                    all_bingo = True
                    break

