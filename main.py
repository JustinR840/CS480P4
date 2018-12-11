from AlphaBeta import DoAlphaBeta
from MinMax import DoMinMax
from Helpers import GetProblemChoice, GetInputFile, GenerateWinStatesForGridSize, CheckBoardLegality

def main():
	GenerateWinStatesForGridSize(4, 4)

	# Main loop. Keep running until we break out when selection == 3 (Quit Program)
	while(True):
		selection = GetProblemChoice()

		if(selection == 3):
			print("Quitting Program")
			break

		board = GetInputFile()
		CheckBoardLegality(board)
		if(selection == 1):
			DoMinMax(board)
		elif(selection == 2):
			DoAlphaBeta(board)

		print()


if __name__ == "__main__":
	main()