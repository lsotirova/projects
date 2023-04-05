import random
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


root = Tk()
root.title("Spy Game")
# root.geometry("1200x700")
clicked = True
global count


l1 = Label(root)
e1 = Entry(root)
e1.insert(0, "Type a word and number")
e1.config(state=DISABLED)

img = ImageTk.PhotoImage(Image.open("thumbnail_spy.png"))
panel = Label(root, image=img)
panel.grid(row=3, column=5)


def main():
    ...


def rules():
    messagebox.showinfo("Rules of Spy Game",
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
                        "or lose all of the buttons are disabled and the game can only be reset."
                        )


def coordinator_words_four():
    messagebox.showinfo("Spymaster", coordinators_words)


def check_if_won(b):
    global clicked, count
    global winner, points
    winner = False
    if b["text"] in list(coordinators_words) and clicked == True:
        count += 1
        points.config(text=f"Score: " + str(count), font=("Helvetica", 12))
        b.config(state=DISABLED)
        winner = True
        if count == 4:
            messagebox.showinfo("Spy Game", "Congratulations!\n You won!")
            disable_all_buttons()
        return True
    else:
        return False


def on_click(event):
    e1.configure(state=NORMAL)
    e1.delete(0, END)

    # make the callback only work once
    e1.unbind('<Button-1>', on_click_id)


on_click_id = e1.bind('<Button-1>', on_click)


def show_entry_fields():
    global l1
    try:
        l1.destroy()
        word, number = e1.get().split(" ")
        number = int(number)
        hint = f"Guess {number} card(s) related to {word}"
        l1 = Label(root, text=hint, font=("Helvetica", 10))
        l1.grid(row=5, columnspan=2, pady=2)
    except ValueError:
        hint = f"Please type: word number"
        l1 = Label(root, text=hint, font=("Helvetica", 10))
        l1.grid(row=5, columnspan=2, pady=2)


def disable_all_buttons():
    global count
    count = 0
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)
    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)
    b16.config(state=DISABLED)
    coordinators_button.config(state=DISABLED)
    submit.config(state=DISABLED)
    e1.config(state=DISABLED)


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, coordinators_button, e1, l1, submit
    global clicked, words_choice, count, points, hint
    global coordinators_words
    count = 0
    clicked = True

    words_list = ["boat", "apple", "house", "icecream", "chips", "computer", "tree", "diamond", "baby", "sand", "sea",
             "seashell", "pen", "cake", "chocolate", "notebook", "cup", "desk", "tomato", "jeans", "guitar", "photo",
             "rose", "butterfly", "carpet"]
    words = [word.upper() for word in words_list]
    random.shuffle(words)
    words_choice = random.sample(words, 16)
    coordinators_words = random.sample(words_choice, 4)

    b1 = Button(root, text=words_choice[0], font=("Helvetica", 12), height=3, width=10,
                command=lambda: [b_click(b1), check_if_won(b1)])
    b2 = Button(root, text=words_choice[1], font=("Helvetica", 12), height=3, width=10,
                command=lambda: [b_click(b2), check_if_won(b2)])
    b3 = Button(root, text=words_choice[2], font=("Helvetica", 12), height=3, width=10,
                command=lambda: [b_click(b3), check_if_won(b3)])
    b4 = Button(root, text=words_choice[3], font=("Helvetica", 12), height=3, width=10,
                command=lambda: [b_click(b4), check_if_won(b4)])
    b5 = Button(root, text=words_choice[4], font=("Helvetica", 12), height=3, width=10,
                command=lambda: [b_click(b5), check_if_won(b5)])
    b6 = Button(root, text=words_choice[5], font=("Helvetica", 12), height=3, width=10,
                command=lambda: [b_click(b6), check_if_won(b6)])
    b7 = Button(root, text=words_choice[6], font=("Helvetica", 12), height=3, width=10,
                command=lambda: [b_click(b7), check_if_won(b7)])
    b8 = Button(root, text=words_choice[7], font=("Helvetica", 12), height=3, width=10,
                command=lambda: [b_click(b8), check_if_won(b8)])

    b9 = Button(root, text=words_choice[8], font=("Helvetica", 12), height=3, width=10,
                command=lambda: [b_click(b9), check_if_won(b9)])
    b10 = Button(root, text=words_choice[9], font=("Helvetica", 12), height=3, width=10,
                 command=lambda: [b_click(b10), check_if_won(b10)])
    b11 = Button(root, text=words_choice[10], font=("Helvetica", 12), height=3, width=10,
                 command=lambda: [b_click(b11), check_if_won(b11)])
    b12 = Button(root, text=words_choice[11], font=("Helvetica", 12), height=3, width=10,
                 command=lambda: [b_click(b12), check_if_won(b12)])

    b13 = Button(root, text=words_choice[12], font=("Helvetica", 12), height=3, width=10,
                 command=lambda: [b_click(b13), check_if_won(b13)])
    b14 = Button(root, text=words_choice[13], font=("Helvetica", 12), height=3, width=10,
                 command=lambda: [b_click(b14), check_if_won(b14)])
    b15 = Button(root, text=words_choice[14], font=("Helvetica", 12), height=3, width=10,
                 command=lambda: [b_click(b15), check_if_won(b15)])
    b16 = Button(root, text=words_choice[15], font=("Helvetica", 12), height=3, width=10,
                 command=lambda: [b_click(b16), check_if_won(b16)])

    coordinators_button = Button(root, text="Spy words", font=("Helvetica", 10), height=1, width=8
                                 , command=lambda: coordinator_words_four())
    reset_button = Button(root, text="Reset", font=("Helvetica", 10), height=1, width=8
                          , command=lambda: [reset(), destroy_label()])
    rules_button = Button(root, text="Rules", font=("Helvetica", 10), height=1, width=8
                          , command=lambda: rules())
    submit = Button(root, text='Submit', font=("Helvetica", 10), command=show_entry_fields)

    points = Label(root, text=f"Score: " + str(count), font=("Helvetica", 12))

    # Grid buttons
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=0, column=3)

    b5.grid(row=1, column=0)
    b6.grid(row=1, column=1)
    b7.grid(row=1, column=2)
    b8.grid(row=1, column=3)

    b9.grid(row=2, column=0)
    b10.grid(row=2, column=1)
    b11.grid(row=2, column=2)
    b12.grid(row=2, column=3)

    b13.grid(row=3, column=0)
    b14.grid(row=3, column=1)
    b15.grid(row=3, column=2)
    b16.grid(row=3, column=3)

    coordinators_button.grid(row=0, column=5, padx=30)
    reset_button.grid(row=4, column=5)

    points.grid(row=2, column=5, padx=80)
    e1.grid(row=4, columnspan=2, pady=3, sticky=E)
    e1.config(state=NORMAL)

    submit.grid(row=4, column=2, sticky=W, pady=2)
    rules_button.grid(row=1, column=5)


def destroy_label():
    try:
        l1.destroy()

    except NameError:
        pass


reset()


def b_click(b):
    global clicked
    bomb_list = []
    for word in list(words_choice):
        if word not in list(coordinators_words):
            bomb_list.append(word)
    word_bomb = random.choice(bomb_list)

    if b["text"] == word_bomb and clicked == True:
        b["text"] = "💣"
        messagebox.showerror("Spy Game", "GAME OVER!")
        disable_all_buttons()


root.mainloop()

if __name__ == "__main__":
    main()