Below is the corrected code implementation in Python with a 3x3 grid using the Tkinter library. I have added a shuffle button, ensured that only adjacent tiles can be swapped with the empty slot, and displayed a congratulatory message when the puzzle is solved.

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
                self.tiles[self.empty_row][self.empty_col], self.tiles[new_row][new_col] = self.tiles[new_row][new_col], self.tiles[self.empty_row][self.empty_col]
                self.buttons[self.empty_row][self.empty_col]['text'] = self.tiles[self.empty_row][self.empty_col]
                self.buttons[new_row][new_col]['text'] = self.tiles[new_row][new_col]
                self.empty_row, self.empty_col = new_row, new_col

    def move_tile(self, row, col):
        if abs(row - self.empty_row) + abs(col - self.empty_col) == 1:
            self.tiles[self.empty_row][self.empty_col], self.tiles[row][col] = self.tiles[row][col], self.tiles[self.empty_row][self.empty_col]
            self.buttons[self.empty_row][self.empty_col]['text'] = self.tiles[self.empty_row][self.empty_col]
            self.buttons[row][col]['text'] = self.tiles[row][col]
            self.empty_row, self.empty_col = row, col
            self.check_win()

    def check_win(self):
        win_condition = [[str(i + j * 3 + 1) for i in range(3)] for j in range(3)]
        win_condition[2][2] = ""
        if self.tiles == win_condition:
            tk.Label(self.master, text="Congratulations!!", font=("Helvetica", 16)).grid(row=4, columnspan=3)

root = tk.Tk()
app = SlidingPuzzle(root)
root.mainloop()
```

**Explanation of Changes:**

1.  **Added Shuffle Button**: I added a shuffle button to the game by creating a new button with the text "Shuffle" and assigning it the `shuffle` method as its command. This allows the player to shuffle the tiles at the start of the game.
2.  **Improved Shuffle Method**: I modified the `shuffle` method to only swap the empty slot with an adjacent tile, ensuring that the game remains solvable. I achieved this by selecting a random direction (up, down, left, or right) and checking if the new position is within the grid boundaries before swapping the tiles.
3.  **Restricted Tile Movement**: I updated the `move_tile` method to only allow the player to move a tile if it is adjacent to the empty slot. I checked this by verifying that the absolute difference between the row and column indices of the tile and the empty slot is equal to 1.
4.  **Enhanced Win Condition Check**: I modified the `check_win` method to compare the current tile configuration with the winning configuration, which includes the empty slot in the bottom-right corner. If the tiles match the winning configuration, the game displays a congratulatory message.
5.  **Added Congratulatory Message**: I added a congratulatory message that appears when the player solves the puzzle. The message is displayed below the grid, and its font size and style are consistent with the rest of the game.
