import random
import math
import time

'''
    Project Requirement:
    - Requires board argument to take in a 1D list as input and 1D list as output 

    General Points:
    As input and outputs both use 1D list!
    Therefore, have a function to convert from 1D list to 2D list and vice versa.

    The reversed() function is applied on the board first as for 1D list the first element
    is the 0th row and 0th column which is the bottom left hand corner of the board.

    while the 2D list here the 0th row and 0th column refers to to the top right hand corner
    of the board.
'''

invalid_cols = [] # this will store the cols which have been filled up and have to be popped


def one_dim_to_two_dim(board):
    # convert 1D list to 2D list #
    output_list = []
    row_list = []
    count = 0
    for val in board:
        row_list.append(val)
        count += 1
        if (count % 7 == 0): # fixed 7 entries per row
            output_list.insert(0, row_list)
            row_list = [] # clear row_list

    return output_list


def two_dim_to_one_dim(board):
    # convert 2D list to 1D list #
    output_list = []
    for row in reversed(board):
        for val in row:
            output_list.append(val)
    
    return output_list


def check_move(board, turn, col, pop):
    # implement your function here'

    # Convert the board from one-dimensional to two-dimensional
    board = one_dim_to_two_dim(board)
    
    # Check if column index is valid
    if col < 0 or col >= len(board[0]):
        print("The column you selected is outside of the board.")
        return False  # Invalid column index
    
    if not pop:  # For a drop move
        # Check if the column is full
        is_full = all(board[row][col] != 0 for row in range(len(board)))
        if is_full:
            invalid_cols.append(col)
            print("The column you selected is full, please try another column.")
            return False  # Cannot drop into a full column
        
        # Check for a valid empty spot in the column
        for i in range(len(board) - 1, -1, -1):  # Iterate from bottom to top
            if board[i][col] == 0:
                return True  # Valid move if an empty spot is found
    
    elif pop:  # For a pop move
        # The bottom-most row index
        bottom_most_row = len(board) - 1
        # Check if the bottom-most piece matches the player's turn
        if (turn == 1 and board[bottom_most_row][col] == 1) or \
           (turn == 2 and board[bottom_most_row][col] == 2):
            return True  # Valid move if the bottom-most piece matches the turn
        else:
            print("No Disc To Be Popped, Please Try Another Column!")
            return False
    
    print("No valid moves found.")
    return False  # If no valid move is found


def apply_move(board, turn, col, pop):
    # implement your function here

    '''

        Note that these scenarios (A) and (B) are merely used for the test(1).py file

        (A) In this check_move() function I have added the additional checks for these conditions:
        1) board[bottom_most_row][col] == 1
        2) board[bottom_most_row][col] == 2
        3) board[i][col] == 0

        (B) I have also changed the board from a 1D list to a 2D list as the input for test(1).py is a
        1D list.

    '''
    
    board = one_dim_to_two_dim(board)

    if (pop == False):
        if (col >= 0 and col <= len(board[0])-1): # col <= board's width
            for i in range(len(board)-1, -1 , -1): # iterating over board's height
                # print("value i:", i)
                if (board[i][col] == 0):
                    insert_row = i
                    break
        
            # print()
            # print("INSERTED ROW:", insert_row)
            # print()

            if (turn == 1):
                board[insert_row][col] = 1
            else: # turn is 2
                board[insert_row][col] = 2
            
            board = two_dim_to_one_dim(board) # board has to be 1D as input
            display_board(board)

            return board.copy()

    # elif (pop == True):
    #     # move every disc above current disc down 1 space

    #     bottom_most_row = len(board)-1
    #     if (board[bottom_most_row-1][col] == 0):
    #         board[bottom_most_row][col] = 0
        
    #     else:
    #         for pos in range(len(board)-1, -1, -1):
    #             if (board[pos-1][col] == 0):
    #                 board[pos][col] = 0
    #                 break
    #             else:
    #                 board[pos][col] = board[pos-1][col]

    elif (pop == True):
        # move every disc above the bottom-most disc down 1 space
        bottom_most_row = len(board) - 1
        
        # Shift all discs down, keeping the top-most as 0
        for pos in range(bottom_most_row, 0, -1):
            if (board[pos][col] == 0):
                break
            board[pos][col] = board[pos-1][col]

            # Top-most row is non-zero
            if (pos-1) == 0:
                board[pos-1][col] = 0  # Set the top-most row to 0
            

        board = two_dim_to_one_dim(board) # board has to be 1D as input
        display_board(board)

        # returned board is in 1D #
        return board.copy()


def computer_attacks(get_way_of_computer, way_of_computer):
    '''
        Scenario where Computer can have a direct win is set up above already, now is to set up the win whenever there are 1 or 2 computer discs in play.

        Notice that we do not set up wins from:
        1) Main Diagonal
        2) Reflected Diagonal
        3) Non-Contiguous Horizontal

        * It is assumed from practice that it's better to optimize for horizontal and vertical wins first and if by chance, wins from scenario 1), 2) or
        3) occurs then do a direct win for them because 1), 2) or 3) are less often scenarios and 1), 2), 3) have more uncertainty involved in the setting
        up for the win process as compared to setting up the win for horizontal and vertical wins
    '''

    print("COMPUTER SCORE MORE THAN USER!")
    print("COMPUTER ATTACKS ...")

    # START OF 1 SCORE #
    if (get_way_of_computer == 0 and way_of_computer == 1): # horizontal win is available
        if (computer_high_score_col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx+1]) == 0):
            print("COMPUTER SETTING UP A HORIZONTAL WIN (A)")
            return (computer_high_score_col_idx+1, False)
        elif (computer_high_score_col_idx-1 >= 0) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx-1]) == 0):
                print("COMPUTER SETTING UP A HORIZONTAL WIN (B)")
                return (computer_high_score_col_idx-2, False)

    elif (get_way_of_computer == 1 and way_of_computer == 1): # vertical win is avaialable
        if (computer_high_score_row_idx-1 >= 0) and (max(combined_mat[computer_high_score_row_idx-1][computer_high_score_col_idx]) == 0):
            print("COMPUTER SETTING UP VERTICAL WIN")
            return (computer_high_score_col_idx, False)
    # END OF 1 SCORE #

    # START OF 2 SCORE #
    if (get_way_of_computer == 0 and way_of_computer == 2): # horizontal win is available
        if (computer_high_score_col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx+1]) == 0):
            print("COMPUTER SETTING UP A HORIZONTAL WIN (A)")
            return (computer_high_score_col_idx+1, False)
        elif (computer_high_score_col_idx-2 >= 0) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx-2]) == 0):
                print("COMPUTER SETTING UP A HORIZONTAL WIN (B)")
                return (computer_high_score_col_idx-2, False)

    elif (get_way_of_computer == 1 and way_of_computer == 2): # vertical win is avaialable
        if (computer_high_score_row_idx-1 >= 0) and (max(combined_mat[computer_high_score_row_idx-1][computer_high_score_col_idx]) == 0):
            print("COMPUTER SETTING UP VERTICAL WIN")
            return (computer_high_score_col_idx, False)
    # END OF 2 SCORE #


def check_victory(board, who_played):

    # implement your function here

    board = one_dim_to_two_dim(board)

    # col index increasing from left to right
    # row index increasing from top to bottom

    '''
        check if opponent wins first
    '''

    ############################################################################
    # CHECK IF PLAYER 2 HAS WON #
    if (who_played == 1):

        # check horizontal spaces
        for row in range(len(board)):
            for col in range(len(board[0]) - 3):
                if (board[row][col] == 2 and board[row][col+1] == 2 and \
                    board[row][col+2] == 2 and board[row][col+3] == 2):
                    return 2

        # check vertical spaces
        for col in range(len(board[0])):
            for row in range(len(board) - 3):
                if (board[row][col] == 2 and board[row+1][col] == 2 and \
                    board[row+2][col] == 2 and board[row+3][col] == 2):
                    return 2

        # check main diagonal spaces
        for col in range(len(board[0]) - 3):
            for row in range(len(board) - 3): # minus 2 is because of the 2 descriptive rows at the bottom
                if (board[row][col] == 2 and board[row+1][col+1] == 2 and \
                    board[row+2][col+2] == 2 and board[row+3][col+3] == 2):
                    return 2

        # check reflected diagonal spaces
        for col in range(3, len(board[0])):
            for row in range(len(board) - 3): # minus 2 is because of the 2 descriptive rows at the bottom
                if (board[row][col] == 2 and board[row+1][col-1] == 2 and \
                    board[row+2][col-2] == 2 and board[row+3][col-3] == 2):
                    return 2
    ############################################################################


    ############################################################################
    # CHECK IF PLAYER 1 HAS WON #
    elif (who_played == 2):
        
        # check horizontal spaces
        for row in range(len(board)):
            for col in range(len(board[0]) - 3):
                if (board[row][col] == 1 and board[row][col+1] == 1 and \
                    board[row][col+2] == 1 and board[row][col+3] == 1):
                    return 1

        # check vertical spaces
        for col in range(len(board[0])):
            for row in range(len(board) - 3):
                if (board[row][col] == 1 and board[row+1][col] == 1 and \
                    board[row+2][col] == 1 and board[row+3][col] == 1):
                    return 1

        # check main diagonal spaces
        for col in range(len(board[0]) - 3):
            for row in range(len(board) - 3): # minus 2 is because of the 2 descriptive rows at the bottom
                if (board[row][col] == 1 and board[row+1][col+1] == 1 and \
                    board[row+2][col+2] == 1 and board[row+3][col+3] == 1):
                    return 1

        # check reflected diagonal spaces
        for col in range(3, len(board[0])):
            for row in range(len(board) - 3): # minus 2 is because of the 2 descriptive rows at the bottom
                if (board[row][col] == 1 and board[row+1][col-1] == 1 and \
                    board[row+2][col-2] == 1 and board[row+3][col-3] == 1):
                    return 1
    ############################################################################

    
    ############################################################################
    # CHECK IF who_played HAS WON #

    # check horizontal spaces
    for row in range(len(board)):
        for col in range(len(board[0]) - 3):
            if (board[row][col] == 1 and board[row][col+1] == 1 and \
                board[row][col+2] == 1 and board[row][col+3] == 1):
                return 1

    # check vertical spaces
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if (board[row][col] == who_played and board[row+1][col] == who_played and \
                board[row+2][col] == who_played and board[row+3][col] == who_played):
                return who_played

    # check main diagonal spaces
    for col in range(len(board[0]) - 3):
        for row in range(len(board) - 3): # minus 2 is because of the 2 descriptive rows at the bottom
            if (board[row][col] == who_played and board[row+1][col+1] == who_played and \
                board[row+2][col+2] == who_played and board[row+3][col+3] == who_played):
                return who_played

    # check reflected diagonal spaces
    for col in range(3, len(board[0])):
        for row in range(len(board) - 3): # minus 2 is because of the 2 descriptive rows at the bottom
            if (board[row][col] == who_played and board[row+1][col-1] == who_played and \
                board[row+2][col-2] == who_played and board[row+3][col-3] == who_played):
                return who_played
    ############################################################################
            
    return 0


