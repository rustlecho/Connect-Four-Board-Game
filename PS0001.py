#-*-coding:utf8;-*-
#qpy:2
#qpy:console

from platform import machine
import time
import random


player_color = {0: "Yellow", 1: "Red"}

board = [] 
label = []

# whos_turn = 0b10
current_player = False # False will be you

winner1 = False # this is for human vs human

winner2 = False # this is for human vs machine
machine_turn = False # human vs machine

insert_row = 0
insert_col = 0

start_game = False

getboardheight = 0
human_opponent = True # True by default
opponent_type_selected = False

if (getboardheight == 0):
    print()
    print("!! WELCOME TO CONNECT FOUR MENU !!")
    print()
    print("MENU:")
    print("-----")
    print()
    while (not(6 <= getboardheight <= 10)):
        getboardheight = int(input("Select Number of Rows (Choose a number from 6-10)"))

    while (not(opponent_type_selected)):
        get_opponent_type =  input("Play Against A Computer? (y/n)")
        if (get_opponent_type == "y" or get_opponent_type == "Y" or get_opponent_type == "n" or get_opponent_type == "N"):
            opponent_type_selected = True
            if (get_opponent_type == "y" or get_opponent_type == "Y"):
                human_opponent = False

    start_game = True

boardheight = getboardheight
boardwidth = 7

# generate empty board
def generate_board(boardheight, boardwidth):
    for i in range(boardheight):
        board.append(["_"] * boardwidth)
        
    board.append(["^"] * boardwidth)
    for j in range(boardwidth):
        label.append(str(j+1))
    board.append(label)


def print_board(board):
    print("\n")
    print(" A GAME OF CONNECT FOUR! ")
    print("\n")
    for row in board:
        print(" ".join(row))
    print("\n")

def mark_board(insert_row, insert_column, colored_player):
    if (colored_player == "Red"): # current_player = True --> You
        board[insert_row][insert_column] = "R"
    else: # Opponent
        board[insert_row][insert_column] = "Y"
    print_board(board)

def play(colored_player):
    while True:
        insert_column = int(input("Pick a column (1-7): ")) - 1
        # try:
        if insert_column >= 0 and insert_column <= boardwidth-1:
            for i in range(boardheight-1, -1 , -1):
                if board[i][insert_column] == "_":
                    insert_row = i
                    break                    
        try:
            mark_board(insert_row, insert_column, colored_player)
            break
        except:
            print("Please Try Another Column!")
            continue
    
def machine_play():
    print("Computer is making a move...")
    time.sleep(1.3)
    print()
    
    while True:
        random_column = random.randint(0, boardwidth-1)
        for i in range(boardheight-1, -1 , -1):
            print("check i:", i)
            if board[i][random_column] == "_":
                insert_row = i
                break
        try:
            print("insert_row:", insert_row, "random column:", random_column)
            board[insert_row][random_column] = "Y"
            print_board(board)
            break
        except:
            continue

def check_winner(board, colored_player):
    
    #check horizontal spaces
    for y in range(boardheight):
        for x in range(boardwidth - 3):
            if board[x][y] == colored_player[0] and board[x+1][y] == colored_player[0] and board[x+2][y] == colored_player[0] and board[x+3][y] == colored_player[0]:
                return True

    #check vertical spaces
    for x in range(boardwidth):
        for y in range(boardheight - 3):
            if board[x][y] == colored_player[0] and board[x][y+1] == colored_player[0] and board[x][y+2] == colored_player[0] and board[x][y+3] == colored_player[0]:
                return True

    #check / diagonal spaces
    for x in range(boardwidth - 3):
        for y in range(3, boardheight):
            if board[x][y] == colored_player[0] and board[x+1][y-1] == colored_player[0] and board[x+2][y-2] == colored_player[0] and board[x+3][y-3] == colored_player[0]:
                return True

    #check \ diagonal spaces
    for x in range(boardwidth - 3):
        for y in range(boardheight - 3):
            if board[x][y] == colored_player[0] and board[x+1][y+1] == colored_player[0] and board[x+2][y+2] == colored_player[0] and board[x+3][y+3] == colored_player[0]:
                return True

    return False


# start()

if (start_game):
    print()
    print("GAME HAS STARTED")
    generate_board(boardheight, boardwidth)
    print_board(board)


if (human_opponent == True):
    while (winner1 == False):
        if (not current_player):
            current_player = True
        else:
            current_player = False
        
        colored_player = player_color[current_player]
        print("It is " + colored_player + " Player turn.")
    
        play(colored_player)
        
        winner1 = check_winner(board, colored_player)

    if (winner1 == True):
        colored_player = player_color[current_player]
        print(colored_player + " Player wins!")

else: # you vs machine
    while (winner2 == False):
        you_player = player_color[1]

        if (machine_turn == False):
            print("It is " + you_player + " Player turn.")
            play(you_player)
            winner2 = check_winner(board, you_player)
            if (winner2 == True):
                print(you_player, " Player wins!")
            machine_turn = True

        else:
            machine_play()
            winner2 = check_winner(board, "Yellow") # machine is yellow player by default
            if (winner2 == True):
                print("Machine has won!")
            machine_turn = False
        
    

    
