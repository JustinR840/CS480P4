NumNodesExpanded = 0


# Wrapper function for AlphaBeta. Will time AlphaBeta
# and display the related output.
def DoAlphaBeta(board):
	win_states = GenerateWinStatesForGridSize(4, 4)
	res = AlphaBeta(board, -1000, 1000, 2, win_states)

	print("Board value is " + str(res))
	print("Number of nodes expanded is " + str(NumNodesExpanded))
	print("Best move is ")
	return res, NumNodesExpanded


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
			if(j == 1):
				p1Count += 1
			elif(j == 2):
				p2Count += 1
	return (p1Count, p2Count)


def AlphaBeta(board, alpha, beta, depth, win_states):
	global NumNodesExpanded
	NumNodesExpanded += 1
	if (depth == 0 or CheckBoardForWin(board, 1) or CheckBoardForWin(board, 2)):
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
			if(col == 1):
				NumP1 += 1
			elif(col == 2):
				NumP2 += 1
	if(NumP1 == NumP2):
		return 2
	else:
		return 1


# Generator function to get successor boards for a single board passed to it
def Successors(board, player):
	# Check the current board for empty spaces. For each empty space,
	# create a new board with the player placing a symbol in the empty
	# space and append it to the successor list.
	for i in range(len(board)):
		for j in range(len(board[i])):
			if (board[i][j] == 0):

				succ = deepcopy(board)
				succ[i][j] = player
				yield succ