def update_computer(row_idx, col_idx):
    new_computer_high_score = max(combined_mat[row_idx][col_idx])
    computer_high_score_row_idx = row_idx
    computer_high_score_col_idx = col_idx

    return new_computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx


def check_computer(board, row_idx, col_idx, check_getWay_computer, check_Way_computer):
    
    # print("BOARD:", board)
    # print("COMPUTER HIGH SCORE ROW IDX:", row_idx)
    # print("COMPUTER HIGH SCORE COL IDX:", col_idx)
    # print("get way:", check_getWay_computer)
    # print("way:", check_Way_computer)
    # print("combined mat:", combined_mat)

    ###################################################################################
    # if direct POP horizontal win is avaialable, give computer direct win #

    '''
        4 Scenarios:

                BRRB
    (Eaxmple 1) RRBR
                BBRB
                    ^


        Both of the above scenarios will be a direct win for R
    '''
    if (check_getWay_computer == 0 and check_Way_computer == 3): # if direct horizontal win is available, give computer direct win
        print("!-----------------------------!")
        if ( (col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[row_idx][col_idx+1]) != 0) \
            and (row_idx+1<= len(combined_mat[0])-1) ) or \
            ( (col_idx-3 >= 0) and (max(combined_mat[row_idx][col_idx-3]) != 0) \
            and (row_idx+1<= len(combined_mat[0])-1) ):

            print("++++++++++++++++++++++++++++++++++++")
            computer_win = True
            computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx = update_computer(row_idx, col_idx)
            return computer_win, computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx
        
    
    if (check_getWay_computer == 0 and check_Way_computer == 2):
        # print("!!-----------------------------!!")

        # c1 = (col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[row_idx][col_idx+1]) == 0)
        # c2 = (col_idx+2 <= len(combined_mat[0])-1) and (max(combined_mat[row_idx][col_idx+2]) > 0)
        # c3 = (col_idx-1 >= 0) and (max(combined_mat[row_idx][col_idx-1]) > 0)
        # c4 = row_idx+1<= len(combined_mat[0])-1

        # print(c1, c2, c3, c4)

        # print("END CHECKS")

        if ( (col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[row_idx][col_idx+1]) != 0) \
            and (col_idx+2 <= len(combined_mat[0])-1) and (max(combined_mat[row_idx][col_idx+2]) > 0) \
            and (col_idx-1 >= 0) and (max(combined_mat[row_idx][col_idx-1]) > 0) \
            and (row_idx+1<= len(combined_mat[0])-1) ) \
        or  ( (col_idx-1 >= 0) and (max(combined_mat[row_idx][col_idx-1]) > 0) \
            and (col_idx-2 >= 0) and (max(combined_mat[row_idx][col_idx-2]) != 0) \
            and (col_idx-3 >= 0) and (max(combined_mat[row_idx][col_idx-3]) > 0) \
            and (row_idx+1<= len(combined_mat[0])-1) ):

            print("++++++++++++++++++++++++++++++++++++")
            computer_win = True
            computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx = update_computer(row_idx, col_idx)
            return computer_win, computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx

    ###################################################################################


    ############################################################################
    # COMPUTER 1 disc from NON-CONTIGUOUS HORIZONTAL "DIRECT" win #
    # REQUIRES A SPECIAL LOOK FORWARD KIND OF TECHNIQUE #
        '''
            2 Scenarios:
                (1) RR_R
                (2) R_RR

            Both of the above scenarios will be a direct win for R
        '''

    if (check_getWay_computer == 0 and check_Way_computer == 2):

        if ( (col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[row_idx][col_idx+1]) == 0) \
            and (col_idx+2 <= len(combined_mat[0])-1) and (max(combined_mat[row_idx][col_idx+2]) > 0) \
            and (col_idx-1 >= 0) and (max(combined_mat[row_idx][col_idx-1]) > 0) ) \
        or ( (col_idx-1 >= 0) and (max(combined_mat[row_idx][col_idx-1]) > 0) \
            and (col_idx-2 >= 0) and (max(combined_mat[row_idx][col_idx-2]) == 0) \
            and (col_idx-3 >= 0) and (max(combined_mat[row_idx][col_idx-3]) > 0) ):

            # print("# THERE IS NO different colored disc in NON-CONTIGUOUS HORIZONTAL DIRECT win")
            # print("UPDATE ...")
            # print("old high score:", computer_high_score)

            print("============================")
            computer_win = True
            computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx = update_computer(row_idx, col_idx)
            return computer_win, computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx

            # print("new high score:", max(combined_mat[row_idx][col_idx]))
            # print("(HIGHEST SCORE COMPUTER) row_idx:", row_idx, "col_idx:", col_idx)
            # print()
        
    ############################################################################


    ''' 
    Now let's cover the special cases ...
        Special Cases:
        1) Computer 1 disc from main diagonal win
        2) Computer 1 disc from reflected diagonal win
        3) Computer 1 disc from non-contiguous horizontal win
    '''
    #######################################################################
    # COMPUTER 1 disc from main diagonal win #
    if (check_getWay_computer == 2 and check_Way_computer == 3):
        if ( (row_idx-1 >= 0) and (col_idx-1 >= 0) and \
            (max(combined_mat[row_idx-1][col_idx-1]) == 0) ):

            selected_row = row_idx-1
            # check if this column is actually possible #
            for i in range(len(board)-1, -1, -1): # iterating over board's height
                if board[i][col_idx-1] == 0:
                    insert_row = i
                    break
            
            if (insert_row == selected_row):
                # print("# COMPUTER: THERE IS NO different colored disc in MAIN DIAGONAL")
                # print("UPDATE ...")
                # print("old high score:", computer_high_score)

                computer_win = True
                computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx = update_computer(row_idx, col_idx)
                return computer_win, computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx

                # print("new high score:", max(combined_mat[row_idx][col_idx]))
                # print("(HIGHEST SCORE COMPUTER) row_idx:", row_idx, "col_idx:", col_idx)
                # print()
                
        elif ( (row_idx+3 <= len(combined_mat)-2) and (col_idx+3 <= len(combined_mat[0])-1) and \
            (max(combined_mat[row_idx+3][col_idx+3]) == 0) ):

            selected_row = row_idx+3
            # check if this column is actually possible #
            for i in range(len(board)-1, -1, -1): # iterating over board's height
                if board[i][col_idx+3] == 0:
                    insert_row = i
                    break
            
            if (insert_row == selected_row):
                # print("# COMPUTER: THERE IS NO different colored disc in MAIN DIAGONAL")
                # print("UPDATE ...")
                # print("old high score:", computer_high_score)

                computer_win = True
                computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx = update_computer(row_idx, col_idx)
                return computer_win, computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx

                # print("new high score:", max(combined_mat[row_idx][col_idx]))
                # print("(HIGHEST SCORE COMPUTER) row_idx:", row_idx, "col_idx:", col_idx)
                # print()
            
    #######################################################################


    ############################################################################
    # COMPUTER 1 disc from reflected diagonal win #
    if (check_getWay_computer == 3 and check_Way_computer == 3):
        if ( (row_idx-1 >= 0) and (col_idx+1 <= len(combined_mat[0])-1) and \
            (max(combined_mat[row_idx-1][col_idx+1]) == 0) ):

            selected_row = row_idx-1
            # check if this column is actually possible #
            for i in range(len(board)-1, -1, -1): # iterating over board's height
                if board[i][col_idx+1] == 0:
                    insert_row = i
                    break
            
            if (insert_row == selected_row):
                # print("# COMPUTER: THERE IS NO different colored disc in REFLECTED DIAGONAL")
                # print("UPDATE ...")
                # print("old high score:", computer_high_score)

                computer_win = True
                computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx = update_computer(row_idx, col_idx)
                return computer_win, computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx

                # print("new high score:", max(combined_mat[row_idx][col_idx]))
                # print("(HIGHEST SCORE COMPUTER) row_idx:", row_idx, "col_idx:", col_idx)
                # print()

        elif ( (row_idx+3 <= len(combined_mat)-2) and (col_idx-3 >= 0) and \
            (max(combined_mat[row_idx+3][col_idx-3]) == 0) ):
            
            selected_row = row_idx+3
            # check if this column is actually possible #
            for i in range(len(board)-1, -1, -1): # iterating over board's height
                if board[i][col_idx-3] == 0:
                    insert_row = i
                    break
            
            if (insert_row == selected_row):
                # print("# COMPUTER: THERE IS NO different colored disc in REFLECTED DIAGONAL")
                # print("UPDATE ...")
                # print("old high score:", computer_high_score)
                
                computer_win = True
                computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx = update_computer(row_idx, col_idx)
                return computer_win, computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx

                # print("new high score:", max(combined_mat[row_idx][col_idx]))
                # print("(HIGHEST SCORE COMPUTER) row_idx:", row_idx, "col_idx:", col_idx)
                # print()

            
            
    ############################################################################


    '''
        We will first cover the standard cases for 1 and 2 consecutive computer discs:
        1) horizontal manner
        2) vertical manner

        special cases of 1) main diagonal, 2) reflected diagonal, 3) non-contiguous horizontal
        are done first
    '''

    # START OF 3 SCORES #
    if (check_getWay_computer == 0 and check_Way_computer == 3):
        if ( (col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[row_idx][col_idx+1]) == 0) ) or \
            ( (col_idx-3 >= 0) and (max(combined_mat[row_idx][col_idx-3]) == 0) ): # if there is a different colored disc vertically on top, dont update
            # print("# COMPUTER: THERE IS NO different colored disc horizontally on right (OR)")
            # print("# COMPUTER: THERE IS NO different colored disc horizontally on left ..")
            # print("COMPUTER: UPDATE ...")
            # print("COMPUTER: old high score:", computer_high_score)
            
            computer_win = True
            computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx = update_computer(row_idx, col_idx)
            return computer_win, computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx
        
            # print("COMPUTER: new high score:", max(combined_mat[row_idx][col_idx]))
            # print("(HIGHEST SCORE COMPUTER) row_idx:", row_idx, "col_idx:", col_idx)
            # print()
    elif (check_getWay_computer == 1 and check_Way_computer == 3):
        if (row_idx-1 >= 0) and (max(combined_mat[row_idx-1][col_idx]) == 0):
            # print("# COMPUTER: THERE IS NO different colored disc vertically on top")
            # print("COMPUTER: UPDATE ...")
            # print("COMPUTER: old high score:", computer_high_score)
            
            computer_win = True
            computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx = update_computer(row_idx, col_idx)
            return computer_win, computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx
        
            # print("COMPUTER: new high score:", max(combined_mat[row_idx][col_idx]))
            # print("(HIGHEST SCORE COMPUTER) row_idx:", row_idx, "col_idx:", col_idx)
            # print()
    # END OF 3 SCORES #
    
    # START OF 2 SCORES #
    if (check_getWay_computer == 0 and check_Way_computer == 2):
        if ( (col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[row_idx][col_idx+1]) == 0) ) or \
            ( (col_idx-2 >= 0) and (max(combined_mat[row_idx][col_idx-2]) == 0) ): # if there is a different colored disc vertically on top, dont update
            # print("# COMPUTER: THERE IS NO different colored disc horizontally on right (OR)")
            # print("# COMPUTER: THERE IS NO different colored disc horizontally on left ..")
            # print("COMPUTER: UPDATE ...")
            # print("COMPUTER: old high score:", computer_high_score)
            
            computer_win = False
            computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx = update_computer(row_idx, col_idx)
            return computer_win, computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx
        
            # print("COMPUTER: new high score:", max(combined_mat[row_idx][col_idx]))
            # print("(HIGHEST SCORE COMPUTER) row_idx:", row_idx, "col_idx:", col_idx)
            # print()
    elif (check_getWay_computer == 1 and check_Way_computer == 2):
        if (row_idx-1 >= 0) and (max(combined_mat[row_idx-1][col_idx]) == 0):
            # print("# COMPUTER: THERE IS NO different colored disc vertically on top")
            # print("COMPUTER: UPDATE ...")
            # print("COMPUTER: old high score:", computer_high_score)

            computer_win = False
            computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx = update_computer(row_idx, col_idx)
            return computer_win, computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx
        
            # print("COMPUTER: new high score:", max(combined_mat[row_idx][col_idx]))
            # print("(HIGHEST SCORE COMPUTER) row_idx:", row_idx, "col_idx:", col_idx)
            # print()
    # END OF 2 SCORES #

    # START OF 1 SCORE #
    if (check_getWay_computer == 0 and check_Way_computer == 1):
        if ( (col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[row_idx][col_idx+1]) == 0) ) or \
            ( (col_idx-1 >= 0) and (max(combined_mat[row_idx][col_idx-1]) == 0) ): # if there is a different colored disc vertically on top, dont update
            # print("# COMPUTER: THERE IS NO different colored disc horizontally on right (OR)")
            # print("# COMPUTER: THERE IS NO different colored disc horizontally on left ..")
            # print("COMPUTER: UPDATE ...")
            # print("COMPUTER: old high score:", computer_high_score)
            
            computer_win = False
            computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx = update_computer(row_idx, col_idx)
            return computer_win, computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx
        
            # print("COMPUTER: new high score:", max(combined_mat[row_idx][col_idx]))
            # print("(HIGHEST SCORE COMPUTER) row_idx:", row_idx, "col_idx:", col_idx)
            # print()
    elif (check_getWay_computer == 1 and check_Way_computer == 1):
        if (row_idx-1 >= 0) and (max(combined_mat[row_idx-1][col_idx]) == 0):
            # print("# COMPUTER: THERE IS NO different colored disc vertically on top")
            # print("COMPUTER: UPDATE ...")
            # print("COMPUTER: old high score:", computer_high_score)
            
            computer_win = False
            computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx = update_computer(row_idx, col_idx)
            return computer_win, computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx
        
            # print("COMPUTER: new high score:", max(combined_mat[row_idx][col_idx]))
            # print("(HIGHEST SCORE COMPUTER) row_idx:", row_idx, "col_idx:", col_idx)
            # print()
    # END OF 1 SCORE #
    
    ## END ##

    else:
        return None


