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
	res = AlphaBeta(board, -1000, 1000, 16, win_states)
	print(res)


def max_node(board):
	p1Count, p2Count = CountP1AndP2(board)
	if(p1Count == p2Count):
		return True
	return False

def CountP1AndP2(board):
	p1Count = 0
	p2Count = 0
	for i in range(len(board)):
		for j in board[i]:
			if(j == "X"):
				p1Count += 1
			elif(j == "O"):
				p2Count += 1
	return (p1Count, p2Count)


def AlphaBeta(board, alpha, beta, depth, win_states):
	if (depth == 0 or CheckBoardForWin(board, 'X') or CheckBoardForWin(board, 'O')):
		return Eval(board, win_states)

	nextturn = GetNextTurn(board)

	if (max_node(board)):
		res = alpha
		for v in Successors(board, nextturn):
			val = AlphaBeta(v, res, beta, depth - 1, win_states)
			res = max(res, val)
			if (res >= beta):
				return res
	else:
		res = beta
		for v in Successors(board,nextturn):
			val = AlphaBeta(v, alpha, res, depth - 1, win_states)
			res = min(res, val)
			if (res <= alpha):
				return res

	return res


def GetNextTurn(board):
	NumP1 = 0
	NumP2 = 0
	for row in board:
		for col in row:
			if(col == 'X'):
				NumP1 += 1
			elif(col == 'O'):
				NumP2 += 1
	if(NumP1 == NumP2):
		return 'O'
	else:
		return 'X'


def Successors(board, player):
	# Check the current board for empty spaces. For each empty space,
	# create a new board with the player placing a symbol in the empty
	# space and append it to the successor list.
	for i in range(len(board)):
		for j in range(len(board[i])):
			if (board[i][j] == "-"):

				succ = deepcopy(board)
				if (player == 'X'):
					succ[i][j] = 'X'
				else:
					succ[i][j] = 'O'
				yield succ


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


	finalscore = 0

	for win_state in range(len(win_states)):
		p1tmp = 0
		p2tmp = 0

		for row in range(len(win_states[win_state])):
			for col in range(len(win_states[win_state][row])):
				if (win_states[win_state][row][col] == 'X'):
					if (board[row][col] == 'X'):
						p1tmp += 1
					elif (board[row][col] == 'O'):
						p2tmp += 1
					else:
						p1tmp += 1
						p2tmp += 1

		if(p1tmp == 4):
			finalscore += 1
		elif(p2tmp == 4):
			finalscore -= 1

	return finalscore


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
