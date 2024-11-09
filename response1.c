import tkinter as tk
from tkinter import messagebox
import random
import pygame
import time

# Initialize Pygame mixer
pygame.init()
pygame.mixer.init()

# Define sounds
def play_success_sound():
    pygame.mixer.music.load('success.mp3')
    pygame.mixer.music.play()

def play_error_sound():
    pygame.mixer.music.load('error.mp3')
    pygame.mixer.music.play()

def play_gameover_sound():
    pygame.mixer.music.load('gameover.mp3')
    pygame.mixer.music.play()

class CapitalCityGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Capital City Matching Game")
        self.label = tk.Label(self.root, text="Select a country and its capital", font=('Helvetica', 16))
        self.label.pack()

        self.country_capitals = {
            "France": "Paris",
            "Germany": "Berlin",
            "Italy": "Rome",
            "Spain": "Madrid",
            "UK": "London",
            "Poland": "Warsaw",
            "Romania": "Bucharest",
            "Netherlands": "Amsterdam",
            "Belgium": "Brussels",
            "Greece": "Athens",
            "Portugal": "Lisbon",
            "Ireland": "Dublin",
            "Croatia": "Zagreb",
            "Sweden": "Stockholm",
            "Denmark": "Copenhagen",
            "Norway": "Oslo",
            "Finland": "Helsinki",
            "Estonia": "Tallinn",
            "Latvia": "Riga",
            "Lithuania": "Vilnius",
        }

        self.selected_countries = random.sample(list(self.country_capitals.keys()), 10)
        self.country_buttons = []
        self.capital_buttons = []
        self.clicked_country = None
        self.clicked_capital = None
        self.matches = 0
        self.score = 0
        self.start_time = time.time()

        for country in self.selected_countries:
            button = tk.Button(self.root, text=country, command=lambda c=country: self.country_click(c))
            button.pack()
            self.country_buttons.append(button)

        for country in self.selected_countries:
            button = tk.Button(self.root, text=self.country_capitals[country], command=lambda c=self.country_capitals[country]: self.capital_click(c))
            button.pack()
            self.capital_buttons.append(button)

        self.update_timer()

    def country_click(self, country):
        self.clicked_country = country
        self.check_match()

    def capital_click(self, capital):
        self.clicked_capital = capital
        self.check_match()

    def check_match(self):
        if self.clicked_country and self.clicked_capital:
            if self.country_capitals[self.clicked_country] == self.clicked_capital:
                self.score += 1
                self.matches += 1
                play_success_sound()
                self.label['text'] = f"Correct match! Your score is {self.score}"
                self.disable_buttons(self.clicked_country, self.clicked_capital)
            else:
                play_error_sound()
                self.label['text'] = f"Incorrect match. Try again! Your score is {self.score}"
            self.clicked_country = None
            self.clicked_capital = None
            self.check_game_over()

    def disable_buttons(self, country, capital):
        for button in self.country_buttons:
            if button['text'] == country:
                button['state'] = 'disabled'
        for button in self.capital_buttons:
            if button['text'] == capital:
                button['state'] = 'disabled'

    def check_game_over(self):
        if self.matches == len(self.selected_countries):
            self.label['text'] = f"Congratulations! You have matched all countries with their capitals. Your final score is {self.score}"
            self.disable_all_buttons()
        elif time.time() - self.start_time > 600:
            self.label['text'] = f"Game over! Your final score is {self.score}"
            play_gameover_sound()
            self.disable_all_buttons()

    def disable_all_buttons(self):
        for button in self.country_buttons:
            button['state'] = 'disabled'
        for button in self.capital_buttons:
            button['state'] = 'disabled'

    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        timer_label = tk.Label(self.root, text=f"Time remaining: {9 - minutes} minutes {59 - seconds} seconds")
        timer_label.pack()
        if elapsed_time < 600:
            self.root.after(1000, self.update_timer)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = CapitalCityGame()
    game.run()
