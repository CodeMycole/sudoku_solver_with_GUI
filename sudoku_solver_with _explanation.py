# sudoku board stored as a 2D list / array. This is the board our program is going to solve_______________________________________________________________________

game_board = [                                  # the index of each potition of the board is as follows:
    [7, 8, 0, 4, 0, 0, 1, 2, 0],                # [[0][0], [0][1], [0][2], [0][3], [0][4], [0][5], [0][6], [0][7], [0][8]],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],                # [[1][0], [1][1], [1][2], [1][3], [1][4], [1][5], [1][6], [1][7], [1][8]],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],                # [[2][0], [2][1], [2][2], [2][3], [2][4], [2][5], [2][6], [2][7], [2][8]],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],                # [[3][0], [3][1], [3][2], [3][3], [3][4], [3][5], [3][6], [3][7], [3][8]],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],                # [[4][0], [4][1], [4][2], [4][3], [4][4], [4][5], [4][6], [4][7], [4][8]],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],                # [[5][0], [5][1], [5][2], [5][3], [5][4], [5][5], [5][6], [5][7], [5][8]],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],                # [[6][0], [6][1], [6][2], [6][3], [6][4], [6][5], [6][6], [6][7], [6][8]],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],                # [[7][0], [7][1], [7][2], [7][3], [7][4], [7][5], [7][6], [7][7], [7][8]],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]                 # [[0][0], [0][1], [0][2], [0][3], [0][4], [0][5], [0][6], [0][7], [0][8]],
]

#_________________________________________________________________________________________________________________________________________________________________
# prints the board with dividers to have the real sudoku feel. the for row, then for column together will make it go through every spot on the board:
# [0][0-8] then [1][0-8] and so forth. if we did not have the range(len()) combination, it wouldn't hold values 0-8. holding these values allows us to use
# the temp variables in the loop as index position identifiers near the end of the function

def print_board(board):
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

# print(print_board(game_board))                                    # used to test if the function works

#_________________________________________________________________________________________________________________________________________________________________
# runs through the whole board and will return the first space that is 'empty'. in this case, any spot that == 0. Will return both of the values needed to
# identify its indexed position in our array

def find_empty(board):
    for row in range(len(board)):                   # just like out other function, this runs 9 time with values 0-8
        for column in range(len(board[0])):         # this also runs 9 times with values 0-8.
            if board[row][column] == 0:             # this will see if the space we are on in the index equals 0 which means it is blank and needs a new value. 
                return (row, column)                # returns it to increase the scope of the variables outside the function. 
    return None                                     # we need this for our solve function to work. the if not found part. 

# print(find_empty(game_board))                     # used to test if the function works

#_________________________________________________________________________________________________________________________________________________________________
# This function checks to see if a value at a certain position works relative to the rest of the board.Once we find an empty space, this will see if a given 
# number is a solution at that space on our board. It first checks all the things that will not work, and if it passes all of those, returns true. 

def valid(board, number, position):
    
    # This function is used to check a row to see if the number we are testing is already used, ignoring what we already inserted.
    
    for column in range(len(board[0])):                                         # this goes through every spot in the column on a given row, and checks
        if board[position[0]][column] == number and position[1] != column:      # to find the number which we will insert in another function
            return False                                                        # and ignore the position we just inserted.

    # this function cheks to see if the number we are testing is already in the column, ignoring again what we already inserted.

    for row in range(len(board)):                                               # This goes through every spot in a column on our board, and checks if
        if board[row][position[1]] == number and position[0] != row:            # the number we are testing is already in the column but not the position
            return False                                                        # we already inserted something into and are testing.

    # Function checks to see if the value we are testig is in the box (3x3 chunk) on our board

    box_x = position[1] // 3                                                    # So if you think of our box as a 3x3 array. this takes a given position, lets say
    box_y = position[0] // 3                                                    # board[0][3] box_x = 1 because 3 // 3 = 1. and box[0][1] puts us in the
                                                                                # top middle box
    for a in range(box_y * 3, box_y * 3 + 3):                   # this part of the code will loop through the box. we *3 because the box x & y before can only
        for b in range(box_x * 3, box_x * 3 + 3):               # return values 0,1, or 2. 2 being the last box, the first value in that box is index 6. 
            if board[a][b] == number and (a, b) != position:    # this checks if the number is in the box, ignoring the spot we are testing. 
                return False                                    # this will return false, which later will mean it has to pick a different number to test. 
    
    return True                                                 # if our number passes all 3 tests, then we can use it as a solution.

#_________________________________________________________________________________________________________________________________________________________________
# This is the function that will use the other three functions we made, plus backtracking, to actually solve our board.

def solve(board):
    find = find_empty(board)                                    # we first run our fuction that finds a spot that needs solving
    if not find:                                                # this means "if we look through the whole board and cannot find any spot that needs solved"
        return True                                             # Our find_empty returns an index if there is a spot. so we are saying if find is false, Then 
    else:                                                       # we are done. the board is solved and we are done. otherwise, it
        row, column = find                                      # returns false, meaning the bored is not solved yet, and we have to go back (backtracking)  
    
    for num in range(1,10):                                     # this will take every number 1-9 and
        if valid(board, num, (row, column)):                    # see if it works in an empty spot found earlier in our function.
            board[row][column] = num                            # and if it does, it will assign it to that spot.

            if solve(board):                                    # this is the backtracking part. this tries our function again. if true, board is solved. if it
                return True                                     # is not true, then it will reset the position we are checking to 0, and try the function again.
                                                                    
            board[row][column] = 0                              # if it cannot find a value that works, it will go back again, setting that to zero. etc. until

    return False                                                # it finds a solution that works, or returns False, in which case the board is unsolvable. 

# this will take everything we have done, and print it all to the terminal. At this point we have done all the work. We just have to run the functions. 

print_board(game_board)
solve(game_board)
print('---------------------------') 
print_board(game_board)


