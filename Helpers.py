from copy import deepcopy


all_win_states = []


def GenerateWinStatesForGridSize(num_rows, num_cols):
	def Backtrack(grid, starting_row, starting_col, win_states):
		# The grid is now in a win state. Append a copy of the grid
		# to the win_states list.
		if (CheckBoardForWin(grid, 1)):
			win_states.append(deepcopy(grid))

		# Out of bounds
		if (starting_row >= len(grid) and starting_col >= len(grid[0])):
			return

		for row in range(starting_row, len(grid)):
			for col in range(starting_col, len(grid[starting_row])):
				if (grid[row][col] == 0):
					if (CanPlacePlayerHere(grid, row, col, 1)):
						grid[row][col] = 1
						Backtrack(grid, starting_row + 1, 0, win_states)
					grid[row][col] = 0

	def CanPlacePlayerHere(grid, row, col, player):
		if (player in grid[row]):
			return False
		for i in range(len(grid)):
			if (grid[i][col] == player):
				return False
		return True

	grid = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
	win_states = []
	Backtrack(grid, 0, 0, win_states)

	global all_win_states
	all_win_states = win_states


# Static evaluation function from the perspective
# of Player 1.
# Should return 100 if a move here is a win for P1
# Should return -100 if a move here is a loss for P1
# Otherwise, return # of ways P1 can win - # of ways P2 can win
def Eval(board, win_states):
	if (CheckBoardForWin(board, 1)):
		return 100
	elif (CheckBoardForWin(board, 2)):
		return -100


	finalscore = 0

	for win_state in range(len(win_states)):
		p1tmp = 0
		p2tmp = 0

		for row in range(len(win_states[win_state])):
			for col in range(len(win_states[win_state][row])):
				if (win_states[win_state][row][col] == 1):
					if (board[row][col] == 1):
						p1tmp += 1
					elif (board[row][col] == 2):
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


# Check the legality of the board
# A board is illegal if:
# One player has two or more positions captured than the other player
# Both players have won
def CheckBoardLegality(board):
	# First, count the number of X's and O's
	p1Count, p2Count = CountP1AndP2(board)

	# Take the absolute value of the difference of 1's and 2's
	# If this value is greater than 1, return -1
	if (abs(p1Count - p2Count) > 1):
		return -1

	# Next, check if player 1 won
	Player1Win = True

	# If there are fewer than 4 X's, player 1 hasn't won
	if (p1Count < 4):
		Player1Win = False

	# Check player 1's victory if they may have won
	# Compute this by seeing if player 1 has enough X's in the
	# correct positions to win
	if (Player1Win):
		RowsFilled = [False] * 4
		ColsFilled = [False] * 4
		for i in range(len(board)):
			for j in range(len(board[i])):
				if (board[i][j] == 1):
					RowsFilled[i] = True
					ColsFilled[j] = True

		# Check to make sure all rows and columns have been filled
		# If they haven't, player 1 has not won yet
		for i in RowsFilled:
			if (i == False):
				Player1Win = False
		for j in ColsFilled:
			if (j == False):
				Player1Win = False

	# Check Player 2 in the same fasion for O's
	# Next, check if player 1 won
	Player2Win = True

	# If there are fewer than 4 X's, player 1 hasn't won
	if (p2Count < 4):
		Player2Win = False

	# Check player 1's victory if they may have won
	# Compute this by seeing if player 1 has enough X's in the
	# correct positions to win
	if (Player2Win):
		RowsFilled = [False] * 4
		ColsFilled = [False] * 4
		for i in range(len(board)):
			for j in range(len(board[i])):
				if (board[i][j] == 2):
					RowsFilled[i] = True
					ColsFilled[j] = True

		# Check to make sure all rows and columns have been filled
		# If they haven't, player 1 has not won yet
		for i in RowsFilled:
			if (i == False):
				Player2Win = False
		for j in ColsFilled:
			if (j == False):
				Player2Win = False

	# If player 1 and player 2 have won, return -1
	if (Player1Win and Player2Win):
		# print("Board value: -1")
		return -1

	# If player 1 won, return 1
	if (Player1Win):
		# print("Board value: 1")
		return 1

	# If player 2 won, return 0
	if (Player2Win):
		# print("Board value: 0")
		return 0

	# Otherwise, continue as normal
	return 2







def ConvertBoardToMove(oldBoard, newBoard):
	for r in range(4):
		for c in range(4):
			if (oldBoard[r][c] != newBoard[r][c]):
				return (r, c)


# Ask for an input file. Read the contents of that file.
def GetInputFile():
	#print("The input file should be in the same directory as main.py")
	filename = "test.input" # input("Enter the name of the input file: ")

	with open(filename) as fp:
		alltext = fp.read()
		return InputToBoard(alltext)

# Transform a string into a 2D array representing the gameboard.
def InputToBoard(text):
	# Initially split the board into an array of strings
	board = text.split('\n')

	# Loop through the strings and convert them to an array of chars
	for row in range(len(board)):
		board[row] = list(map(int, board[row].replace(' ', ''))) # Quick hack to fix space-delimiting

	return board

# Get a valid input choice from the user so we know what action to perform.
def GetProblemChoice():
	print("Please section a problem number")
	print("(1) MinMax Search")
	print("(2) AlphaBeta Search")
	print("(3) Quit Program")

	selection = input("Selection: ")

	# If the user doesn't pick a valid choice then repeatedly ask for a valid choice.
	while(selection is not "1" and selection is not "2" and selection is not "3"):
		print()
		print("Invalid choice. Valid choices are...")
		print("(1) MinMax Search")
		print("(2) AlphaBeta Search")
		print("(3) Quit Program")
		selection = input("Selection: ")

	# Convert selection to int before returning.
	return int(selection)
