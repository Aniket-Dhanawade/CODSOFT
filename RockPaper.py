import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")

        # Load images
        self.rock_img = ImageTk.PhotoImage(Image.open("C:\\Users\\Aniket Dhanawade\\Pictures\\Screenshots\\rock.png"))
        self.paper_img = ImageTk.PhotoImage(Image.open("C:\\Users\\Aniket Dhanawade\\Pictures\\Screenshots\\paper.png"))
        self.scissors_img = ImageTk.PhotoImage(Image.open("C:\\Users\\Aniket Dhanawade\\Pictures\\Screenshots\\scissor.png"))

        # Game variables
        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.comp_score = 0

        # Create UI elements
        self.user_choice_label = tk.Label(root, text="Your Choice:", font=("Arial", 14))
        self.user_choice_label.pack()

        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set("rock")  # Default choice
        self.user_choices = tk.OptionMenu(root, self.user_choice_var, *self.choices)
        self.user_choices.pack()

        self.play_button = tk.Button(root, text="Play", command=self.play_game, font=("Arial", 12))
        self.play_button.pack()

        self.result_label = tk.Label(root, text="", font=("Arial", 16), fg="white", bg="orange")
        self.result_label.pack()

        self.comp_choice_label = tk.Label(root, text="")
        self.comp_choice_label.pack()

        self.score_label = tk.Label(root, text="Score: User {} - {} Computer".format(self.user_score, self.comp_score),
                                    font=("Arial", 12))
        self.score_label.pack()

        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again, font=("Arial", 12))
        self.play_again_button.pack()

    def play_game(self):
        user_choice = self.user_choice_var.get()
        comp_choice = random.choice(self.choices)

        # Display choices
        self.display_choices(user_choice, comp_choice)

        # Determine the winner
        result = self.determine_winner(user_choice, comp_choice)

        # Update score and display result
        self.update_score(result)
        self.display_result(result)

    def display_choices(self, user_choice, comp_choice):
        self.user_choice_label.config(image=getattr(self, f"{user_choice}_img"))
        self.comp_choice_label.config(image=getattr(self, f"{comp_choice}_img"))

    def determine_winner(self, user_choice, comp_choice):
        if user_choice == comp_choice:
            return "tie"
        elif (
            (user_choice == "rock" and comp_choice == "scissors") or
            (user_choice == "scissors" and comp_choice == "paper") or
            (user_choice == "paper" and comp_choice == "rock")
        ):
            return "win"
        else:
            return "lose"

    def update_score(self, result):
        if result == "win":
            self.user_score += 1
        elif result == "lose":
            self.comp_score += 1

    def display_result(self, result):
        if result == "tie":
            self.result_label.config(text="It's a tie!")
        elif result == "win":
            self.result_label.config(text="You win!")
        else:
            self.result_label.config(text="You lose!")

        self.score_label.config(text="Score: User {} - {} Computer".format(self.user_score, self.comp_score))

    def play_again(self):
        self.user_choice_var.set("rock")
        self.result_label.config(text="")
        self.comp_choice_label.config(image="")
        self.score_label.config(text="Score: User {} - {} Computer".format(self.user_score, self.comp_score))

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
