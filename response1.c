import random
import tkinter as tk

class SlidingPuzzle:
    def __init__(self):
        self.tiles = list(range(1, 9)) + [0]
        self.empty_slot = (2, 2)

        self.root = tk.Tk()
        self.root.title("Sliding Puzzle")
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.frame, text=str(self.tiles[i*3 + j]), command=lambda i=i, j=j: self.move_tile((i, j)))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.shuffle_button = tk.Button(self.root, text="Shuffle", command=self.shuffle_tiles)
        self.shuffle_button.pack()

    def are_adjacent(self, tile1, tile2):
        dx = abs(tile1[0] - tile2[0])
        dy = abs(tile1[1] - tile2[1])
        return (dx == 1 and dy == 0) or (dx == 0 and dy == 1)

    def get_empty_slot(self):
        return self.empty_slot

    def swap_tiles(self, tile1, tile2):
        i1, j1 = tile1
        i2, j2 = tile2
        self.tiles[i1*3 + j1], self.tiles[i2*3 + j2] = self.tiles[i2*3 + j2], self.tiles[i1*3 + j1]
        self.buttons[i1][j1].config(text=str(self.tiles[i1*3 + j1]))
        self.buttons[i2][j2].config(text=str(self.tiles[i2*3 + j2]))
        self.empty_slot = tile2

    def move_tile(self, tile):
        empty_slot = self.get_empty_slot()
        if self.are_adjacent(tile, empty_slot):
            self.swap_tiles(tile, empty_slot)
            if self.is_solved():
                self.display_congratulatory_message()

    def shuffle_tiles(self):
        random.shuffle(self.tiles)
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=str(self.tiles[i*3 + j]))
        self.empty_slot = (2, 2)
        while self.is_solved():
            random.shuffle(self.tiles)
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].config(text=str(self.tiles[i*3 + j]))

    def is_solved(self):
        for i, tile in enumerate(self.tiles):
            if tile != i + 1 and (i != 8 or tile != 0):
                return False
        return True

    def display_congratulatory_message(self):
        self.root.title("Congratulations! You solved the puzzle!")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    puzzle = SlidingPuzzle()
    puzzle.run()
