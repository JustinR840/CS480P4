def main():
	global player1Sym
	player1Sym = '1'
	global player2Sym
	player2Sym = '2'
	global blankSym
	blankSym = '0'

	# Intialize winning board one time so we don't have to recalculate it
	calcWinPos()

	# Main loop. Keep running until we break out when selection == 3 (Quit Program)
	while(True):
		selection = GetProblemChoice()

		if(selection == 1):
			board = DoMinMax(GetInputFile())
			for i in range(len(board[0])):
				print(board[0][i])
		elif(selection == 2):
			DoAlphaBeta()
		elif(selection == 3):
			print("Quitting Program")
			break
		print()

# Calculate all winning positions
def calcWinPos():
	# There are 24 ways to win (permutations of (0, 1, 2, 3)) for both
	# coordinates.
	global winList
	winList = []
	winBoard = [[blankSym for i in range(4)] for j in range(4)]

	for i in range(4):
		for j in range(4):
			for k in range(4):
				for l in range(4):
					# Pick the 1st one
					winBoard[i][0] = "P"

					# Pick the 2nd one (j != i)
					if(j == i):
						continue
					winBoard[j][1] = "P"

					# Pick the 3rd one (k != j)
					if(k == j):
						continue
					winBoard[k][2] = "P"

					# Pick the 4th one (l != k)
					if(l == k):
						continue
					winBoard[k][3] = "P"

# Count the number of player 1 symbols and player 2 symbols
def CountP1AndP2(board):
	p1Count = 0
	p2Count = 0
	for i in range(len(board)):
		for j in board[i]:
			if(j == player1Sym):
				p1Count += 1
			elif(j == player2Sym):
				p2Count += 1
	return (p1Count, p2Count)

# Check the legality of the board
# A board is illegal if:
# One player has two or more positions captured than the other player
# Both players have won
def CheckBoardLegality(board):

	# First, count the number of X's and O's
	p1Count, p2Count = CountP1AndP2(board)

	# Take the absolute value of the difference of X's and O's
	# If this value is greater than 1, return -1
	if(abs(p1Count - p2Count) > 1):
		print("Board value: -1")
		return -1

	# Next, check if player 1 won
	Player1Win = True

	# If there are fewer than 4 X's, player 1 hasn't won
	if(p1Count < 4):
		Player1Win = False

	# Check player 1's victory if they may have won
	# Compute this by seeing if player 1 has enough X's in the
	# correct positions to win
	if(Player1Win):
		RowsFilled = [False] * 4
		ColsFilled = [False] * 4
		for i in range(len(board)):
			for j in range(len(board[i])):
				if(board[i][j] == player1Sym):
					RowsFilled[i] = True
					ColsFilled[j] = True

		# Check to make sure all rows and columns have been filled
		# If they haven't, player 1 has not won yet
		for i in RowsFilled:
			if(i == False):
				Player1Win = False
		for j in ColsFilled:
			if(j == False):
				Player1Win = False

	# Check Player 2 in the same fasion for O's
	# Next, check if player 1 won
	Player2Win = True

	# If there are fewer than 4 X's, player 1 hasn't won
	if(p2Count < 4):
		Player2Win = False

	# Check player 1's victory if they may have won
	# Compute this by seeing if player 1 has enough X's in the
	# correct positions to win
	if(Player2Win):
		RowsFilled = [False] * 4
		ColsFilled = [False] * 4
		for i in range(len(board)):
			for j in range(len(board[i])):
				if(board[i][j] == player2Sym):
					RowsFilled[i] = True
					ColsFilled[j] = True

		# Check to make sure all rows and columns have been filled
		# If they haven't, player 1 has not won yet
		for i in RowsFilled:
			if(i == False):
				Player2Win = False
		for j in ColsFilled:
			if(j == False):
				Player2Win = False

	# If player 1 and player 2 have won, return -1
	if(Player1Win and Player2Win):
		print("Board value: -1")
		return -1

	# If player 1 won, return 1
	if(Player1Win):
		print("Board value: 1")
		return 1

	# If player 2 won, return 0
	if(Player2Win):
		print("Board value: 0")
		return 0

	# Otherwise, continue as normal
	return 2

# Check and return if a given player has won (1 or 2)
def CheckPlayerVictory(board, player):
	# Initialize the player won boolean
	hasWon = True

	# If there are fewer than 4 of the player's symbols (X or O),
	# the player has not yet won
	p1Count, p2Count = CountP1AndP2(board)
	if(player == 1):
		if(p1Count < 4):
			hasWon = False
	else:
		if(p2Count < 4):
			hasWon = False

	# Check player's victory if they may have won
	# Compute this by seeing if the player has enough symbols in the
	# correct positions to win
	if(hasWon):
		rowsFilled = [False] * 4
		colsFilled = [False] * 4
		for i in range(len(board)):
			for j in range(len(board[i])):
				if(player == 1):
					if(board[i][j] == player1Sym):
						rowsFilled[i] = True
						colsFilled[j] = True
				else:
					if(board[i][j] == player2Sym):
						rowsFilled[i] = True
						colsFilled[j] = True

		# Check to make sure all rows and columns have been filled
		# If they haven't, the player has not won yet
		for i in rowsFilled:
			if(i == False):
				hasWon = False
		for j in colsFilled:
			if(j == False):
				hasWon = False
				
	return hasWon

