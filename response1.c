Here's an updated version of your code that addresses the issues you mentioned:

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

    def create_ui(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text=self.tiles[i][j], font=("Helvetica", 32), width=4, height=2, command=lambda r=i, c=j: self.move_tile(r, c))
                self.buttons[i][j].grid(row=i, column=j)
        tk.Button(self.master, text="Shuffle", font=("Helvetica", 16), command=self.shuffle).grid(row=3, columnspan=3)

    def shuffle(self):
        for _ in range(100):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            dr, dc = random.choice(directions)
            new_row, new_col = self.empty_row + dr, self.empty_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                self.move_tile(new_row, new_col)

    def move_tile(self, row, col):
        if abs(row - self.empty_row) + abs(col - self.empty_col) == 1:
            self.tiles[self.empty_row][self.empty_col], self.tiles[row][col] = self.tiles[row][col], self.tiles[self.empty_row][self.empty_col]
            self.buttons[self.empty_row][self.empty_col]['text'] = self.tiles[self.empty_row][self.empty_col]
            self.buttons[row][col]['text'] = self.tiles[row][col]
            self.empty_row, self.empty_col = row, col
            self.check_win()

    def check_win(self):
        winning_state = [[str(i + j * 3 + 1) for i in range(3)] for j in range(3)]
        winning_state[2][2] = ""
        if self.tiles == winning_state:
            tk.Label(self.master, text="Congratulations!!", font=("Helvetica", 16)).grid(row=4, columnspan=3)

root = tk.Tk()
app = SlidingPuzzle(root)
root.mainloop()
```

Here are the key changes I made:

1. I added a "Shuffle" button to the UI, which calls the `shuffle` method when clicked.
2. I modified the `shuffle` method to only move the empty tile to an adjacent position, rather than moving any tile to the empty position. This ensures that the puzzle remains solvable.
3. I modified the `move_tile` method to only allow moves that are adjacent to the empty tile. This prevents the player from moving tiles that are not adjacent to the empty tile.
4. I modified the `check_win` method to compare the current state of the puzzle to the winning state, rather than comparing it to a state with the empty tile in the wrong position. This ensures that the game correctly detects when the puzzle has been solved.
5. I added a congratulatory message to the UI when the puzzle is solved.