def update_user(row_idx, col_idx):
    new_user_high_score = min(combined_mat[row_idx][col_idx])
    user_high_score = new_user_high_score
    user_high_score_row_idx = row_idx
    user_high_score_col_idx = col_idx

    return user_high_score, user_high_score_row_idx, user_high_score_col_idx


def check_user(board, row_idx, col_idx, check_getWay_user, check_Way_user):

    # print("CHECKING USER >>>")

    # START OF 3 SCORES #
    if (check_getWay_user == 0 and check_Way_user == -3):
        if ( (col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[row_idx][col_idx+1]) == 0) ) or \
            ( (col_idx-3 >= 0) and (max(combined_mat[row_idx][col_idx-3]) == 0) ): # if there is a different colored disc vertically on top, dont update
            
            # user 1 disc from horizontal win #

            user_high_score, user_high_score_row_idx, user_high_score_col_idx = update_user(row_idx, col_idx)
            print("(HIGHEST SCORE USER) row_idx:", user_high_score_row_idx, "col_idx:", user_high_score_col_idx)
            return user_high_score, user_high_score_row_idx, user_high_score_col_idx
        
            # print("USER: new high score:", new_user_high_score)
            # print("(HIGHEST SCORE USER) row_idx:", row_idx, "col_idx:", col_idx)
            # print()
    elif (check_getWay_user == 1 and check_Way_user == -3):
        if (row_idx-1 >= 0) and (max(combined_mat[row_idx-1][col_idx]) == 0):
            
            # user 1 disc from vertical win #

            user_high_score, user_high_score_row_idx, user_high_score_col_idx = update_user(row_idx, col_idx)
            print("(HIGHEST SCORE USER) row_idx:", user_high_score_row_idx, "col_idx:", user_high_score_col_idx)
            return user_high_score, user_high_score_row_idx, user_high_score_col_idx
        
            # print("USER: new high score:", new_user_high_score)
            # print("(HIGHEST SCORE USER) row_idx:", row_idx, "col_idx:", col_idx)
            # print()
    # END OF 3 SCORES #



    #######################################################################
    # user 1 disc from main diagonal win #
    elif (check_getWay_user == 2 and check_Way_user == -3):
        if ( (row_idx-1 >= 0) and (col_idx-1 >= 0) and \
            (max(combined_mat[row_idx-1][col_idx-1]) == 0) ):

            selected_row = row_idx-1
            # check if this column is actually possible #
            for i in range(len(board)-1, -1, -1): # iterating over board's height
                if board[i][col_idx-1] == 0:
                    insert_row = i
                    break
            
            if (insert_row == selected_row):
                # print("# THERE IS NO different colored disc in MAIN DIAGONAL")
                # print("UPDATE ...")
                # print("old high score:", user_high_score)
                
                user_high_score, user_high_score_row_idx, user_high_score_col_idx = update_user(row_idx, col_idx)
                print("(HIGHEST SCORE USER) row_idx:", user_high_score_row_idx, "col_idx:", user_high_score_col_idx)
                return user_high_score, user_high_score_row_idx, user_high_score_col_idx

                # print("new high score:", min(combined_mat[row_idx][col_idx]))
                # print("(HIGHEST SCORE USER) row_idx:", row_idx, "col_idx:", col_idx)
                # print()
                
        elif ( (row_idx+3 <= len(combined_mat)-2) and (col_idx+3 <= len(combined_mat[0])-1) and \
            (max(combined_mat[row_idx+3][col_idx+3]) == 0) ):

            selected_row = row_idx+3
            # check if this column is actually possible #
            for i in range(len(board)-1, -1, -1): # iterating over board's height
                if board[i][col_idx+3] == 0:
                    insert_row = i
                    break
            
            if (insert_row == selected_row):
                # print("# THERE IS NO different colored disc in MAIN DIAGONAL")
                # print("UPDATE ...")
                # print("old high score:", user_high_score)
                
                user_high_score, user_high_score_row_idx, user_high_score_col_idx = update_user(row_idx, col_idx)
                print("(HIGHEST SCORE USER) row_idx:", user_high_score_row_idx, "col_idx:", user_high_score_col_idx)
                return user_high_score, user_high_score_row_idx, user_high_score_col_idx

                # print("new high score:", min(combined_mat[row_idx][col_idx]))
                # print("(HIGHEST SCORE USER) row_idx:", row_idx, "col_idx:", col_idx)
                # print()
            
    #######################################################################


    ############################################################################
    # user 1 disc from reflected diagonal win #
    elif (check_getWay_user == 3 and check_Way_user == -3):

        if ( (row_idx-1 >= 0) and (col_idx+1 <= len(combined_mat[0])-1) and \
            (max(combined_mat[row_idx-1][col_idx+1]) == 0) ):

            selected_row = row_idx-1
            # check if this column is actually possible #
            for i in range(len(board)-1, -1, -1): # iterating over board's height
                if board[i][col_idx+1] == 0:
                    insert_row = i
                    break
            
            if (insert_row == selected_row):
                # print("# THERE IS NO different colored disc in REFLECTED DIAGONAL")
                # print("UPDATE ...")
                # print("old high score:", user_high_score)
                
                user_high_score, user_high_score_row_idx, user_high_score_col_idx = update_user(row_idx, col_idx)
                print("(HIGHEST SCORE USER) row_idx:", user_high_score_row_idx, "col_idx:", user_high_score_col_idx)
                return user_high_score, user_high_score_row_idx, user_high_score_col_idx

                # print("new high score:", min(combined_mat[row_idx][col_idx]))
                # print("(HIGHEST SCORE USER) row_idx:", row_idx, "col_idx:", col_idx)
                # print()

        elif ( (row_idx+3 <= len(combined_mat)-2) and (col_idx-3 >= 0) and \
            (max(combined_mat[row_idx+3][col_idx-3]) == 0) ):
            
            selected_row = row_idx+3
            # check if this column is actually possible #
            for i in range(len(board)-1, -1, -1): # iterating over board's height
                if board[i][col_idx-3] == 0:
                    insert_row = i
                    break
            
            if (insert_row == selected_row):
                # print("# THERE IS NO different colored disc in REFLECTED DIAGONAL")
                # print("UPDATE ...")
                # print("old high score:", user_high_score)
                
                user_high_score, user_high_score_row_idx, user_high_score_col_idx = update_user(row_idx, col_idx)
                print("(HIGHEST SCORE USER) row_idx:", user_high_score_row_idx, "col_idx:", user_high_score_col_idx)
                return user_high_score, user_high_score_row_idx, user_high_score_col_idx

                # print("new high score:", min(combined_mat[row_idx][col_idx]))
                # print("(HIGHEST SCORE USER) row_idx:", row_idx, "col_idx:", col_idx)
                # print()

    ############################################################################

    ############################################################################
    # user 1 disc from NON-CONTIGUOUS HORIZONTAL win #
        '''
            2 Scenarios:
                (1) RR_R
                (2) R_RR

            Both of the above scenarios will be a direct win for R
        '''
    if (check_getWay_user == 0 and check_Way_user == -2):
        if ( (col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[row_idx][col_idx+1]) == 0) \
                and (col_idx+2 <= len(combined_mat[0])-1) and (min(combined_mat[row_idx][col_idx+2]) < 0) \
                and (col_idx-1 >= 0) and (min(combined_mat[row_idx][col_idx-1]) < 0) ) \
            or ( (col_idx-1 >= 0) and (min(combined_mat[row_idx][col_idx-1]) < 0) \
                and (col_idx-2 >= 0) and (max(combined_mat[row_idx][col_idx-2]) == 0) \
                and (col_idx-3 >= 0) and (min(combined_mat[row_idx][col_idx-3]) < 0) ):

            user_high_score, user_high_score_row_idx, user_high_score_col_idx = update_user(row_idx, col_idx)
            print("(HIGHEST SCORE USER) row_idx:", user_high_score_row_idx, "col_idx:", user_high_score_col_idx)
            return user_high_score, user_high_score_row_idx, user_high_score_col_idx

    ################################################################################

    ###################################################################################
    # if user one POP away from horizontal win is avaialable #

        '''
            4 Scenarios:

                    BRRB
        (Eaxmple 1) RRBR
                    BBRB
                        ^


            Both of the above scenarios will be a direct win for R
        '''
    if (check_getWay_user == 0 and check_Way_user == -3): # if direct horizontal win is available, give computer direct win
        if ( (col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[row_idx][col_idx+1]) != 0) \
                and (row_idx+1<= len(combined_mat[0])-1) ) \
            or ( (col_idx-3 >= 0) and (max(combined_mat[row_idx][col_idx-3]) != 0) \
                and (row_idx+1<= len(combined_mat[0])-1) ):
            
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

            user_high_score, user_high_score_row_idx, user_high_score_col_idx = update_user(row_idx, col_idx)
            print("(HIGHEST SCORE USER) row_idx:", user_high_score_row_idx, "col_idx:", user_high_score_col_idx)
            return user_high_score, user_high_score_row_idx, user_high_score_col_idx
        
    
    if (check_getWay_user == 0 and check_Way_user == -2):

        if ( (col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[row_idx][col_idx+1]) != 0) \
                and (col_idx+2 <= len(combined_mat[0])-1) and (max(combined_mat[row_idx][col_idx+2]) < 0) \
                and (col_idx-1 >= 0) and (max(combined_mat[row_idx][col_idx-1]) < 0) \
                and (row_idx+1<= len(combined_mat[0])-1) ) \
            or ( (col_idx-1 >= 0) and (max(combined_mat[row_idx][col_idx-1]) < 0) \
                and (col_idx-2 >= 0) and (max(combined_mat[row_idx][col_idx-2]) != 0) \
                and (col_idx-3 >= 0) and (max(combined_mat[row_idx][col_idx-3]) < 0) \
                and (row_idx+1<= len(combined_mat[0])-1) ):

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            user_high_score, user_high_score_row_idx, user_high_score_col_idx = update_user(row_idx, col_idx)
            print("(HIGHEST SCORE USER) row_idx:", user_high_score_row_idx, "col_idx:", user_high_score_col_idx)
            return user_high_score, user_high_score_row_idx, user_high_score_col_idx
        


    else:
        return None


