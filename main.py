def main():
	# Main loop. Keep running until we break out when selection == 3 (Quit Program)
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







def DoMinMax():
	board = GetInputFile()
	print(board)


def DoAlphaBeta(u, alpha, beta):
	board = GetProblemChoice()
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
	return res









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