import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock, Paper, Scissors Game")
        self.root.wm_iconbitmap("hand-scissors.ico")
        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play_game('Rock'), font=("Arial", 14))
        self.rock_button.grid(row=1, column=0, padx=10, pady=10)

        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play_game('Paper'), font=("Arial", 14))
        self.paper_button.grid(row=1, column=1, padx=10, pady=10)

        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play_game('Scissors'), font=("Arial", 14))
        self.scissors_button.grid(row=1, column=2, padx=10, pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.grid(row=2, column=0, columnspan=3, pady=10)

        self.score_label = tk.Label(self.root, text="Score: User - 0, Computer - 0", font=("Arial", 12))
        self.score_label.grid(row=3, column=0, columnspan=3, pady=10)

        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.reset_game, font=("Arial", 14))
        self.play_again_button.grid(row=4, column=0, columnspan=3, pady=10)
        self.play_again_button.grid_remove()  # Initially hidden

    def play_game(self, player_choice):
        choices = ['Rock', 'Paper', 'Scissors']
        computer_choice = random.choice(choices)

        result = self.determine_winner(player_choice, computer_choice)

        self.result_label.config(text=f"Computer chose {computer_choice}\n{result}")

        self.update_score(result)

        self.score_label.config(text=f"Score: User - {self.user_score}, Computer - {self.computer_score}")

        self.show_play_again_button()

    def determine_winner(self, player, computer):
        if player == computer:
            return "It's a tie!"
        elif (
            (player == 'Rock' and computer == 'Scissors') or
            (player == 'Paper' and computer == 'Rock') or
            (player == 'Scissors' and computer == 'Paper')
        ):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"

    def update_score(self, result):
        if "win" in result.lower():
            self.user_score += 1
        elif "computer" in result.lower():
            self.computer_score += 1

    def show_play_again_button(self):
        self.play_again_button.grid()

    def reset_game(self):
        self.result_label.config(text="")
        self.play_again_button.grid_remove()
        self.root.mainloop()

# Instantiate the game
game = RockPaperScissorsGame()

# Run the Tkinter event loop
game.root.mainloop()