def find_computer_win_strategies(board, turn, get_way_of_computer, way_of_computer):

    ###################################################################################
    # if direct POP horizontal win is avaialable, give computer direct win #

    '''
        4 Scenarios:

                BRRB
    (Eaxmple 1) RRBR
                BBRB
                    ^


        Both of the above scenarios will be a direct win for R
    '''
    if (get_way_of_computer == 0 and way_of_computer == 3): # if direct horizontal win is available, give computer direct win
        if (computer_high_score_col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx+1]) != 0) \
            and (computer_high_score_row_idx+1<= len(combined_mat[0])-1):
            
            # Note that invalid_cols only means a column is full
            # if (computer_high_score_col_idx+1 in invalid_cols) and (combined_mat[len(combined_mat[0])-1][computer_high_score_col_idx+1] == turn):
            if (board[len(combined_mat[0])-1][computer_high_score_col_idx+1] == turn):
                print("COMPUTER TRYING *POP* FOR DIRECT HORIZONTAL WIN")
                return (computer_high_score_col_idx+1, True)
            
        elif (computer_high_score_col_idx-3 >= 0) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx-3]) != 0) \
            and (computer_high_score_row_idx+1<= len(combined_mat[0])-1):

            # Note that invalid_cols only means a column is full
            # if (computer_high_score_col_idx-3 in invalid_cols) and (combined_mat[len(combined_mat[0])-1][computer_high_score_col_idx-3] == turn):
            if (board[len(combined_mat[0])-1][computer_high_score_col_idx-3] == turn):
                print("COMPUTER TRYING *POP* FOR DIRECT HORIZONTAL WIN")
                return (computer_high_score_col_idx-3, True)
        
    
    if (get_way_of_computer == 0 and way_of_computer == 2):

        if ( (computer_high_score_col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx+1]) != 0) \
            and (computer_high_score_col_idx+2 <= len(combined_mat[0])-1) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx+2]) > 0) \
            and (computer_high_score_col_idx-1 >= 0) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx-1]) > 0) \
            and (computer_high_score_row_idx+1<= len(combined_mat[0])-1) ):
            
            # Note that invalid_cols only means a column is full
            # if (computer_high_score_col_idx+1 in invalid_cols) and (combined_mat[len(combined_mat[0])-1][computer_high_score_col_idx+1] == turn):
            print("length:", len(combined_mat[0])-1)
            print("board:", board)
            print("board length:", len(board), len(board[0]), len(board[1]))
            if (board[len(combined_mat[0])-1][computer_high_score_col_idx+1] == turn):
                print("COMPUTER TRYING *POP* FOR DIRECT NON-CONTIGUOUS HORIZONTAL WIN")
                return (computer_high_score_col_idx+1, True)
        
        elif ( (computer_high_score_col_idx-1 >= 0) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx-1]) > 0) \
            and (computer_high_score_col_idx-2 >= 0) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx-2]) != 0) \
            and (computer_high_score_col_idx-3 >= 0) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx-3]) > 0) \
            and (computer_high_score_row_idx+1<= len(combined_mat[0])-1) ):

            # Note that invalid_cols only means a column is full
            # if (computer_high_score_col_idx-2 in invalid_cols) and (combined_mat[len(combined_mat[0])-1][computer_high_score_col_idx-2] == turn): 
            if (board[len(combined_mat[0])-1][computer_high_score_col_idx-2] == turn): 
                print("COMPUTER TRYING *POP* FOR DIRECT NON-CONTIGUOUS HORIZONTAL WIN") # Note that invalid_cols only means a column is full
                return (computer_high_score_col_idx-2, True)
            
    ###################################################################################
    # if direct non-contiguous horizontal win is avaialable, give computer direct win #

        '''
            2 Scenarios:
                (1) RR_R
                (2) R_RR

            Both of the above scenarios will be a direct win for R
        '''
    if (get_way_of_computer == 0 and way_of_computer == 2):

        if ( (computer_high_score_col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx+1]) == 0) \
            and (computer_high_score_col_idx+2 <= len(combined_mat[0])-1) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx+2]) > 0) \
            and (computer_high_score_col_idx-1 >= 0) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx-1]) > 0) ):

            print("COMPUTER TRYING FOR DIRECT NON-CONTIGUOUS HORIZONTAL WIN")
            return (computer_high_score_col_idx+1, False)
        
        elif ( (computer_high_score_col_idx-1 >= 0) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx-1]) > 0) \
            and (computer_high_score_col_idx-2 >= 0) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx-2]) == 0) \
            and (computer_high_score_col_idx-3 >= 0) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx-3]) > 0) ):

            print("COMPUTER TRYING FOR DIRECT NON-CONTIGUOUS HORIZONTAL WIN")
            return (computer_high_score_col_idx-2, False)

    ###################################################################################


    #######################################################################
    # if direct main diagonal win is avaialable, give computer direct win #
    if (get_way_of_computer == 2 and way_of_computer == 3):
        if (computer_high_score_row_idx-1 >= 0) and (computer_high_score_col_idx-1 >= 0) and \
            (max(combined_mat[computer_high_score_row_idx-1][computer_high_score_col_idx-1]) == 0):

            selected_row = computer_high_score_row_idx-1
            # check if this column is actually possible #
            for i in range(len(board)-1, -1, -1): # iterating over board's height
                if board[i][computer_high_score_col_idx-1] == 0:
                    insert_row = i
                    break
            
            if (insert_row == selected_row):
                print("COMPUTER TRYING FOR DIRECT MAIN DIAGONAL WIN")
                return (computer_high_score_col_idx-1, False)

        elif (computer_high_score_row_idx+3 <= len(combined_mat)-2) and (computer_high_score_col_idx+3 <= len(combined_mat[0])-1) and \
            (max(combined_mat[computer_high_score_row_idx+3][computer_high_score_col_idx+3]) == 0):

            selected_row = computer_high_score_row_idx+3
            # check if this column is actually possible #
            for i in range(len(board)-1, -1, -1): # iterating over board's height
                if board[i][computer_high_score_col_idx+3] == 0:
                    insert_row = i
                    break
            
            if (insert_row == selected_row):
                print("COMPUTER TRYING FOR DIRECT MAIN DIAGONAL WIN")
                return (computer_high_score_col_idx+3, False)
    #######################################################################


    ############################################################################
    # if direct reflected diagonal win is avaialable, give computer direct win #
    if (get_way_of_computer == 3 and way_of_computer == 3):
        if (computer_high_score_row_idx-1 >= 0) and (computer_high_score_col_idx+1 <= len(combined_mat[0])-1) and \
            (max(combined_mat[computer_high_score_row_idx-1][computer_high_score_col_idx+1]) == 0):

            selected_row = computer_high_score_row_idx-1
            # check if this column is actually possible #
            for i in range(len(board)-1, -1, -1): # iterating over board's height
                if board[i][computer_high_score_col_idx+1] == 0:
                    insert_row = i
                    break
            
            if (insert_row == selected_row):
                print("COMPUTER TRYING FOR DIRECT REFLECTED DIAGONAL WIN")
                return (computer_high_score_col_idx+1, False)
        
        elif (computer_high_score_row_idx+3 <= len(combined_mat)-2) and (computer_high_score_col_idx-3 >= 0) and \
            (max(combined_mat[computer_high_score_row_idx+3][computer_high_score_col_idx-3]) == 0):

            selected_row = computer_high_score_row_idx+3
            # check if this column is actually possible #
            for i in range(len(board)-1, -1, -1): # iterating over board's height
                if board[i][computer_high_score_col_idx-3] == 0:
                    insert_row = i
                    break
            
            if (insert_row == selected_row):
                print("COMPUTER TRYING FOR DIRECT REFLECTED DIAGONAL WIN")
                return (computer_high_score_col_idx-3, False)
    ############################################################################


    '''
        We will first cover the standard cases for 1 and 2 consecutive computer discs:
        1) horizontal manner
        2) vertical manner

        special cases of 1) main diagonal, 2) reflected diagonal, 3) non-contiguous horizontal
        are done first
    '''

    # START OF 3 SCORES #
    if (get_way_of_computer == 0 and way_of_computer == 3): # if direct horizontal win is available, give computer direct win
        if (computer_high_score_col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx+1]) == 0):
            print("COMPUTER TRYING FOR DIRECT HORIZONTAL WIN")
            return (computer_high_score_col_idx+1, False)
        
        elif (computer_high_score_col_idx-3 >= 0) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx-3]) == 0):
            print("COMPUTER TRYING FOR DIRECT HORIZONTAL WIN")
            return (computer_high_score_col_idx-3, False)

    elif (get_way_of_computer == 1 and way_of_computer == 3): # if direct vertical win is avaialable, give computer direct win
        if (computer_high_score_row_idx-1 >= 0) and (max(combined_mat[computer_high_score_row_idx-1][computer_high_score_col_idx]) == 0):
            print("COMPUTER TRYING FOR DIRECT VERTICAL WIN")
            return (computer_high_score_col_idx, False)
    # END OF 3 SCORES #
    ###################################################################################

    # START OF 2 SCORES #
    if (get_way_of_computer == 0 and way_of_computer == 2):
        if ( (computer_high_score_col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx+1]) == 0) ):
            print("COMPUTER CREATING CHANCES FOR HORIZONTAL WIN")
            return (computer_high_score_col_idx+1, False)
        
        elif ( (computer_high_score_col_idx-2 >= 0) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx-2]) == 0) ): # if there is a different colored disc vertically on top, dont update
            print("COMPUTER CREATING CHANCES FOR HORIZONTAL WIN")
            return (computer_high_score_col_idx-2, False)

    elif (get_way_of_computer == 1 and way_of_computer == 2):
        if (computer_high_score_row_idx-1 >= 0) and (max(combined_mat[computer_high_score_row_idx-1][computer_high_score_col_idx]) == 0):
            print("COMPUTER CREATING CHANCES FOR VERTICAL WIN")
            return (computer_high_score_col_idx, False)
    # END OF 2 SCORES #

    # START OF 1 SCORE #
    if (get_way_of_computer == 0 and way_of_computer == 1):
        if ( (computer_high_score_col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx+1]) == 0) ):
            print("COMPUTER CREATING CHANCES FOR HORIZONTAL WIN")
            return (computer_high_score_col_idx+1, False)
        
        elif ( (computer_high_score_col_idx-1 >= 0) and (max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx-1]) == 0) ): # if there is a different colored disc vertically on top, dont update
            print("COMPUTER CREATING CHANCES FOR HORIZONTAL WIN")
            return (computer_high_score_col_idx-1, False)
            
            
    elif (get_way_of_computer == 1 and way_of_computer == 1):
        if (computer_high_score_row_idx-1 >= 0) and (max(combined_mat[computer_high_score_row_idx-1][computer_high_score_col_idx]) == 0):
            print("COMPUTER CREATING CHANCES FOR VERTICAL WIN")
            return (computer_high_score_col_idx, False)
    # END OF 1 SCORE #

    ## END ##    
    
    else:
        return None
    


