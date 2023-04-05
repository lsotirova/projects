# SPY GAME
#### Video Demo:  <https://youtu.be/-jupTLYddWE>
#### Description:
This code is using the Tkinter library to create a GUI (graphical user interface) game called Spy Game. The Tkinter library is a Python module that provides tools to create GUI applications.

The code creates a main Tkinter window with the title "Spy Game". It then defines several functions that correspond to different actions in the game, such as displaying the rules of the game, showing the spymaster's hint, checking if the game has been won, and resetting the game.

The game also includes several Tkinter widgets, such as labels, buttons, and an entry field. These widgets are used to display information to the user, and allow the user to interact with the game by clicking buttons or entering input.
# How to play
The game is played by the user guessing words related to a hint given by the spymaster. The spymaster's hint is displayed in a label widget, and the user can guess by clicking on one of 16 buttons, each corresponding to a word. If the user clicks on a button with a word that is related to the hint, the button is disabled and the user's score is incremented. If the user's score reaches 4, they win the game.

The game can be reset by clicking the reset button, which disables all of the buttons and clears the input field. The game can also be exited by clicking the quit button, which closes the Tkinter window and ends the program.
In addition to the main functions and widgets described above, the code also includes several other features. For example, the game includes an entry field that allows the user to input a hint for the next round of the game. When the user clicks on the entry field, the text "Type a word and number" is deleted, and the user can enter their own hint in the format "word number". The user can then click the submit button to display their hint in a label widget.

The code also includes a function called "coordinator_words_four" that displays a message box containing a list of words that the spymaster can use as hints. These words are stored in a list called "coordinators_words".

There is also a "rules" function that displays a message box with instructions on how to play the game. Finally, the code includes a main function that is called when the program is run. This function creates the widgets and buttons for the game, and assigns them to specific positions in the Tkinter window using the "grid" layout manager.

Overall, this code creates a simple GUI game called Spy Game that allows the user to guess words related to a hint given by the spymaster, and displays the user's score as they play. It also includes several additional features such as the ability to input and display hints, and the option to view the available hints for the spymaster.
# Detailed explanation of each function and widget in the code:

## main:
This function is called when the program is run. It creates the widgets and buttons for the game, and assigns them to specific positions in the Tkinter window using the "grid" layout manager. It also defines the text and behavior for each button. For example, the "rules" button displays the rules of the game when clicked, and the "coordinator's words" button displays the available hints for the spymaster.

## rules:
This function displays a message box with instructions on how to play the game. The message box is created using the messagebox.showinfo function from the Tkinter library.

## coordinator_words_four:
This function displays a message box containing a list of words that the spymaster can use as hints. The list of words is stored in a global variable called "coordinators_words". The message box is created using the messagebox.showinfo function from the Tkinter library.

## check_if_won:
 This function checks if the game has been won by the user. It takes in a button widget as an argument, and checks if the text of the button is contained in the list of "coordinators_words" (i.e., the list of available hints). If the button's text is in the list, the function increments the user's score and disables the button. If the user's score reaches 4, the function displays a message box congratulating the user on winning the game.

## on_click:
 This function is called when the user clicks on the entry field widget. It unbinds the "on_click" function from the entry field, so that it is only called once. This is done to prevent the default text from being deleted multiple times if the user clicks on the entry field multiple times.

## show_entry_fields:
This function is called when the user clicks the submit button. It retrieves the input from the entry field and displays it in a label widget. If the input is not in the correct format (i.e., "word number"), the function displays an error message in the label widget.

## disable_all_buttons:
This function disables all of the buttons in the game and clears the input field. It is called when the reset button is clicked.

## reset:
This function resets the game by calling the disable_all_buttons function, and setting several global variables to their default values. It is called when the reset button is clicked.

## root:
This is the main Tkinter window for the game. It has the title "Spy Game".

## l1:
This is a label widget that is used to display the spymaster's hint or an error message.

## e1:
This is an entry widget that allows the user to input a hint for the next round of the game. When the user clicks on the entry field, the text "Type a word and number" is deleted, and the user can enter their own hint in the format "word number".

## img:
This is an image widget that displays the image "spy2_50x50.png".

## panel:
This is a label widget that displays the image "img".

## b1, b2, ..., b16:
These are button widgets that correspond to the words that the user can guess. When the user clicks on a button, the button is disabled and the user's score is incremented if the button's text is related to the spymaster's hint.

## coordinators_button:
This is a button widget that displays the available hints for the spymaster when clicked.

## submit:
This is a button widget that retrieves the input from the entry field and displays it in a label widget when clicked.

## points:
This is a label widget that displays the user's score. It is updated each time the user clicks on a button with a word related to the spymaster's hint.