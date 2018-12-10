from AlphaBeta import DoAlphaBeta
from MinMax import DoMinMax
from Helpers import GetProblemChoice, GetInputFile, GenerateWinStatesForGridSize, WhoseTurnIsIt

def main():
	GenerateWinStatesForGridSize(4, 4)
	board = GetInputFile()
	#DoMinMax(board)
	print()
	print()
	DoAlphaBeta(board)


	return



	# Main loop. Keep running until we break out when selection == 3 (Quit Program)
	while(True):
		selection = GetProblemChoice()

		if(selection == 1):
			board = GetInputFile()
			DoMinMax(board)
			# oldBoard = GetInputFile()
			# newBoard, value, numNodes = DoMinMax(oldBoard)
			# if(numNodes > 1):
			# 	# Output 1 if win for 1st player
			# 	# Output 0.5 if draw
			# 	# Output 0 if win for 2nd player
			# 	if(value > 0):
			# 		print("Board value is 1")
			# 	elif(value < 0):
			# 		print("Board value is 0")
			# 	elif(value == 0):
			# 		print("Board value is 0.5")
			# elif(numNodes == 1):
			# 	print("Board value is " + str(value))
			# print("Number of nodes expanded is " + str(numNodes))
			# move = ConvertBoardToMove(oldBoard, newBoard)
			# print("Best move is " + str(move))
		elif(selection == 2):
			board = GetInputFile()
			DoAlphaBeta(board)
		elif(selection == 3):
			print("Quitting Program")
			break
		print()


if __name__ == "__main__":
	main()