import tkinter as tk
from tkinter import messagebox
import random
import pygame
import threading
import time

class CapitalCityGame:
    # ...

    def check_match(self):
        """
        Checks if the selected country and capital form a valid pair.
        If correct, updates the score and disables the buttons.
        """
        if self.selected_country and self.selected_capital:
            if self.capital_dict[self.selected_country] == self.selected_capital:
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                self.message_label.config(text="Correct Match!", fg="green")
                self.play_sound('success.mp3')  # Correct match sound

                # Change button colors briefly to light green
                self.buttons[self.selected_country].config(bg="#90EE90")
                self.buttons[self.selected_capital].config(bg="#90EE90")
                self.root.update_idletasks()
                self.root.after(500, self.reset_button_colors, self.selected_country, self.selected_capital)

                # Disable matched buttons
                self.buttons[self.selected_country].config(state="disabled")
                self.buttons[self.selected_capital].config(state="disabled")

                # Check for game end
                if self.score == len(self.capital_dict):
                    self.end_game("Congratulations! You've matched all pairs!")

            else:
                self.message_label.config(text="Incorrect Match!", fg="red")
                self.play_sound('error.mp3')  # Incorrect match sound

                # Change button colors briefly to red
                self.buttons[self.selected_country].config(bg="red")
                self.buttons[self.selected_capital].config(bg="red")
                self.root.update_idletasks()
                self.root.after(500, self.reset_button_colors, self.selected_country, self.selected_capital)

            # Reset selections
            self.selected_country = ""
            self.selected_capital = ""

    def reset_button_colors(self, country, capital):
        """
        Resets the button colors back to default.
        """
        self.buttons[country].config(bg="SystemButtonFace")
        self.buttons[capital].config(bg="SystemButtonFace")

# Run the game
root = tk.Tk()
game = CapitalCityGame(root)
root.mainloop()
