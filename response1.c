A developer has created a sliding puzzle game in Python with a 3x3 grid. The game starts with tiles numbered 1 to 8 and an empty slot in the bottom-right corner. When the “Shuffle” button is pressed, the tiles are randomized. The player can move a tile by selecting any tile adjacent to the empty slot, which swaps their positions. The game ends when the tiles are back in numerical order with the empty slot in the bottom-right corner, displaying a congratulatory message.

However, the code has a few issues:

	1.	Sometimes tiles move even if they are not adjacent to the empty slot.
	2.	The shuffle feature occasionally leaves the tiles in the correct order, which makes the puzzle too easy.
	3.	The game doesn’t always detect when the puzzle is solved.

Review the code and identify the likely causes of these issues. Suggest specific changes to fix these bugs and improve the gameplay experience.
