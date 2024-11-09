The rewritten code introduces several key updates to enhance the functionality and flow of the game.

The game now starts with a paused state, where all buttons, including the 'Start Game' button, are initially disabled. When the user clicks 'Start Game,' the game begins, the timer starts, and all buttons are enabled for interaction.

The end_game method has been updated to disable all buttons, including both the randomized buttons and the 'Start Game' button, when the game ends. This prevents further interactions after the game concludes.

In the reset_game method, the game state is reset (score, timer, message), and all buttons are disabled. The 'Start Game' button is re-enabled, and the randomized capital-city pairs are shuffled again, readying the game for a new round.

This restructuring ensures that no further interaction is possible after the timer expires or all matches are made, effectively fixing the issue where buttons remained active after the game ended.
