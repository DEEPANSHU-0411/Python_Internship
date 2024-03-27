import tkinter as tk
import random

def play():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = user_choice_var.get()

    if user_choice == computer_choice:
        result_var.set("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result_var.set("You win!")
    else:
        result_var.set("Computer wins!")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Create the user choice label and dropdown menu
user_choice_label = tk.Label(root, text="Choose: ")
user_choice_label.pack()

user_choice_var = tk.StringVar(root)
user_choice_var.set("rock")
choices = ['rock', 'paper', 'scissors']
user_choice_menu = tk.OptionMenu(root, user_choice_var, *choices)
user_choice_menu.pack()

# Create the play button
play_button = tk.Button(root, text="Play", command=play)
play_button.pack()

# Create the label to display the result
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack()

root.mainloop()