def find_block_user_win_strategies(board, turn, get_way_of_user, way_of_user, user_high_score_row_idx, user_high_score_col_idx):

    # print()
    # print("USER HIGH SCORE ROW IDX:", user_high_score_row_idx, "USER HIGH SCORE COL IDX:", user_high_score_col_idx)
    # print("WAY OF USER:", way_of_user, "GET WAY OF USER:", get_way_of_user)
    # print()

    if (get_way_of_user == 0 and way_of_user == -3): # user 1 disc from winning horizonatally

        print("COMPUTER BLOCKING USER FROM DIRECT WIN")
        if (user_high_score_col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[user_high_score_row_idx][user_high_score_col_idx+1]) == 0):
            if (user_high_score_row_idx+1 == len(board)):
                print("PREVENT DIRECT HORIZONTAL WIN (A) ...")
                computer_best_col_idx = user_high_score_col_idx+1
                return (computer_best_col_idx, False) # block user from direct horizontal win
            elif (user_high_score_row_idx+1 < len(board)):
                if (board[user_high_score_row_idx+1][user_high_score_col_idx] == 0):
                    pass

        elif (user_high_score_col_idx-3 >= 0) and (max(combined_mat[user_high_score_row_idx][user_high_score_col_idx-3]) == 0):
            print("PREVENT DIRECT HORIZONTAL WIN (B) ...")
            computer_best_col_idx = user_high_score_col_idx - 3
            return (computer_best_col_idx, False) # block user from direct horizontal win

    elif (get_way_of_user == 1 and way_of_user == -3): # user 1 disc from winning vertically
        if (user_high_score_row_idx-1 >= 0) and (max(combined_mat[user_high_score_row_idx-1][user_high_score_col_idx]) == 0):
            print("COMPUTER BLOCKING USER FROM DIRECT VERTICAL WIN")
            computer_best_col_idx = user_high_score_col_idx
            return (computer_best_col_idx, False) # block user from direct vertical win

    
    #######################################################################
    # user 1 disc from main diagonal win #
    if (get_way_of_user == 2 and way_of_user == -3):
        print("COMPUTER BLOCKING USER FROM DIRECT MAIN DIAGONAL WIN")
        if (user_high_score_row_idx-1 >= 0) and (user_high_score_col_idx-1 >= 0) and \
            (max(combined_mat[user_high_score_row_idx-1][user_high_score_col_idx-1]) == 0):

            selected_row = user_high_score_row_idx-1
            # check if this column is actually possible #
            for i in range(len(board)-1, -1, -1): # iterating over board's height
                if board[i][user_high_score_col_idx-1] == 0:
                    insert_row = i
                    break
            
            if (insert_row == selected_row):
                print("COMPUTER BLOCKING USER FROM DIRECT MAIN DIAGONAL WIN (EXECUTED)")
                return (user_high_score_col_idx-1, False)

        elif (user_high_score_row_idx+3 <= len(combined_mat)-2) and (user_high_score_col_idx+3 <= len(combined_mat[0])-1) and \
            (max(combined_mat[user_high_score_row_idx+3][user_high_score_col_idx+3]) == 0):

            selected_row = user_high_score_row_idx+3
            # check if this column is actually possible #
            for i in range(len(board)-1, -1, -1): # iterating over board's height
                if board[i][user_high_score_col_idx+3] == 0:
                    insert_row = i
                    break
            
            if (insert_row == selected_row):
                print("COMPUTER BLOCKING USER FROM DIRECT MAIN DIAGONAL WIN (EXECUTED)")
                return (user_high_score_col_idx+3, False)
    #######################################################################


    ############################################################################
    # user 1 disc from reflected diagonal win #
    if (get_way_of_user == 3 and way_of_user == -3):
        print("COMPUTER BLOCKING USER FROM DIRECT REFLECTED DIAGONAL WIN")
        if (user_high_score_row_idx-1 >= 0) and (user_high_score_col_idx+1 <= len(combined_mat[0])-1) and \
            (max(combined_mat[user_high_score_row_idx-1][user_high_score_col_idx+1]) == 0):

            selected_row = user_high_score_row_idx-1
            # check if this column is actually possible #
            for i in range(len(board)-1, -1, -1): # iterating over board's height
                if board[i][user_high_score_col_idx+1] == 0:
                    insert_row = i
                    break
            
            if (insert_row == selected_row):
                print("COMPUTER BLOCKING USER FROM DIRECT REFLECTED DIAGONAL WIN (EXECUTED)")
                return (user_high_score_col_idx+1, False)
        
        elif (user_high_score_row_idx+3 <= len(combined_mat)-2) and (user_high_score_col_idx-3 >= 0) and \
            (max(combined_mat[user_high_score_row_idx+3][user_high_score_col_idx-3]) == 0):

            selected_row = user_high_score_row_idx+3
            # check if this column is actually possible #
            for i in range(len(board)-1, -1, -1): # iterating over board's height
                if board[i][user_high_score_col_idx-3] == 0:
                    insert_row = i
                    break
            
            if (insert_row == selected_row):
                print("COMPUTER BLOCKING USER FROM DIRECT REFLECTED DIAGONAL WIN (EXECUTED)")
                return (user_high_score_col_idx-3, False)
    ############################################################################

    ############################################################################
    # user 1 disc from NON-CONTIGUOUS HORIZONTAL win #
        '''
            2 Scenarios:
                (1) RR_R
                (2) R_RR

            Both of the above scenarios will be a direct win for R
        '''
    if (get_way_of_user == 0 and way_of_user == -2):
        if (user_high_score_col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[user_high_score_row_idx][user_high_score_col_idx+1]) == 0) \
            and (user_high_score_col_idx+2 <= len(combined_mat[0])-1) and (min(combined_mat[user_high_score_row_idx][user_high_score_col_idx+2]) < 0) \
            and (user_high_score_col_idx-1 >= 0) and (min(combined_mat[user_high_score_row_idx][user_high_score_col_idx-1]) < 0):

            print("COMPUTER BLOCKING USER FROM DIRECT NON-CONTIGUOUS HORIZONTAL win")
            return (user_high_score_col_idx+1, False)

        elif (user_high_score_col_idx-1 >= 0) and (min(combined_mat[user_high_score_row_idx][user_high_score_col_idx-1]) < 0) \
            and (user_high_score_col_idx-2 >= 0) and (max(combined_mat[user_high_score_row_idx][user_high_score_col_idx-2]) == 0) \
            and (user_high_score_col_idx-3 >= 0) and (min(combined_mat[user_high_score_row_idx][user_high_score_col_idx-3]) < 0):

            print("COMPUTER BLOCKING USER FROM DIRECT NON-CONTIGUOUS HORIZONTAL win")
            return (user_high_score_col_idx-2, False)

    ###################################################################################

    # IF user 1 POP AWAY from win, BLOCK user with a POP #
    ###################################################################################

        '''
            4 Scenarios:

                    BRRB
        (Eaxmple 1) RRBR
                    BBRB
                        ^


            Both of the above scenarios will be a direct win for R
        '''
    if (get_way_of_user == 0 and way_of_user == -3): # if direct horizontal win is available, give computer direct win

        print("IS THIS RUNNING @ ?")

        if (user_high_score_col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[user_high_score_row_idx][user_high_score_col_idx+1]) != 0) \
            and (user_high_score_row_idx+1<= len(combined_mat[0])-1):

            # Note that invalid_cols only means a column is full

            print("length:", len(combined_mat[0])-1)
            print("board:", board)
            print("board length:", len(board), len(board[0]), len(board[1]))

            if (board[len(combined_mat[0])-1][user_high_score_col_idx] == turn):
                print("COMPUTER BLOCKING USER *POP* WIN with POP")
                return (user_high_score_col_idx, True)
            
            elif (board[len(combined_mat[0])-1][user_high_score_col_idx-1] == turn):
                print("COMPUTER BLOCKING USER *POP* WIN with POP")
                return (user_high_score_col_idx-1, True)
            
            elif (board[len(combined_mat[0])-1][user_high_score_col_idx-2] == turn):
                print("COMPUTER BLOCKING USER *POP* WIN with POP")
                return (user_high_score_col_idx-2, True)
            
            
        elif (user_high_score_col_idx-3 >= 0) and (max(combined_mat[user_high_score_row_idx][user_high_score_col_idx-3]) != 0) \
            and (user_high_score_row_idx+1<= len(combined_mat[0])-1):

            # Note that invalid_cols only means a column is full
            
            if (board[len(combined_mat[0])-1][user_high_score_col_idx-2] == turn):
                print("COMPUTER BLOCKING USER *POP* WIN with POP")
                return (user_high_score_col_idx-2, True)
            
            elif (board[len(combined_mat[0])-1][user_high_score_col_idx-1] == turn):
                print("COMPUTER BLOCKING USER *POP* WIN with POP")
                return (user_high_score_col_idx-1, True)
            
            elif (board[len(combined_mat[0])-1][user_high_score_col_idx] == turn):
                print("COMPUTER BLOCKING USER *POP* WIN with POP")
                return (user_high_score_col_idx, True)
        
    
    if (get_way_of_user == 0 and way_of_user == -2):

        print("IS THIS RUNNING @@@ ?")

        if ( (user_high_score_col_idx+1 <= len(combined_mat[0])-1) and (max(combined_mat[user_high_score_row_idx][user_high_score_col_idx+1]) != 0) \
            and (user_high_score_col_idx+2 <= len(combined_mat[0])-1) and (max(combined_mat[user_high_score_row_idx][user_high_score_col_idx+2]) < 0) \
            and (user_high_score_col_idx-1 >= 0) and (max(combined_mat[user_high_score_row_idx][user_high_score_col_idx-1]) < 0) \
            and (user_high_score_row_idx+1<= len(combined_mat[0])-1) ):
            
            # Note that invalid_cols only means a column is full
            # if (computer_high_score_col_idx+1 in invalid_cols) and (combined_mat[len(combined_mat[0])-1][computer_high_score_col_idx+1] == turn):
            print("length:", len(combined_mat[0])-1)
            print("board:", board)
            print("board length:", len(board), len(board[0]), len(board[1]))

            # Note that invalid_cols only means a column is full

            if (board[len(combined_mat[0])-1][user_high_score_col_idx+1+1] == turn):
                print("COMPUTER BLOCKING USER *POP* WIN with POP")
                return (user_high_score_col_idx+1+1, True)
            
            elif (board[len(combined_mat[0])-1][user_high_score_col_idx+1-1] == turn):
                print("COMPUTER BLOCKING USER *POP* WIN with POP")
                return (user_high_score_col_idx, True)
            
            elif (board[len(combined_mat[0])-1][user_high_score_col_idx+1-2] == turn):
                print("COMPUTER BLOCKING USER *POP* WIN with POP")
                return (user_high_score_col_idx-1, True)
                
        
        elif ( (user_high_score_col_idx-1 >= 0) and (max(combined_mat[user_high_score_row_idx][user_high_score_col_idx-1]) < 0) \
            and (user_high_score_col_idx-2 >= 0) and (max(combined_mat[user_high_score_row_idx][user_high_score_col_idx-2]) != 0) \
            and (user_high_score_col_idx-3 >= 0) and (max(combined_mat[user_high_score_row_idx][user_high_score_col_idx-3]) < 0) \
            and (user_high_score_row_idx+1<= len(combined_mat[0])-1) ):

            # Note that invalid_cols only means a column is full

            print("length:", len(combined_mat[0])-1)
            print("board:", board)
            print("board length:", len(board), len(board[0]), len(board[1]))

            if (board[len(combined_mat[0])-1][user_high_score_col_idx] == turn):
                print("COMPUTER BLOCKING USER *POP* WIN with POP")
                return (user_high_score_col_idx, True)
            
            elif (board[len(combined_mat[0])-1][user_high_score_col_idx-1] == turn):
                print("COMPUTER BLOCKING USER *POP* WIN with POP")
                return (user_high_score_col_idx-1, True)
            
            elif (board[len(combined_mat[0])-1][user_high_score_col_idx-3] == turn):
                print("COMPUTER BLOCKING USER *POP* WIN with POP")
                return (user_high_score_col_idx-3, True)
            
        
    ###################################################################################
    ## END ##

    else:
        return None


