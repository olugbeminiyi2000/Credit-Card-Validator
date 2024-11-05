import tkinter as tk
import random
from nltk.corpus import words
from nltk import download
from threading import Timer

download('words')
english_words = set(words.words())

class WordScrambleGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Word Scramble Game")

        self.score = 0
        self.time_left = 120  
        self.current_word = ""
        self.scrambled_word = ""

        self.timer_label = tk.Label(root,
                                    text="Time left: 2:00",
                                    font=("Helvetica", 14))
        self.timer_label.pack(pady=10)

        self.score_label = tk.Label(root,
                                    text="Score: 0",
                                    font=("Helvetica", 14))
        self.score_label.pack(pady=10)

        self.word_label = tk.Label(root, text="", font=("Helvetica", 18))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Helvetica", 16))
        self.entry.pack(pady=10)

        self.feedback_label = tk.Label(root,
                                       text="",
                                       font=("Helvetica", 12),
                                       fg="red")
        self.feedback_label.pack(pady=10)

        self.submit_button = tk.Button(root,
                                       text="Submit",
                                       command=self.check_answer,
                                       font=("Helvetica", 12))
        self.submit_button.pack(pady=10)

        self.play_button = tk.Button(root,
                                     text="Play",
                                     command=self.start_game,
                                     font=("Helvetica", 12))
        self.play_button.pack(pady=10)

    def start_game(self):
        self.score = 0
        self.time_left = 120
        self.update_score()
        self.pick_random_word()
        self.countdown()
        self.play_button.config(text="Quit", command=self.end_game)

    def pick_random_word(self):
        self.current_word = random.choice(
            [word for word in english_words if 4 <= len(word) <= 7])
        self.scrambled_word = self.scramble_word(self.current_word)
        while self.scrambled_word == self.current_word:
            self.scrambled_word = self.scramble_word(self.current_word)
        self.word_label.config(text=self.scrambled_word)
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    def scramble_word(self, word):
        return ''.join(random.sample(word, len(word)))

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def check_answer(self):
        answer = self.entry.get().strip().lower()
        if answer == self.current_word:
            self.score += 10
            self.update_score()
            self.pick_random_word()
        elif answer == "":
            self.feedback_label.config(text="Please enter an answer!")
        elif answer not in english_words:
            self.feedback_label.config(text="Invalid word!")
        else:
            self.feedback_label.config(text="Try again!")

    def countdown(self):
        if self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            self.timer_label.config(text=f"Time left: {mins:02}:{secs:02}")
            self.time_left -= 1
            self.root.after(1000, self.countdown)
        else:
            self.end_game()

    def end_game(self):
        self.word_label.config(text="Game Over!")
        self.feedback_label.config(text=f"Your final score: {self.score}")
        self.entry.delete(0, tk.END)
        self.submit_button.config(state="disabled")
        self.play_button.config(text="Play", command=self.start_game)

# Initialize Tkinter and create game instance
root = tk.Tk()
game = WordScrambleGame(root)
root.mainloop()
