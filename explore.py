# boardwidth = 7
# label = []

# def one_dim_to_two_dim(board):
#     # convert 1D list to 2D list #
#     output_list = []
#     row_list = []
#     count = 0
#     for val in board:
#         row_list.append(val)
#         count += 1
#         if (count % 7 == 0): # fixed 7 entries per row
#             output_list.insert(0, row_list)
#             row_list = [] # clear row_list

#     return output_list

# def two_dim_to_one_dim(board):
#     # convert 2D list to 1D list #
#     output_list = []
#     for row in reversed(board):
#         for val in row:
#             output_list.append(val)
    
#     return output_list

# def display_board(board):
#     # implement your function here

#     # convert board from 1D to 2D #
#     board = one_dim_to_two_dim(board)
#     print("board's length:", len(board))
    
#     print("\n")
#     print(" A GAME OF CONNECT FOUR! ")
#     print("\n")
#     for row in board:
#         # print(" ".join(row))
#         print(row)
#     print("\n")

# board = [
#         [0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0],
#         [0,0,0,1,0,0,0],
#         [0,0,1,2,1,1,0]
#     ]

# board.append([9] * boardwidth)
# for j in range(boardwidth):
#     label.append(j+1)
# board.append(label)

# board = two_dim_to_one_dim(board)

# print(display_board(board))

import random
random_pop_list = [True, False]

for i in range(10):
    random_pop = random_pop_list[random.randint(0,1)]
    print(random_pop)