# Checks if the board is a leaf node (either the board is filled or
# one of the players has won).
# R
def Leaf(board):
	# Check if each player has won. If a player has won, the board
	# is at a leaf node
	if(CheckPlayerVictory(board, 1) or CheckPlayerVictory(board, 2)):
		return True

	# Count # of X's and O's. If they both equal 8, the board is full
	if(CountP1AndP2(board) == (8,8)):
		return True

	# Otherwise, the current board is not at a leaf node
	return False

# Returns the static evaluation of the node
# The static evaluation is as follows:
# 100 if a win for player one,
# -100 if a win for player two
# Else,
# The static eval is:
# Number of ways player 1 can win - number of ways player 2 can win
# To count the number of ways a player can win:
# 
def Eval(board):
	if(CheckPlayerVictory(board, 1)):
		return 100
	if(CheckPlayerVictory(board, 2)):
		return -100

	if(CountP1AndP2(board) == (8,8)):
		return 0

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
				if(winBoard[i][j] == "P"):
					if(board[i][j] == player1Sym or board[i][j] == blankSym):
						numMatches += 1

		if(numMatches == 4):
			player1Eval += 1

	player2Eval = 0
	for winBoard in winList:
		numMatches = 0

		# Traverse both boards at the same time
		for i in range(len(board)):
			for j in range(len(board[i])):
				if(winBoard[i][j] == "P"):
					if(board[i][j] == player2Sym or board[i][j] == blankSym):
						numMatches += 1

		if(numMatches == 4):
			player2Eval += 1

	return player1Eval - player2Eval

# Returns true if the node is a max node, false otherwise
# Basically, true if it is player 1's turn, false if player 2's
# Since player 1 (X) goes first, if there are an equal number of
# X's and O's, it is player 1's turn
# Else, it is player 2's turn
def MaxNode(board):
	p1Count, p2Count = CountP1AndP2(board)
	if(p1Count == p2Count):
		return True
	return False

# Return a list of all immediate successor boards for the given player
def Succ(board, player):
	succList = []

	# Check the current board for empty spaces. For each empty space,
	# create a new board with the player placing a symbol in the empty
	# space and append it to the successor list.
	for i in range(len(board)):
		for j in range(len(board[i])):
			if(board[i][j] == blankSym):
				succ = board.copy()
				if(player == 1):
					succ[i][j] = player1Sym
				else:
					succ[i][j] = player2Sym
				succList.append(succ)

	return succList

# Recursive minimax prodecure
def DoMinMax(u):

	# Check if the board is legal. End the function with a -1 if not legal.
	# Also end the function if player 1 or 2 has won
	BoardValue = CheckBoardLegality(u)
	if(BoardValue != 2):
		return (u, BoardValue)

	#TODO: Output board value
	# Output 1 if win for 1st player
	# Output 0.5 if draw
	# Output 0 if win for 2nd player


	# Return the static evaluation if the current board is a leaf node
	if(Leaf(u)):
		return (u, Eval(u))

	# Which player's turn is it?
	curPlayer = -1

	# Initialize the current static eval value
	val = 0

	# Initialize return value for MAX node
	if(MaxNode(u)):
		val = float("-inf")
		curPlayer = 1

	# Initialize return value for MIN node
	else:
		val = float("inf")
		curPlayer = 2
	
	# Resulting board
	res = None

	# Traverse successor list
	for v in Succ(u, curPlayer):

		# Recursive call at MAX node
		if(curPlayer == 1):
			if(DoMinMax(v)[1] > val):
				res = v
				val = DoMinMax(v)[1]

		# Recursive call at MIN node
		else:
			if(DoMinMax(v)[1] < val):
				res = v
				val = DoMinMax(v)[1]

	# Return final evaluation
	return (res, val)


def DoAlphaBeta(u, alpha, beta):
	"""board = GetProblemChoice()
	print(board)

	# TODO: Need some way to determine our leaf nodes. A max depth?
	if(leaf(u)):
		return Eval(p)
	if(max_node(u)):
		res = alpha
		for each v in succ(u):
			val = DoAlphaBeta(v, res, beta)
			res = max_of(res, val)
			if(res >= beta):
				return res
	else:
		res = beta
		for each v in succ(u):
			val = DoAlphaBeta(v, alpha, res)
			res = min_of(res, val)
			if(res <= alpha):
				return res

	# What is this for..?
	return res"""

# Ask for an input file. Read the contents of that file.
def GetInputFile():
	print("The input file should be in the same directory as main.py")
	filename = "test.input" #TODO: input("Enter the name of the input file: ")

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
	while(selection is not "1" and selection is not "2" and selection is not "3"):
		print()
		print("Invalid choice. Valid choices are...")
		print("(1) MinMax Search")
		print("(2) AlphaBeta Search")
		print("(3) Quit Program")
		selection = input("Selection: ")

	# Convert selection to int before returning.
	return int(selection)


main()