def find_computer_random_move(board, turn):

    # DEBUG #
    print("BOARD IN FIND_COMP_RANDOM_MOVE():", board)

    random_pop_list = [True, False]
    while True:

        print("Computer -- Current FULL Columns:", invalid_cols) # invalid_cols is defined globally

        # num_rows_initial = len(board)
        # # print("computer_move() DEBUG:", board)
        # if (num_rows_initial > len(one_dim_to_two_dim(board))): # if board is in 1D
        #     # print("CONNNVVEERRTTING")
        #     board = one_dim_to_two_dim(board) # change board to 2D for len(board[0])-1 to work


        random_column = random.randint(0, len(board[0])-1)
        random_pop = random_pop_list[random.randint(0,1)]

        if random_pop:  # Handle the case where random_pop is True
            if invalid_cols:  # Ensure there are columns available to pop
                random_column = random.choice(invalid_cols)  # Pick a column from invalid_cols
                invalid_cols.remove(random_column)  # Remove the picked column from invalid_cols
            else:
                continue  # If no columns are in invalid_cols, try again

        copy_board = two_dim_to_one_dim(board) # for input to check_move()
        if (check_move(copy_board, turn, random_column, random_pop) == True):
            print("COMPUTER DOES RANDOM MOVE")
            return random_column, random_pop # returns col, pop (Boolean)



def initialize_combined_matrix(computer_disc_locs, user_disc_locs, computer_highest_disc_row_idx, user_highest_disc_row_idx):
    """
    Initialize the combined matrix by marking the computer and user discs 
    and calculating connection counts for each cell.
    
    Args:
        computer_disc_locs (list of tuples): Positions of computer discs.
        user_disc_locs (list of tuples): Positions of user discs.
        computer_highest_disc_row_idx (int): Topmost row index for computer discs.
        user_highest_disc_row_idx (int): Topmost row index for user discs.
    
    Each cell in combined_mat is a list of four integers that store connection counts for:
        Horizontal connections (index 0).
        Vertical connections (index 1).
        Main diagonal connections (index 2).
        Reflected diagonal connections (index 3).
    ** Whether 0 or 1 or 2 or 3, depends on connection_idx. **

    Returns:
        list: Updated combined matrix.
    """
    
    # Initialize discs for the computer
    for row, col in computer_disc_locs:
        combined_mat[row][col] = [1, 1, 1, 1]

    # Initialize discs for the user
    for row, col in user_disc_locs:
        combined_mat[row][col] = [-1, -1, -1, -1]

    def update_connections(row_idx, col_idx, highest_row_idx, is_computer):
        """Update connections for a cell based on neighboring cells."""
        directions = [(0, -1, 0), (1, 0, 1), (1, 1, 2), (1, -1, 3)]  # (row_offset, col_offset, connection_idx)
        current_cell = combined_mat[row_idx][col_idx]
        
        # Update highest disc row index
        if is_computer:
            if row_idx < highest_row_idx[0]:
                highest_row_idx[0] = row_idx
        else:
            if row_idx < highest_row_idx[1]:
                highest_row_idx[1] = row_idx

        for row_offset, col_offset, conn_idx in directions:
            neighbor_row, neighbor_col = row_idx + row_offset, col_idx + col_offset
            # Ensure neighbor is within bounds and has the same sign
            if 0 <= neighbor_row < len(combined_mat) and 0 <= neighbor_col < len(combined_mat[0]):
                neighbor_cell = combined_mat[neighbor_row][neighbor_col]
                if current_cell[conn_idx] * neighbor_cell[conn_idx] > 0:  # Same sign check
                    current_cell[conn_idx] += neighbor_cell[conn_idx]

    # Process the board bottom-to-top
    highest_row_idx = [computer_highest_disc_row_idx, user_highest_disc_row_idx]
    for row_idx in reversed(range(len(combined_mat))):  # Bottom-to-top
        for col_idx in range(len(combined_mat[row_idx])):  # Left-to-right
            cell_value = combined_mat[row_idx][col_idx]
            if max(cell_value) > 0:  # Computer's disc
                update_connections(row_idx, col_idx, highest_row_idx, is_computer=True)
            elif min(cell_value) < 0:  # User's disc
                update_connections(row_idx, col_idx, highest_row_idx, is_computer=False)

    return combined_mat




