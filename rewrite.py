Key Changes:
Refactored Class (CapitalCityGame):

The CapitalCityGame class now directly takes the root Tkinter window as an argument in its constructor, similar to CountryCapitalGame in Code 2.
Timer with Threading:

The start_timer method now uses a separate thread (threading.Thread) to handle the countdown and update the timer label without blocking the main game loop.
Button Layout:

Buttons are placed in a grid with 5 columns, similar to Code 2's layout (self.buttons_text.index(text) // 5).
Message Feedback:

A message_label is added to show "Correct Match!" or "Incorrect Match!" messages, along with changing the message color (green for correct, red for incorrect).
Sound Effects:

The play_sound method handles the playing of sound files for correct and incorrect matches.
Game End Conditions:

The game ends either when the timer runs out or when all pairs are correctly matched, with a pop-up message displaying the final result.




Game Initialization and Setup: This code creates a graphical country-capital matching game using Tkinter, where players are prompted to match a capital city with its respective country. The main game structure includes a timer, scoring system, and sound effects for user feedback.

Gameplay and Logic: Players select countries and capitals from randomized buttons; when a correct pair is chosen, points are awarded, and both buttons are disabled. Incorrect matches prompt an error message. The game ends when all pairs are matched or time runs out.

Multithreading for Timer: The countdown timer runs in a separate thread to ensure the game remains responsive. Sound effects use Pygame for quick audio feedback on correct and incorrect matches.

Complexity Analysis:

Time Complexity: Button initialization is 
𝑂
(
𝑛
)
O(n), where 
𝑛
n is twice the number of country-capital pairs, as each country and capital has its own button. Match checking is 
𝑂
(
1
)
O(1) for each click, as dictionary access in Python is constant time.
Space Complexity: 
𝑂
(
𝑛
)
O(n) for storing button widgets and country-capital pairs.


import tkinter as tk
from tkinter import messagebox
import random
import pygame
import threading
import time

class CapitalCityGame:
    def __init__(self, root):
        """
        Initializes the game, sets up the Tkinter window, sound effects, and game state.
        """
        self.root = root
        self.root.title("Capital City Matching Game")
        self.root.geometry("500x400")

        # Initialize pygame mixer for sound
        pygame.mixer.init()

        # Game state variables
        self.score = 0
        self.click_count = 0
        self.selected_country = ""
        self.selected_capital = ""
        self.timer_running = True
        self.time_left = 600  # 10 minutes in seconds

        # Country-Capital pairs
        self.capital_dict = {
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

        self.items = list(self.capital_dict.items())
        random.shuffle(self.items)

        # Split and shuffle for random placement of buttons
        self.buttons_text = [item[0] for item in self.items] + [item[1] for item in self.items]
        random.shuffle(self.buttons_text)

        # Create timer label
        self.timer_label = tk.Label(self.root, text="Time left: 10:00", font=("Arial", 14))
        self.timer_label.pack(pady=10)

        # Display the score
        self.score_label = tk.Label(self.root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)

        # Message display
        self.message_label = tk.Label(self.root, text="", font=("Arial", 12), fg="green")
        self.message_label.pack(pady=10)

        # Create button frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        # Initialize buttons
        self.buttons = {}
        for i, text in enumerate(self.buttons_text):
            btn = tk.Button(self.button_frame, text=text, font=("Arial", 10), width=15, command=lambda t=text: self.button_click(t))
            btn.grid(row=i // 10, column=i % 10, padx=5, pady=5)
            self.buttons[text] = btn

        # Start the timer thread
        self.start_timer()

    def start_timer(self):
        """
        Starts the countdown timer in a separate thread.
        """
        def countdown():
            while self.time_left > 0 and self.timer_running:
                mins, secs = divmod(self.time_left, 60)
                time_str = f"{mins:02}:{secs:02}"
                self.timer_label.config(text=f"Time left: {time_str}")
                time.sleep(1)
                self.time_left -= 1

            if self.time_left == 0:
                self.end_game("Game Over! Time's up.")

        timer_thread = threading.Thread(target=countdown)
        timer_thread.start()

    def play_sound(self, file):
        """
        Plays the given sound file using pygame.
        """
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

    def button_click(self, text):
        """
        Handles the click event for buttons.
        Updates the selected country or capital and checks for a match.
        """
        if text in self.capital_dict:
            self.selected_country = text
        elif text in self.capital_dict.values():
            self.selected_capital = text

        self.check_match()

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

                # Disable matched buttons
                self.buttons[self.selected_country].config(state="disabled")
                self.buttons[self.selected_capital].config(state="disabled")

                # Check for game end
                if self.score == len(self.capital_dict):
                    self.end_game("Congratulations! You've matched all pairs!")

            else:
                self.message_label.config(text="Incorrect Match!", fg="red")
                self.play_sound('error.mp3')  # Incorrect match sound

            # Reset selections
            self.selected_country = ""
            self.selected_capital = ""

    def end_game(self, message):
        """
        Ends the game, displaying the final message and stopping the timer.
        """
        self.timer_running = False
        messagebox.showinfo("Game Over", message)

# Run the game
root = tk.Tk()
game = CapitalCityGame(root)
root.mainloop()