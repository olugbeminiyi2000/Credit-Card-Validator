import tkinter as tk
from tkinter import messagebox
import random
import pygame
import time

# Initialize Pygame for sound playback
pygame.init()
pygame.mixer.init()

class CapitalCityGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Capital City Matching Game")
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        # Load sounds
        self.success_sound = 'success.mp3'
        self.error_sound = 'error.mp3'
        self.gameover_sound = 'gameover.mp3'

        # Country-capital pairs
        self.pairs = {
            "Argentina": "Buenos Aires",
            "Australia": "Canberra",
            "Austria": "Vienna",
            "Belgium": "Brussels",
            "Brazil": "Brasília",
            "Bulgaria": "Sofia",
            "Canada": "Ottawa",
            "Chile": "Santiago",
            "China": "Beijing",
            "Croatia": "Zagreb",
            "Cuba": "Havana",
            "Cyprus": "Nicosia",
            "Czech Republic": "Prague",
            "Denmark": "Copenhagen",
            "Egypt": "Cairo",
            "Estonia": "Tallinn",
            "Finland": "Helsinki",
            "France": "Paris",
            "Germany": "Berlin",
            "Greece": "Athens",
            "Hungary": "Budapest",
            "Iceland": "Reykjavik",
            "India": "New Delhi",
            "Indonesia": "Jakarta",
            "Ireland": "Dublin",
            "Israel": "Jerusalem",
            "Italy": "Rome",
            "Japan": "Tokyo",
            "Latvia": "Riga",
            "Lithuania": "Vilnius",
            "Luxembourg": "Luxembourg City",
            "Malaysia": "Kuala Lumpur",
            "Malta": "Valletta",
            "Mexico": "Mexico City",
            "Netherlands": "Amsterdam",
            "New Zealand": "Wellington",
            "Norway": "Oslo",
            "Philippines": "Manila",
            "Poland": "Warsaw",
            "Portugal": "Lisbon",
            "Romania": "Bucharest",
            "Russia": "Moscow",
            "Serbia": "Belgrade",
            "Singapore": "Singapore",
            "Slovakia": "Bratislava",
            "Slovenia": "Ljubljana",
            "South Africa": "Pretoria",
            "South Korea": "Seoul",
            "Spain": "Madrid",
            "Sweden": "Stockholm",
            "Switzerland": "Bern",
            "Taiwan": "Taipei",
            "Thailand": "Bangkok",
            "Turkey": "Ankara",
            "Ukraine": "Kyiv",
            "United Kingdom": "London",
            "United States": "Washington, D.C.",
            "Vietnam": "Hanoi",
        }

        # Randomly shuffle the pairs
        self.countries = list(self.pairs.keys())
        self.capitals = list(self.pairs.values())
        random.shuffle(self.countries)
        random.shuffle(self.capitals)

        # Create buttons for countries and capitals
        self.country_buttons = []
        self.capital_buttons = []
        for i, country in enumerate(self.countries):
            button = tk.Button(self.frame, text=country, command=lambda i=i: self.country_selected(i))
            button.grid(row=i, column=0)
            self.country_buttons.append(button)
        for i, capital in enumerate(self.capitals):
            button = tk.Button(self.frame, text=capital, command=lambda i=i: self.capital_selected(i))
            button.grid(row=i, column=1)
            self.capital_buttons.append(button)

        # Create a label to display the score
        self.score_label = tk.Label(self.frame, text="Score: 0")
        self.score_label.grid(row=len(self.countries), column=0, columnspan=2)

        # Create a label to display the time remaining
        self.time_label = tk.Label(self.frame, text="Time remaining: 10:00")
        self.time_label.grid(row=len(self.countries)+1, column=0, columnspan=2)

        # Initialize the score and the time remaining
        self.score = 0
        self.time_remaining = 600  # 10 minutes in seconds

        # Start the countdown timer
        self.update_timer()

        # Initialize the selected country and capital
        self.selected_country = None
        self.selected_capital = None

    def country_selected(self, i):
        self.selected_country = self.countries[i]
        self.check_match()

    def capital_selected(self, i):
        self.selected_capital = self.capitals[i]
        self.check_match()

    def check_match(self):
        if self.selected_country and self.selected_capital:
            if self.pairs[self.selected_country] == self.selected_capital:
                # Correct match, increment score and play success sound
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                pygame.mixer.music.load(self.success_sound)
                pygame.mixer.music.play()
                # Disable the buttons for the matched country and capital
                for i, country in enumerate(self.countries):
                    if country == self.selected_country:
                        self.country_buttons[i].config(state="disabled")
                for i, capital in enumerate(self.capitals):
                    if capital == self.selected_capital:
                        self.capital_buttons[i].config(state="disabled")
                # Check if all pairs are matched
                if self.score == len(self.pairs):
                    self.root.after(3000, self.game_won)
            else:
                # Incorrect match, play error sound
                pygame.mixer.music.load(self.error_sound)
                pygame.mixer.music.play()
            # Reset the selected country and capital
            self.selected_country = None
            self.selected_capital = None

    def update_timer(self):
        minutes, seconds = divmod(self.time_remaining, 60)
        self.time_label.config(text=f"Time remaining: {minutes:02d}:{seconds:02d}")
        self.time_remaining -= 1
        if self.time_remaining >= 0:
            self.root.after(1000, self.update_timer)
        else:
            self.game_over()

    def game_won(self):
        messagebox.showinfo("Congratulations!", "You have matched all the capital cities correctly!")
        self.root.quit()

    def game_over(self):
        pygame.mixer.music.load(self.gameover_sound)
        pygame.mixer.music.play()
        messagebox.showinfo("Game Over", "Time's up! Your final score is " + str(self.score))
        self.root.quit()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = CapitalCityGame()
    game.run()
