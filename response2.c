import tkinter as tk
from tkinter import messagebox
import random
import pygame
import time

class CapitalCityGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Capital City Matching Game")
        self.countries = {
            "France": "Paris",
            "Germany": "Berlin",
            "Italy": "Rome",
            "Spain": "Madrid",
            "Portugal": "Lisbon",
            "Greece": "Athens",
            "Austria": "Vienna",
            "Belgium": "Brussels",
            "Croatia": "Zagreb",
            "Cyprus": "Nicosia"
        }
        self.country_buttons = {}
        self.capital_buttons = {}
        self.country_selected = None
        self.capital_selected = None
        self.matches = 0
        self.score = 0
        self.time_left = 600  # 10 minutes
        self.create_widgets()
        self.layout_widgets()
        self.update_timer()

    def create_widgets(self):
        self.country_frame = tk.Frame(self.root)
        self.capital_frame = tk.Frame(self.root)
        self.score_label = tk.Label(self.root, text="Score: 0")
        self.time_label = tk.Label(self.root, text="Time left: 10:00")
        self.country_list = list(self.countries.keys())
        self.capital_list = list(self.countries.values())
        random.shuffle(self.country_list)
        random.shuffle(self.capital_list)
        for country in self.country_list:
            self.country_buttons[country] = tk.Button(self.country_frame, text=country, command=lambda c=country: self.select_country(c))
        for capital in self.capital_list:
            self.capital_buttons[capital] = tk.Button(self.capital_frame, text=capital, command=lambda c=capital: self.select_capital(c))
        pygame.init()
        pygame.mixer.init()

    def layout_widgets(self):
        self.score_label.pack()
        self.time_label.pack()
        self.country_frame.pack()
        self.capital_frame.pack()
        for country in self.country_buttons.values():
            country.pack(side=tk.LEFT)
        for capital in self.capital_buttons.values():
            capital.pack(side=tk.LEFT)

    def select_country(self, country):
        if self.country_selected:
            self.country_buttons[self.country_selected].config(relief="raised")
        self.country_selected = country
        self.country_buttons[country].config(relief="sunken")
        self.check_match()

    def select_capital(self, capital):
        if self.capital_selected:
            self.capital_buttons[self.capital_selected].config(relief="raised")
        self.capital_selected = capital
        self.capital_buttons[capital].config(relief="sunken")
        self.check_match()

    def check_match(self):
        if self.country_selected and self.capital_selected:
            if self.countries[self.country_selected] == self.capital_selected:
                self.score += 1
                self.matches += 1
                self.score_label.config(text=f"Score: {self.score}")
                self.country_buttons[self.country_selected].config(state="disabled")
                self.capital_buttons[self.capital_selected].config(state="disabled")
                pygame.mixer.music.load("success.mp3")
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.load("error.mp3")
                pygame.mixer.music.play()
                self.country_buttons[self.country_selected].config(relief="raised")
                self.capital_buttons[self.capital_selected].config(relief="raised")
                self.country_selected = None
                self.capital_selected = None
            if self.matches == len(self.countries):
                messagebox.showinfo("Congratulations!", f"Your final score is {self.score}!")
                self.root.quit()

    def update_timer(self):
        minutes, seconds = divmod(self.time_left, 60)
        self.time_label.config(text=f"Time left: {minutes:02d}:{seconds:02d}")
        self.time_left -= 1
        if self.time_left < 0:
            pygame.mixer.music.load("gameover.mp3")
            pygame.mixer.music.play()
            messagebox.showinfo("Game Over!", f"Your final score is {self.score}!")
            self.root.quit()
        else:
            self.root.after(1000, self.update_timer)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = CapitalCityGame()
    game.run()
