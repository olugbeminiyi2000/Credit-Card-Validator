"""
This module implements a Sliding Puzzle game using tkinter.

The game consists of a 3x3 grid of numbered tiles, with one empty space.
The player can move adjacent tiles into the empty space.
The game is won when the tiles are in numerical order, with the empty space at the bottom right.
"""

import tkinter as tk
import random

class SlidingPuzzle:
    """
    Represents a Sliding Puzzle game.

    Attributes:
        master (tk.Tk): The tkinter root window.
        tiles (list of lists): A 3x3 grid of tile values, as strings.
        buttons (list of lists): A 3x3 grid of tkinter Button widgets.
        empty_row (int): The row index of the empty space.
        empty_col (int): The column index of the empty space.
    """

    def __init__(self, master):
        """
        Initializes a new SlidingPuzzle instance.

        Args:
            master (tk.Tk): The tkinter root window.
        """
        self.master = master
        self.master.title("Sliding Puzzle")
        self.tiles = [[str(i + j * 3 + 1) for i in range(3)] for j in range(3)]
        self.tiles[2][2] = ""  # Initialize the empty space at the bottom right.
        self.buttons = [[None] * 3 for _ in range(3)]
        self.empty_row = 2
        self.empty_col = 2
        self.create_ui()

    def create_ui(self):
        """
        Creates the game's user interface, including the tile buttons and the shuffle button.
        """
        for i in range(3):
            for j in range(3):
                # Create a button for each tile, with a command to move the tile when clicked.
                self.buttons[i][j] = tk.Button(self.master, text=self.tiles[i][j], font=("Helvetica", 32), width=4, height=2,
                                              command=lambda r=i, c=j: self.move_tile(r, c))
                self.buttons[i][j].grid(row=i, column=j)
        # Create the shuffle button.
        tk.Button(self.master, text="Shuffle", font=("Helvetica", 16), command=self.shuffle).grid(row=3, columnspan=3)

    def shuffle(self):
        """
        Shuffles the tiles randomly, by repeatedly moving the empty space to a random adjacent position.
        """
        for _ in range(100):  # Repeat 100 times to ensure thorough shuffling.
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, left, down, up.
            dr, dc = random.choice(directions)
            new_row, new_col = self.empty_row + dr, self.empty_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:  # Check if the new position is within the grid.
                # Swap the empty space with the adjacent tile.
                self.tiles[self.empty_row][self.empty_col], self.tiles[new_row][new_col] = self.tiles[new_row][new_col], self.tiles[self.empty_row][self.empty_col]
                self.buttons[self.empty_row][self.empty_col]['text'] = self.tiles[self.empty_row][self.empty_col]
                self.buttons[new_row][new_col]['text'] = self.tiles[new_row][new_col]
                self.empty_row, self.empty_col = new_row, new_col

    def move_tile(self, row, col):
        """
        Moves the tile at the given position to the empty space, if it is adjacent.

        Args:
            row (int): The row index of the tile to move.
            col (int): The column index of the tile to move.
        """
        if abs(row - self.empty_row) + abs(col - self.empty_col) == 1:  # Check if the tile is adjacent to the empty space.
            # Swap the tile with the empty space.
            self.tiles[self.empty_row][self.empty_col], self.tiles[row][col] = self.tiles[row][col], self.tiles[self.empty_row][self.empty_col]
            self.buttons[self.empty_row][self.empty_col]['text'] = self.tiles[self.empty_row][self.empty_col]
            self.buttons[row][col]['text'] = self.tiles[row][col]
            self.empty_row, self.empty_col = row, col
            self.check_win()

    def check_win(self):
        """
        Checks if the game has been won, by comparing the current tile configuration to the winning configuration.

        If the game has been won, displays a congratulatory message.
        """
        win_condition = [[str(i + j * 3 + 1) for i in range(3)] for j in range(3)]
        win_condition[2][2] = ""  # The winning configuration has the empty space at the bottom right.
        if self.tiles == win_condition:
            # Display a congratulatory message.
            tk.Label(self.master, text="Congratulations!!", font=("Helvetica", 16)).grid(row=4, columnspan=3)

if __name__ == "__main__":
    root = tk.Tk()
    app = SlidingPuzzle(root)
    root.mainloop()
