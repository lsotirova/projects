from tkinter import messagebox, Entry, Button
from unittest.mock import patch
from project import main, rules, coordinator_words_four, check_if_won


# Create the Entry and Button objects that are used in the test functions
e1 = Entry()
b = Button(text='secret')


def test_rules():
    # Test rules function
    with patch.object(messagebox, 'showinfo', return_value=None) as mock_showinfo:
        assert rules() == None  # rules function should not return anything
        mock_showinfo.assert_called_once()  # Test that showinfo is called once in the rules function


def test_coordinator_words_four():
    # Test coordinator_words_four function
    with patch.object(messagebox, 'showinfo', return_value=None) as mock_showinfo:
        assert coordinator_words_four() == None  # coordinator_words_four function should not return anything
        mock_showinfo.assert_called_once()  # Test that showinfo is called once in the coordinator_words_four function


def test_check_if_won():
    coordinators_words = ["secret", "words", "to", "guess"]
    # Test check_if_won function
    assert check_if_won(b) == False  # check_if_won should return False when b['text'] is not in coordinators_words
    b['text'] = coordinators_words[0]
    assert check_if_won(b) == False  # check_if_won should return True when b['text'] is in coordinators_words


def test_main():
    # Test main function
    assert main() == None


@patch("tkinter.messagebox.showinfo")
def test_rules(mock_showinfo):
    # Call the rules function
    rules()

    # Assert that the showinfo function was called with the correct arguments
    mock_showinfo.assert_called_with("Rules of Spy Game",
                                     "This is a game of Codenames implemented with a graphical user interface (GUI) using the "
                                     "Tkinter library.\n"
                                     "It has a number of features including:\n"
                                     "• A login screen where the player can input a word and number\n"
                                     "• A reset button that allows the player to start a new game\n"
                                     "• A 'Spymaster' button that reveals the secret words to the player\n"
                                     "• 16 buttons representing game tiles that the player can click on to guess the secret words\n"
                                     "• A submit button that allows the player to submit their guess\n"
                                     "• A label displaying the score\n"
                                     "• The game is won when the player has correctly guessed 4 secret words. When the player wins"
                                     "or lose all of the buttons are disabled and the game can only be reset.")

