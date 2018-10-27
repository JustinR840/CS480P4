def main():
	while(True):
		selection = GetProblemChoice()

		if(selection == 1):
			DoMinMax()
		elif(selection == 2):
			DoAlphaBeta()
		elif(selection == 3):
			print("Quitting Program")
			break
		print()

# Check the legality of the board
# A board is illegal if:
# One player has two or more positions captured than the other player
# Both players have one
def CheckBoard(board):

	# First, count the number of X's and O's
	XCount = 0
	OCount = 0
	

	for i in range(len(board)):
		for j in board[i]:
			if(j == 'X'):
				XCount += 1
			elif(j == 'O'):
				OCount += 1

	# Take the absolute value of the difference of X's and O's
	# If this value is greater than 1, return -1
	if(abs(XCount - OCount) > 1):
		print("Board value: -1")
		return -1

	# Next, check if player 1 won
	Player1Win = True

	# If there are fewer than 4 X's, player 1 hasn't won
	if(XCount < 4):
		Player1Win = False

	# Check player 1's victory if they may have won
	# Compute this by seeing if player 1 has enough X's in the
	# correct positions to win
	if(Player1Win):
		RowsFilled = [False] * 4
		ColsFilled = [False] * 4
		for i in range(len(board)):
			for j in range(len(board[i])):
				if(board[i][j] == 'X'):
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
	if(OCount < 4):
		Player2Win = False

	# Check player 1's victory if they may have won
	# Compute this by seeing if player 1 has enough X's in the
	# correct positions to win
	if(Player2Win):
		RowsFilled = [False] * 4
		ColsFilled = [False] * 4
		for i in range(len(board)):
			for j in range(len(board[i])):
				if(board[i][j] == 'O'):
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


# Recursive minimax prodecure
def DoMinMax():
	# Get the board from the input file
	board = GetInputFile()

	#print(board)

	# Check if the board is legal. End the function with a -1 if not legal.
	# Also end the function if player 1 or 2 has won
	BoardValue = CheckBoard(board)
	if(BoardValue != 2):
		return BoardValue
	

	#TODO: Output board value
	# Output 1 if win for 1st player
	# Output 0.5 if draw
	# Output 0 if win for 2nd player


def DoAlphaBeta():
	board = GetProblemChoice()
	print(board)









# Ask for an input file. Read the contents of that file.
def GetInputFile():
	print("The input file should be in the same directory as main.py")
	filename = "test.input" #TODO: input("Enter the name of the input file: ")

	with open(filename) as fp:
		alltext = fp.read()
		return InputToBoard(alltext)


# Transform a string into a 2D array representing the gameboard.
def InputToBoard(text):
	board = text.split('\n')
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
	while(selection is not "1" and selection is not "2" and selection is not "3"):
		print()
		print("Invalid choice. Valid choices are...")
		print("(1) MinMax Search")
		print("(2) AlphaBeta Search")
		print("(3) Quit Program")
		selection = input("Selection: ")

	return int(selection)


main()