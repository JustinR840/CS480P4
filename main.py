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







def DoMinMax():
	board = GetInputFile()
	print(board)


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