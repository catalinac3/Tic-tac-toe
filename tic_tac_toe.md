# tic_tac_toe.py

### How to use it?
You can run it in your VS Code and play it in the terminal with 2 players on the same computer.<br>
OR...<br>
Try to write the code of each function by copying down the name of the functions needed with the description of what they should do, to recreate this exercise.

### What is it?
This file displays the code of the tic-tac-toe written in python. No modules were imported.
 
The interface with the users is located in the terminal. In the terminal, both players can make their move and see the development of the game on the board game. 
An additional board indicating available positions is given as a guide for the players to make the next move. This is done with numbers from 1 to 9
 
The board game and the board indicating available moves look like this:
 
![tic_tac_toe terminal interface](https://github.com/catalinac3/Projects-in-python/blob/master/images/tic_tac_toe.JPG?raw=true)
 
One player marks in the board with an X the other one with O. Where there are 3 in a row the of the same mark, the player related to that mark wins.
 
![tic_tac_toe terminal interface](https://github.com/catalinac3/Projects-in-python/blob/master/images/show_win.JPG?raw=true)
 
In this code, the board is set up as a list of lists in python (a matrix), not as a list of nine like it is usually made. 
This brings a bit of an extra challenge on checking whether a player has won or not. 

