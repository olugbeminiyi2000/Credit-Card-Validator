I am developing a sliding puzzle game in Python with a 3x3 grid using the Tkinter library. The game starts with tiles numbered 1 to 8 and an empty slot in the bottom-right corner. When the “Shuffle” button is pressed, the tiles are randomized including the empty slot. The player can move a tile by selecting any tile adjacent to the empty slot, which swaps the selected adjacent tile with the empty slot. The game ends when the tiles are back in numerical order with the empty slot in the bottom-right corner, displaying a congratulatory message "Congratulations!!". 

However, the current code has the below issues: 

	1.	There is no shuffle button.
	2.	It swaps the empty slot to whichever tile I click whether they adjacent to the empty slot or not.
	3.	The game doesn’t always detect when the puzzle is solved.
        4. No congratulatory message displayed when solved.
Below is my code:
```python
import tkinter as tk
import random

class SlidingPuzzle:
    def __init__(self, master):
        self.master = master
        self.master.title("Sliding Puzzle")
        self.tiles = [[str(i + j * 3 + 1) for i in range(3)] for j in range(3)]
        self.tiles[2][2] = ""
        self.buttons = [[None] * 3 for _ in range(3)]
        self.empty_row = 2
        self.empty_col = 2
        self.create_ui()
        self.shuffle()

    def create_ui(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text=self.tiles[i][j], font=("Helvetica", 32), width=4, height=2, command=lambda r=i, c=j: self.move_tile(r, c))
                self.buttons[i][j].grid(row=i, column=j)

    def shuffle(self):
        for _ in range(100):
            row, col = random.randint(0, 2), random.randint(0, 2)
            self.move_tile(row, col)

    def move_tile(self, row, col):
        if abs(row - self.empty_row) <= 2 or abs(col - self.empty_col) <= 2:
            self.tiles[self.empty_row][self.empty_col], self.tiles[row][col] = self.tiles[row][col], self.tiles[self.empty_row][self.empty_col]
            self.buttons[self.empty_row][self.empty_col]['text'] = self.tiles[self.empty_row][self.empty_col]
            self.buttons[row][col]['text'] = self.tiles[row][col]
            self.empty_row, self.empty_col = row, col
            self.check_win()

    def check_win(self):
        if self.tiles == [[str(i + j * 3 + 1) for i in range(3)] for j in range(3)]:
            self.tiles[2][2] = ""
            tk.Label(self.master, text="Congratulations! You solved the puzzle!", font=("Helvetica", 16)).grid(row=3, columnspan=3)

root = tk.Tk()
app = SlidingPuzzle(root)
root.mainloop()
```
