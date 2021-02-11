# Tic-tac-toe 

Play through the console.
[tic_tac_toe.py read me](tic_tac_toe.md)

# Tic-tac-toe with interface

The interface is done using Tkinter. By constructing the GUI (graphical interface) the code changes and it is now event driven. In other words the flow of the program is determined by the action of pressing a button.

- In the interface the player can play against the computer or another player in the same computer.

he interface looks like this:

![tic_tac_toe tkinter interface](https://github.com/catalinac3/Projects-in-python/blob/master/images/simple_tkinter.JPG?raw=true)

Files:
- settings_tic_tac_toe.py
- game_tic_tac_toe.py


How the computer chooses a position:
- If the computer is able to win in the next turn, it will choose that position.
- If the player wins in the next turn, the computer will block it.
- If there in no posibility of wining or blocking, the computer will choose a corner or the center, if one is available.
- If none of the above, the computer will use a side position.


