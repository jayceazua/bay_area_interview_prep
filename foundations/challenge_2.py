# Former Google Coding Interview Question: https://techdevguide.withgoogle.com/paths/foundational/coding-question-minesweeper/#!
# Implement Minesweeper

# Minesweeper is a game where the objective is correctly identify the location of all mines in a given grid. 
# You are given a uniform grid of gray squares in the beginning of the game. Each square contains either 
# a mine(indicated by a value of 9), or an empty square. Empty squares have a number indicating the count 
# of mines in the adjacent squares. Empty squares can have counts from zero(no adjacent mines) up to 8 (all adjacent squares are mines).

# If you were to take a complete grid, for example, you can see which squares have mines and which squares are empty:

# 0  0  0  0  0
# 0  0  0  0  0
# 1  1  1  0  0
# 1  9  1  0  0
# 1  2  2  1  0
# 0  1  9  1  0
# 0  1  1  1  0

# The squares with "2" indicate that there 2 mines adjacent to that particular square.

# Gameplay starts with a user un-hiding a square at random. If the square contains a mine, 
# the game ends. If it is a blank, the number of adjacent mines is revealed.

# Exposing a zero means that there are no adjacent mines, so exposing all adjacent squares is guaranteed safe. 
# As a convenience to the player, the game continues to expose adjacent squares until a non-zero square is reached.

# For example, if you click on the top right corner you get this('-' means hidden):
