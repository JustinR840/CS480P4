from copy import deepcopy


def GenerateWinStatesForGridSize(num_rows, num_cols):
	def Backtrack(grid, starting_row, starting_col, win_states):
		# The grid is now in a win state. Append a copy of the grid
		# to the win_states list.
		if (CheckBoardForWin(grid, 'X')):
			win_states.append(deepcopy(grid))

		# Out of bounds
		if (starting_row >= len(grid) and starting_col >= len(grid[0])):
			return

		for row in range(starting_row, len(grid)):
			for col in range(starting_col, len(grid[starting_row])):
				if (grid[row][col] == '-'):
					if (CanPlacePlayerHere(grid, row, col, 'X')):
						grid[row][col] = 'X'
						Backtrack(grid, starting_row + 1, 0, win_states)
					grid[row][col] = '-'

	def CanPlacePlayerHere(grid, row, col, player):
		if (player in grid[row]):
			return False
		for i in range(len(grid)):
			if (grid[i][col] == player):
				return False
		return True

	grid = [['-' for i in range(num_cols)] for j in range(num_rows)]
	win_states = []
	Backtrack(grid, 0, 0, win_states)

	return win_states



# Wrapper function for AlphaBeta. Will time AlphaBeta
# and display the related output.
def DoAlphaBeta():
	board = GetInputFile()
	win_states = GenerateWinStatesForGridSize(4, 4)
	print(Eval2(board, win_states))


# AlphaBeta()


def max_node():
	pass


def AlphaBeta(board, u, alpha, beta, depth):
	if (depth == 0):  # leaf(u)):
		return Eval(board)
	if (max_node(u)):
		res = alpha
		for v in Successors(u):
			val = AlphaBeta(board, v, res, beta, depth - 1)
			res = max(res, val)
			if (res >= beta):
				return res
	else:
		res = beta
		for v in Successors(u):
			val = AlphaBeta(board, v, alpha, res, depth - 1)
			res = min(res, val)
			if (res <= alpha):
				return res

	# TODO: What is this for..?
	return res


def Successors(u):
	for i in range(1):
		yield i


# Static evaluation function from the perspective
# of Player 1.
# Should return 100 if a move here is a win for P1
# Should return -100 if a move here is a loss for P1
# Otherwise, return # of ways P1 can win - # of ways P2 can win
def Eval(board, win_states):
	if (CheckBoardForWin(board, 'X')):
		return 100
	elif (CheckBoardForWin(board, 'O')):
		return -100

	# TODO: Ways P1 can win - Ways P2 can win
	score = 0

	for win_state in range(len(win_states)):
		player_one_score = 0
		player_two_score = 0

		for row in range(len(win_states[win_state])):
			for col in range(len(win_states[win_state][row])):
				if (win_states[win_state][row][col] == 'X'):
					if (board[row][col] == 'X' or board[row][col] == '-'):
						player_one_score += 1
					elif (board[row][col] == 'O' or board[row][col] == '-'):
						player_two_score += 1

		if(player_one_score == 4):
			score += 1
		if(player_two_score == 4):
			score -= 1

	return score


def Eval2(board, winList):
	if (CheckBoardForWin(board, 'X')):
		return 100
	if (CheckBoardForWin(board, 'O')):
		return -100
	# For each player:
	# Traverse the win list. If there is a "P" in the win board position
	# and either a '0' or player symbol ('1' for player 1, '2' for player 2)
	# in the current board position, mark that row and column for that
	# player as filled. At the end of each board comparison, if there are
	# 4 matches, then that is a possible win state for the player
	player1Eval = 0
	for winBoard in winList:
		numMatches = 0
		# Traverse both boards at the same time
		for i in range(len(board)):
			for j in range(len(board[i])):
				if (winBoard[i][j] == "P"):
					if (board[i][j] == 'X' or board[i][j] == '-'):
						numMatches += 1
		if (numMatches == 4):
			player1Eval += 1
	player2Eval = 0
	for winBoard in winList:
		numMatches = 0
		# Traverse both boards at the same time
		for i in range(len(board)):
			for j in range(len(board[i])):
				if (winBoard[i][j] == "P"):
					if (board[i][j] == 'O' or board[i][j] == '-'):
						numMatches += 1
		if (numMatches == 4):
			player2Eval += 1
	return player1Eval - player2Eval


def CheckBoardForWin(board, player):
	row_status = [0, 0, 0, 0]
	col_status = [0, 0, 0, 0]

	for row in range(len(board)):
		for col in range(len(board[row])):
			if (board[row][col] == player):
				row_status[row] = 1
				col_status[col] = 1

	if (0 in row_status or 0 in col_status):
		return False
	else:
		return True


# Ask for an input file. Read the contents of that file.
def GetInputFile():
	print("The input file should be in the same directory as main.py")
	filename = "test.input"  # TODO: input("Enter the name of the input file: ")

	with open(filename) as fp:
		alltext = fp.read()
		return InputToBoard(alltext)


# Transform a string into a 2D array representing the gameboard.
def InputToBoard(text):
	# Initially split the board into an array of strings
	board = text.split('\n')

	# Loop through the strings and convert them to an array of chars
	for row in range(len(board)):
		board[row] = list(board[row])

	return board


# Get a valid input choice from the user so we know what action to perform.
def GetProblemChoice():
	print("Please section a problem number")
	print("(1) MinMax Search")
	print("(2) AlphaBeta Search")
	print("(3) Quit Program")

	selection = input("Selection: ")

	# If the user doesn't pick a valid choice then repeatedly ask for a valid choice.
	while (selection is not "1" and selection is not "2" and selection is not "3"):
		print()
		print("Invalid choice. Valid choices are...")
		print("(1) MinMax Search")
		print("(2) AlphaBeta Search")
		print("(3) Quit Program")
		selection = input("Selection: ")

	# Convert selection to int before returning.
	return int(selection)
