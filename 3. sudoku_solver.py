# sudoku board stored as a 2D list / array. This is the board our program is going to solve. 

game_board = [                                  # the index of each potition of the board is as follows:
    [0, 0, 0, 6, 0, 0, 1, 0, 7],                # [[0][0], [0][1], [0][2], [0][3], [0][4], [0][5], [0][6], [0][7], [0][8]],
    [6, 8, 0, 9, 5, 1, 3, 0, 0],                # [[1][0], [1][1], [1][2], [1][3], [1][4], [1][5], [1][6], [1][7], [1][8]],
    [0, 0, 3, 0, 0, 2, 5, 6, 8],                # [[2][0], [2][1], [2][2], [2][3], [2][4], [2][5], [2][6], [2][7], [2][8]],
    [0, 4, 0, 8, 1, 0, 0, 2, 0],                # [[3][0], [3][1], [3][2], [3][3], [3][4], [3][5], [3][6], [3][7], [3][8]],
    [0, 0, 0, 0, 0, 0, 8, 5, 0],                # [[4][0], [4][1], [4][2], [4][3], [4][4], [4][5], [4][6], [4][7], [4][8]],
    [0, 9, 0, 0, 6, 5, 0, 7, 3],                # [[5][0], [5][1], [5][2], [5][3], [5][4], [5][5], [5][6], [5][7], [5][8]],
    [4, 0, 9, 0, 0, 3, 0, 8, 5],                # [[6][0], [6][1], [6][2], [6][3], [6][4], [6][5], [6][6], [6][7], [6][8]],
    [1, 6, 2, 0, 0, 9, 0, 3, 0],                # [[7][0], [7][1], [7][2], [7][3], [7][4], [7][5], [7][6], [7][7], [7][8]],
    [5, 0, 0, 7, 0, 6, 0, 0, 0]                 # [[0][0], [0][1], [0][2], [0][3], [0][4], [0][5], [0][6], [0][7], [0][8]],
]

# prints the board with dividers to have the real sudoku feel. the for row, then for column together will make it go through every spot on the board:
# [0][0-8] then [1][0-8] and so forth. if we did not have the range(len()) combination, it wouldn't hold values 0-8. holding these values allows us to use
# the temp variables in the loop as index position identifiers near the end of the function. 

def print_board(board):
    print('')                                                       # adds space in your terminal for a nice look. 
    for row in range(len(board)):                                   # will run as many times as we have rows, starting with 0. 
        if row % 3 == 0 and row != 0:                               # since index starts at 0. this will print a line
            print('------- -------- -------')                       # brefore the start of the 4th row (index 3) without one at the top.
        
        for column in range(len(board[0])):                         # now it will run through every column essentially, again startig with 0.
            if column % 3 == 0 and column != 0:                     # just like before, this will create the virtical line dividers
                print(' | ', end = '')                              # but without one on the far left. the end keeps the function on the same line
                                                                    # instead of moving on
            if column == 8:
                print(board[row][column])                           # this prints the last column value without extra space
            else:
                print(str(board[row][column]) + ' ', end= '')       # this prints every value of the board with space in between for a clean look.
    return ''                                                       # Without this, at the end of our board, it would show None to our Terminal.

print(print_board(game_board))                                      # used to test if the function works

# runs through the whole board and will return the first space that is 'empty'. in this case, any spot that == 0. Will return both of the values needed to
# identify its indexed position in our array.

def find_empty(board):
    for row in range(len(board)):                   # just like out other function, this runs 9 time with values 0-8
        for column in range(len(board[0])):         # this also runs 9 times with values 0-8.
            if board[row][column] == 0:             # this will see if the space we are on in the index equals 0 which means it is blank and needs a new value. 
                return (row, column)                # returns it to increase the scope of the variables outside the function. 

print(find_empty(game_board))                       # used to test if the function works