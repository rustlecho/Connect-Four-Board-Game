## Copyright and Authorship
Author: Russell

1. The code in this repository is written as part of an ongoing research with Nanyang Technological University.
2. This repository, including all its contents, is protected by copyright laws. If you wish to use, modify, or distribute any part of this repository, please contact [Russell] at [rcho002@e.ntu.edu.sg] for more details.
3. For potential collaboration, please contact the author as well.


## Connect Four Game (Pop-Your-Chip)
### Pop-Your-Chip Version -- *Modified/Special Version of Connect Four*
Connect4 or Connect Four is a game in which the players choose a color and then take turns dropping colored tokens into a six-row, seven-column vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own tokens.

Players choose a color (Player 1 or Player 2), and take turn dropping their colored chips from the top row down a column. In this "Pop-Your Chip" *Modified/Special Version* of Connect4, Players are able to pop their own chips out from the bottom of the board. This causes the chips above to all fall down by one position producing a new arrangement of chips on the board. Which in consequence, can act as a way to modify the strategies each player can use to win the game either from an offensive or defensive perspective! The first player to get four chips in a row (vertical, horizontal, or diagonal) wins!


## Economics Perspective and Computational Complexity
Connect Four is a two-player game with perfect information for both sides, meaning that nothing is hidden from anyone. Connect Four also belongs to the classification of an adversarial, zero-sum game, since a player's advantage is an opponent's disadvantage.

One measure of complexity of the Connect Four game is the number of possible games board positions. For classic Connect Four played on a 7-column-wide, 6-row-high grid, there are 4,531,985,219,092 (about 4.5 trillion) positions for all game boards populated with 0 to 42 pieces. Connect Four is a solved game. The first player can always win by playing the right moves.

(description taken from wikipedia: http://en.wikipedia.org/wiki/Connect_Four)

This code is implemented in python and is played via the terminal.
Play with the computer on a (6-rows x 7-columns) board or have a 2-player game with your buddy ! :)

(7x7) board may be desired for symmetrical reasons for but this version follows the classic 6-rows and 7-columns grid.


## Code Flowchart Visualisation:
![Alt text](./connect4_code_overview_final.png)


### How to run:
```
python connect4.py
```