def computer_move(board, turn, level):
    # implement your function here

    # global computer_high_score
    computer_high_score = 0
    global computer_high_score_row_idx
    computer_high_score_row_idx = 0
    global computer_highest_disc_row_idx
    computer_highest_disc_row_idx = 100 # the smaller the index the higher the disc
    # global computer_highest_disc_col_idx
    # computer_highest_disc_col_idx = 0 ## __________ ******** NOT IN USED ********
    global computer_high_score_col_idx
    computer_high_score_col_idx = 0

    computer_best_col_idx = 0 # this will be the optimal selection by computer

    global user_high_score
    user_high_score = 0
    global user_high_score_row_idx
    user_high_score_row_idx = 0
    global user_highest_disc_row_idx
    user_highest_disc_row_idx = 100 # the smaller the index the higher the disc
    # global user_highest_disc_col_idx
    # user_highest_disc_col_idx = 0 ## __________ ******** NOT IN USED ********
    global user_high_score_col_idx
    user_high_score_col_idx = 0


    num_rows_initial = len(board)
    # print("computer_move() DEBUG:", board)
    if (num_rows_initial > len(one_dim_to_two_dim(board))): # if board is in 1D
        # print("CONNNVVEERRTTING")
        board = one_dim_to_two_dim(board) # change board to 2D for len(board[0])-1 to work

    # print("BOARD IN COMPUTER_MOVE():", board)

    print("Computer is making a move...")
    time.sleep(1.3)
    print()
    
    # print("board's length:", len(board))

    if (level == 1): # random moves
        random_column, random_pop = find_computer_random_move(board, turn) # returns col, pop (Boolean)
        return (random_column, random_pop)
    

    if (level == 2 or level == 3):

        global combined_mat # * Global for update_computer() and update_user()
        combined_mat = [[[0,0,0,0] for i in range(len(board[0]))] for j in range(len(board))] # score matrix [0,0,0,0] for score per square for horizontal, vertical, main diag, reflected diag #
            
    
    if (level == 2): # Medium


        computer_disc_locs = []
        user_disc_locs = []
        

        '''
            add computer_disc_locs and user_disc_locs depending on which player computer is
        '''

        if (turn == 1): # computer is player 1
            for row_idx, row in enumerate(board):
                for col_idx, val in enumerate(row):
                    if (row_idx < len(board)):
                        if (val == 1):
                            computer_disc_locs.append((row_idx, col_idx))
                        elif (val == 2):
                            user_disc_locs.append((row_idx, col_idx))

        else: # computer is player 2
            for row_idx, row in enumerate(board):
                for col_idx, val in enumerate(row):
                    if (row_idx < len(board)):
                        if (val == 1):
                            user_disc_locs.append((row_idx, col_idx))
                        elif (val == 2):
                            computer_disc_locs.append((row_idx, col_idx))
                    

        combined_mat = initialize_combined_matrix(computer_disc_locs, user_disc_locs, computer_highest_disc_row_idx, user_highest_disc_row_idx)


        for row_idx, row in reversed(list(enumerate(combined_mat))): # go from bottom to top of board
            for col_idx, val in enumerate(combined_mat[row_idx]):
                
                # if (row_idx <= 2 and combined_mat[row_idx][col_idx][1] == -1) or (row_idx <= 2 and combined_mat[row_idx][col_idx][1] == -1):
                #     invalid_cols.append(col_idx)

                if (min(combined_mat[row_idx][col_idx]) < 0): # this is user entry
                    if (min(combined_mat[row_idx][col_idx]) <= user_high_score):

                        # do updates #
                        check_Way_user = min(combined_mat[row_idx][col_idx]) # see how user is trying to win (e.g. horizontally, vertically etc.)
                        check_getWay_user = combined_mat[row_idx][col_idx].index(check_Way_user)

                        if (check_user(board, row_idx, col_idx, check_getWay_user, check_Way_user)):
                            user_high_score, user_high_score_row_idx, user_high_score_col_idx = check_user(board, row_idx, col_idx, check_getWay_user, check_Way_user)
                            break


                elif (max(combined_mat[row_idx][col_idx]) > 0): # this is computer entry
                    if (max(combined_mat[row_idx][col_idx]) >= computer_high_score):
                                    
                        # do updates #

                        check_Way_computer = max(combined_mat[row_idx][col_idx]) # see how computer is trying to win (e.g. horizontally, vertically etc.)
                        check_getWay_computer = combined_mat[row_idx][col_idx].index(check_Way_computer)

                        if (check_computer(board, row_idx, col_idx, check_getWay_computer, check_Way_computer)):
                            computer_win, computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx = check_computer(board, row_idx, col_idx, check_getWay_computer, check_Way_computer)
                            print("computer high score col:", computer_high_score_col_idx)
                            if computer_win:
                                break
                
                else:
                    continue


        
        #                           ******************** DEBUG                  --------------#
        # print("combined_mat:")
        # for row in combined_mat:
        #     print(row)
        #     print()



        ## START OF CHECK USER (BLOCK USER FROM DIRECT WIN) ##
        way_of_user = min(combined_mat[user_high_score_row_idx][user_high_score_col_idx]) # see how user is trying to win (e.g. horizontally, vertically etc.)
        get_way_of_user = combined_mat[user_high_score_row_idx][user_high_score_col_idx].index(way_of_user)

        if (find_block_user_win_strategies(board, turn, get_way_of_user, way_of_user, user_high_score_row_idx, user_high_score_col_idx)):
            block_user_win_column, block_user_win_to_pop = find_block_user_win_strategies(board, turn, get_way_of_user, way_of_user, user_high_score_row_idx, user_high_score_col_idx)
            return (block_user_win_column, block_user_win_to_pop)



        ## START OF CHECK COMPUTER (GIVE COMPUTER DIRECT WIN IF AVAILABLE) ##
        way_of_computer = max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx])
        get_way_of_computer = combined_mat[computer_high_score_row_idx][computer_high_score_col_idx].index(way_of_computer)

        if (find_computer_win_strategies(board, turn, get_way_of_computer, way_of_computer)):
            computer_win_column, computer_to_pop = find_computer_win_strategies(board, turn, get_way_of_computer, way_of_computer)
            return (computer_win_column, computer_to_pop)

        
        
        else: # Find random move for computer
            random_column, random_pop = find_computer_random_move(board, turn) # returns col, pop (Boolean)
            return (random_column, random_pop)


    elif (level == 3): # HARD

        computer_best_col_idx = 0 # this will be the optimal selection by computer

        computer_disc_locs = []
        user_disc_locs = []

        if (turn == 1): # computer is player 1
            for row_idx, row in enumerate(board):
                for col_idx, val in enumerate(row):
                    if (row_idx < len(board)):
                        if (val == 1):
                            computer_disc_locs.append((row_idx, col_idx))
                        elif (val == 2):
                            user_disc_locs.append((row_idx, col_idx))

        else: # computer is player 2
            for row_idx, row in enumerate(board):
                for col_idx, val in enumerate(row):
                    if (row_idx < len(board)):
                        if (val == 1):
                            user_disc_locs.append((row_idx, col_idx))
                        elif (val == 2):
                            computer_disc_locs.append((row_idx, col_idx))


        combined_mat = initialize_combined_matrix(computer_disc_locs, user_disc_locs, computer_highest_disc_row_idx, user_highest_disc_row_idx)


        for row_idx, row in reversed(list(enumerate(combined_mat))): # go from bottom to top of board
            for col_idx, val in enumerate(combined_mat[row_idx]):
                
                # if (row_idx <= 2 and combined_mat[row_idx][col_idx][1] == -1) or (row_idx <= 2 and combined_mat[row_idx][col_idx][1] == -1):
                #     invalid_cols.append(col_idx)

                if (min(combined_mat[row_idx][col_idx]) < 0): # this is user entry
                    if (min(combined_mat[row_idx][col_idx]) <= user_high_score):

                        # do updates #
                        check_Way_user = min(combined_mat[row_idx][col_idx]) # see how user is trying to win (e.g. horizontally, vertically etc.)
                        check_getWay_user = combined_mat[row_idx][col_idx].index(check_Way_user)

                        if (check_user(board, row_idx, col_idx, check_getWay_user, check_Way_user)):
                            user_high_score, user_high_score_row_idx, user_high_score_col_idx = check_user(board, row_idx, col_idx, check_getWay_user, check_Way_user)
                            break


                elif (max(combined_mat[row_idx][col_idx]) > 0): # this is computer entry
                    if (max(combined_mat[row_idx][col_idx]) >= computer_high_score):
                                    
                        # do updates #

                        check_Way_computer = max(combined_mat[row_idx][col_idx]) # see how computer is trying to win (e.g. horizontally, vertically etc.)
                        check_getWay_computer = combined_mat[row_idx][col_idx].index(check_Way_computer)

                        if (check_computer(board, row_idx, col_idx, check_getWay_computer, check_Way_computer)):
                            computer_win, computer_high_score, computer_high_score_row_idx, computer_high_score_col_idx = check_computer(board, row_idx, col_idx, check_getWay_computer, check_Way_computer)
                            print("computer high score col:", computer_high_score_col_idx)
                            if computer_win:
                                break
                
                else:
                    continue

        
        #                           ******************** DEBUG                  --------------#
        # print("combined_mat:")
        # for row in combined_mat:
        #     print(row)
        #     print()



        ## START OF CHECK USER (BLOCK USER FROM DIRECT WIN) ##
        way_of_user = min(combined_mat[user_high_score_row_idx][user_high_score_col_idx]) # see how user is trying to win (e.g. horizontally, vertically etc.)
        get_way_of_user = combined_mat[user_high_score_row_idx][user_high_score_col_idx].index(way_of_user)

        if (find_block_user_win_strategies(board, turn, get_way_of_user, way_of_user, user_high_score_row_idx, user_high_score_col_idx)):
            block_user_win_column, block_user_win_to_pop = find_block_user_win_strategies(board, turn, get_way_of_user, way_of_user, user_high_score_row_idx, user_high_score_col_idx)
            return (block_user_win_column, block_user_win_to_pop)
        


        ## START OF CHECK COMPUTER (GIVE COMPUTER DIRECT WIN IF AVAILABLE) ##
        way_of_computer = max(combined_mat[computer_high_score_row_idx][computer_high_score_col_idx])
        get_way_of_computer = combined_mat[computer_high_score_row_idx][computer_high_score_col_idx].index(way_of_computer)

        if (find_computer_win_strategies(board, turn, get_way_of_computer, way_of_computer)):
            computer_win_column, computer_to_pop = find_computer_win_strategies(board, turn, get_way_of_computer, way_of_computer)
            return (computer_win_column, computer_to_pop)

        # else: # COMPUTER ATTACKS
        #     computer_attacks(get_way_of_computer, way_of_computer)

        else: # Find random move for computer
            random_column, random_pop = find_computer_random_move(board, turn) # returns col, pop (Boolean)
            return (random_column, random_pop)
         
                
    
