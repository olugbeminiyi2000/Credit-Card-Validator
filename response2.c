import tkinter as tk
from random import shuffle
import pygame
import time

# Initialize Pygame
pygame.init()

class CapitalCityGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Capital City Matching Game")
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.country_capitals = {
            "Argentina": "Buenos Aires",
            "Australia": "Canberra",
            "Austria": "Vienna",
            "Belgium": "Brussels",
            "Brazil": "Brasilia",
            "Canada": "Ottawa",
            "Chile": "Santiago",
            "China": "Beijing",
            "Croatia": "Zagreb",
            "Czech Republic": "Prague",
            "Denmark": "Copenhagen",
            "Egypt": "Cairo",
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
            "Malaysia": "Kuala Lumpur",
            "Mexico": "Mexico City",
            "Netherlands": "Amsterdam",
            "New Zealand": "Wellington",
            "Norway": "Oslo",
            "Pakistan": "Islamabad",
            "Philippines": "Manila",
            "Poland": "Warsaw",
            "Portugal": "Lisbon",
            "Romania": "Bucharest",
            "Russia": "Moscow",
            "Saudi Arabia": "Riyadh",
            "South Africa": "Pretoria",
            "South Korea": "Seoul",
            "Spain": "Madrid",
            "Sweden": "Stockholm",
            "Switzerland": "Bern",
            "Taiwan": "Taipei",
            "Thailand": "Bangkok",
            "Turkey": "Ankara",
            "Ukraine": "Kyiv",
            "United Arab Emirates": "Abu Dhabi",
            "United Kingdom": "London",
            "United States": "Washington, D.C.",
            "Vatican City": "Vatican City",
        }

        self.countries = list(self.country_capitals.keys())
        self.capitals = list(self.country_capitals.values())

        shuffle(self.countries)
        shuffle(self.capitals)

        self.country_buttons = []
        self.capital_buttons = []

        for i, country in enumerate(self.countries):
            button = tk.Button(self.frame, text=country, command=lambda country=country: self.select_country(country))
            button.grid(row=i, column=0)
            self.country_buttons.append(button)

        for i, capital in enumerate(self.capitals):
            button = tk.Button(self.frame, text=capital, command=lambda capital=capital: self.select_capital(capital))
            button.grid(row=i, column=1)
            self.capital_buttons.append(button)

        self.score = 0
        self.selected_country = None
        self.selected_capital = None
        self.matches = 0
        self.time_left = 600  # 10 minutes in seconds

        self.score_label = tk.Label(self.root, text="Score: 0")
        self.score_label.pack()

        self.time_label = tk.Label(self.root, text="Time: 10:00")
        self.time_label.pack()

        self.update_timer()

    def select_country(self, country):
        if self.selected_capital:
            if self.country_capitals[country] == self.selected_capital:
                self.score += 1
                self.score_label['text'] = f"Score: {self.score}"
                pygame.mixer.music.load('success.mp3')
                pygame.mixer.music.play()
                self.matches += 1
                self.check_game_over()
            else:
                pygame.mixer.music.load('error.mp3')
                pygame.mixer.music.play()
            self.selected_capital = None
            self.selected_country = None
        else:
            self.selected_country = country

    def select_capital(self, capital):
        if self.selected_country:
            if self.country_capitals[self.selected_country] == capital:
                self.score += 1
                self.score_label['text'] = f"Score: {self.score}"
                pygame.mixer.music.load('success.mp3')
                pygame.mixer.music.play()
                self.matches += 1
                self.check_game_over()
            else:
                pygame.mixer.music.load('error.mp3')
                pygame.mixer.music.play()
            self.selected_capital = None
            self.selected_country = None
        else:
            self.selected_capital = capital

    def update_timer(self):
        if self.time_left > 0:
            minutes, seconds = divmod(self.time_left, 60)
            self.time_label['text'] = f"Time: {minutes}:{seconds:02d}"
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.time_label['text'] = "Time's up!"
            pygame.mixer.music.load('gameover.mp3')
            pygame.mixer.music.play()
            self.game_over()

    def check_game_over(self):
        if self.matches == len(self.countries):
            self.root.after(3000, self.congratulations)

    def congratulations(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        label = tk.Label(self.root, text="Congratulations! You matched all the countries and capitals!")
        label.pack()
        score_label = tk.Label(self.root, text=f"Your final score is: {self.score}")
        score_label.pack()

    def game_over(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        label = tk.Label(self.root, text="Game Over! Time's up!")
        label.pack()
        score_label = tk.Label(self.root, text=f"Your final score is: {self.score}")
        score_label.pack()

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = CapitalCityGame()
    game.start()