def display_board(board):
    # implement your function here

    # convert board from 1D to 2D #
    board = one_dim_to_two_dim(board)
    print("board's length:", len(board))
    
    print("\n")
    print(" A GAME OF CONNECT FOUR! ")
    print("\n")
    for row in board:
        # print(" ".join(row))
        print(row)
    print("\n")


def menu():

    

    ##############################

    # board = []

    current_player = 2 # set to 2 but will be decremented to 1. So PLAYER 1 always first to start

    winner1 = False # this is for human vs human

    winner2 = False # this is for human vs computer
    machine_turn = False # human vs computer

    start_game = False

    getboardheight = 0
    human_opponent = True # True by default
    opponent_type_selected = False

    get_computer_difficulty = None

    # implement your function here
    print()
    print("!! WELCOME TO CONNECT FOUR MENU !!")
    print()
    print("                     MENU:")
    print("--------------------------------------------------")
    print("CHOOSE YOUR PLAYER:")
    print("PLAYER 1 - DISC WILL BE LABELLED 1")
    print("PLAYER 2 - DISC WILL BE LABELLED 2")
    print("##################################")
    print()
    print()
    print("*************************************")
    print("*PLEASE READ CAREFULLY* (GAME DESIGN):")
    print("BOARD AREA IS MARKED WITH NUMBERS 0, 1 and 2")
    print("*************************************")
    print()
    print()

    user_preferred_player = None
    while (user_preferred_player != 1 and user_preferred_player != 2):
        user_preferred_player = int(input("CHOOSE YOUR PLAYER: ENTER THE NUMBER (1 / 2) ").strip())

    if (user_preferred_player == 1):
        print()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("YOU ARE PLAYER 1! DISC LABELLED AS 1!")
        print("OPPONENT IS PLAYER 2, DISC LABELLED AS 2!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print()
    else:
        print()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("YOU ARE PLAYER 2! DISC LABELLED AS 2!")
        print("OPPONENT IS PLAYER 1, DISC LABELLED AS 1!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print()

    # while (not(6 <= getboardheight <= 10)):
    #     getboardheight = int(input("Select Number of Rows (Choose a number from 6-10)").strip())

    while (not(opponent_type_selected)):
        get_opponent_type =  input("Play Against A Computer? (y/n)").strip()
        if (get_opponent_type == "y" or get_opponent_type == "Y" or get_opponent_type == "n" or get_opponent_type == "N"):
            opponent_type_selected = True
            if (get_opponent_type == "y" or get_opponent_type == "Y"):
                human_opponent = False

    # if selected computer player, ask user to select difficulty of computer #
    while (not human_opponent):
        get_computer_difficulty = int(input("Enter Number For Computer Difficulty (1=Easy / 2=Medium / 3=Hard)").strip())
        if (get_computer_difficulty == 1 or get_computer_difficulty == 2 or get_computer_difficulty == 3):
            break

    start_game = True

    # boardheight = getboardheight
    boardheight = 7
    boardwidth = 7


    # generate board #
    for i in range(boardheight):
        board.append([0] * boardwidth)
        
    

    # start game #
    if (start_game):

        # convert 2D board to 1D board (FOR INPUT) #
        board = two_dim_to_one_dim(board)

        print()
        print("GAME HAS STARTED")
        display_board(board)


    if (human_opponent == True):

        '''
            * Board is now in 1D, change to 2D for DATA MANIPULATION if necessary
        '''

        while (winner1 == False):
                
            while True:

                if (current_player == 1):
                    current_player += 1
                    print("It is PLAYER", current_player, "Turn.")
                else:
                    current_player -= 1
                    print("It is PLAYER", current_player, "Turn.")

                insert_col_selected = False
                while (not insert_col_selected):
                    insert_col = int(input("Pick a column (1-7): ").strip())

                    # convert 1D board to 2D board (FOR MANIPUlATION) #
                    board = one_dim_to_two_dim(board)

                    if (insert_col > len(board[0]) or insert_col < 0):
                        print("Please Try Another Column!")
                        continue
                    else:
                        break
                insert_col_idx = insert_col - 1

                to_pop_selected = False
                while (not to_pop_selected):
                    to_pop = input("Do you want to pop? Enter Boolean Value (True / False)")
                    if (to_pop != "True" and to_pop != "False"):
                            print("Please Enter A Boolean Value!")
                            print("to_pop value:", to_pop)
                            continue
                    else:
                        if (to_pop == "True"):
                            to_pop = True
                        else:
                            to_pop = False
                        break
                
                # convert 2D board to 1D board (FOR INPUT) #
                board = two_dim_to_one_dim(board)

                if (check_move(board, current_player, insert_col_idx, to_pop) == True):
                    board = apply_move(board, current_player, insert_col_idx, to_pop)

                    '''
                        check if opponent wins first
                    '''

                    who_win = check_victory(board, current_player)
                    if who_win == 0:
                        if current_player == 1:
                            who_win = check_victory(board, 2)
                        elif current_player == 2:
                            who_win = check_victory(board, 1)
                    if (who_win == 1):
                        print("PLAYER 1 wins!")
                        winner1 = True
                        break
                    elif (who_win == 2):
                        print("PLAYER 2 wins!")
                        winner1 = True
                        break
                
                else:
                    # print("No Disc To Be Popped, Please Try Another Column!")
                    continue
                    

    else: # you vs computer

        '''
            * Board is now in 1D, change to 2D for DATA MANIPULATION if necessary
        '''

        while (winner2 == False):
            you_player = user_preferred_player
            
            if (machine_turn == False):
                if (you_player == 1):
                    print("It is YOUR Turn.", "PLAYER", you_player)
                else:
                    print("It is YOUR Turn.", "PLAYER", you_player)
                
                while True:
                    insert_col_selected = False
                    insert_col = None
                    while (not insert_col_selected):
                        insert_col = int(input("Pick a column (1-7): ").strip())

                        # convert 1D board to 2D board (FOR MANIPUlATION) #
                        board = one_dim_to_two_dim(board)

                        if (insert_col > len(board[0]) or insert_col < 0):
                            print("Please Try Another Column!")
                            continue
                        else:
                            break
                    insert_col_idx = insert_col - 1

                    to_pop_selected = False
                    to_pop = None
                    while (not to_pop_selected):
                        to_pop = input("Do you want to pop? Enter Boolean Value (True / False)").strip()
                        if (to_pop != "True" and to_pop != "False"):
                                print("Please Enter A Boolean Value!")
                                print("to_pop value:", to_pop)
                                continue
                        else:
                            if (to_pop == "True"):
                                to_pop = True
                            else:
                                to_pop = False
                            break
                    
                    if (you_player == 1):

                        # convert 2D board to 1D board (FOR INPUT) #
                        board = two_dim_to_one_dim(board)

                        if (check_move(board, you_player, insert_col_idx, to_pop) == True):
                            board = apply_move(board, you_player, insert_col_idx, to_pop)

                            '''
                                check if opponent wins first
                            '''
                            
                            winner2 = check_victory(board, 2)
                            if (winner2 == 2):
                                print("Computer (PLAYER 2) has won!")
                                break
                            elif (winner2 == 1):
                                print("YOU, PLAYER 1 wins!")
                            

                            winner2 = check_victory(board, you_player)
                            if (winner2 == 1):
                                print("YOU, PLAYER", you_player, "wins!")
                                break
                            elif (winner2 == 2):
                                print("PLAYER 2 wins!")
                                break

                            break

                        else:
                            # print("No Disc To Be Popped, Please Try Another Column!")
                            continue
                    
                    elif (you_player == 2):

                        # convert 2D board to 1D board (FOR INPUT) #
                        board = two_dim_to_one_dim(board)

                        if (check_move(board, you_player, insert_col_idx, to_pop) == True):
                            board = apply_move(board, you_player, insert_col_idx, to_pop)
                            
                            '''
                                check if opponent wins first
                            '''

                            winner2 = check_victory(board, 1)
                            if (winner2 == 1):
                                print("Computer (PLAYER 1) has won!")
                                break
                            elif (winner2 == 2):
                                print("YOU, PLAYER 1 wins!")
                                break

                            winner2 = check_victory(board, you_player)
                            if (winner2 == 2):
                                print("YOU, PLAYER", you_player, "wins!")
                                break
                            elif (winner2 == 1):
                                print("COMPUTER (PLAYER 1) wins!")
                            
                            break

                        else:
                            # print("No Disc To Be Popped, Please Try Another Column!")
                            continue
                
                machine_turn = True

            else:
                if (you_player == 1):
                    
                    computer_move_found = 0
                    while (not computer_move_found):
                        computer_selected_col, computer_pop = computer_move(board, 2, get_computer_difficulty)
                        if check_move(board, 2, computer_selected_col, computer_pop) == True:
                            computer_move_found = 1

                    print("computer_selected_col:", computer_selected_col, "computer_pop:", computer_pop)
                    board = apply_move(board, 2, computer_selected_col, computer_pop)

                    # check if Computer won #
                    winner2 = check_victory(board, 2)
                    if (winner2 == 2):
                        print("COMPUTER (PLAYER 2) has won!")
                        break
                    elif (winner2 == 1):
                        print("PLAYER 1 wins")
                        break
                        
                    # check if human won #
                    winner2 = check_victory(board, you_player)
                    if (winner2 == 1):
                        print("YOU, PLAYER", you_player, "wins!")
                        break
                    elif (winner2 == 2):
                        print("COMPUTER (PLAYER 2) wins")
                        break
                    
                
                    machine_turn = False

                else: # human is PLAYER 2
                    
                    computer_move_found = 0
                    while (not computer_move_found):
                        computer_selected_col, computer_pop = computer_move(board, 1, get_computer_difficulty)
                        if check_move(board, 1, computer_selected_col, computer_pop) == True:
                            computer_move_found = 1

                    print("computer_selected_col:", computer_selected_col, "computer_pop:", computer_pop)
                    board = apply_move(board, 1, computer_selected_col, computer_pop)

                    # check if Computer won #
                    winner2 = check_victory(board, 1)
                    if (winner2 == 1):
                        print("Computer (PLAYER 1) has won!")
                        break
                    elif (winner2 == 2):
                        print("YOU, PLAYER 2 wins")
                        break
                        
                    # check if human won #
                    winner2 = check_victory(board, you_player)
                    if (winner2 == 2):
                        print("YOU, PLAYER", you_player, "wins!")
                        break
                    elif (winner2 == 1):
                        print("COMPUTER (PLAYER 1) wins")
                        break

                    machine_turn = False
    

if __name__ == "__main__":
    menu()




    
