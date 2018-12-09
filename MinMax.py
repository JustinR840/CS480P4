from copy import deepcopy
from Helpers import all_win_states

num_nodes_expanded = 0


def DoMinMax(current_board):
	better_board, val = MinMax(current_board, 1, 1)
	move = WhatWasTheMove(current_board, better_board)

	if(val == 100):
		print(1, "player 1 wins")
	elif(val == -100):
		print(0, "player 2 wins")
	else:
		print(0.5, "draw")

	print("best move:", move)
	print("number of nodes expanded:", num_nodes_expanded)


def MinMax(current_board, current_player, original_player):
	global num_nodes_expanded
	num_nodes_expanded += 1

	better_board = list(current_board)
	if(IsLeaf(current_board)):
		return better_board, Eval(current_board)

	if(current_player == 1):
		nextPlayer = 2
	else:
		nextPlayer = 1

	if(current_player == original_player):
		val = -100
	else:
		val = 100

	for new_board in Successors(current_board, current_player):
		x, y = MinMax(new_board, nextPlayer, original_player)
		if(current_player == original_player):
			if(y > val):
				val = y
				better_board = list(new_board)
		else:
			if(y < val):
				val = y
				better_board = list(new_board)
	return better_board, val


def WhatWasTheMove(old_board, new_board):
	for i in range(len(old_board)):
		for j in range(len(old_board[i])):
			if(old_board[i][j] != new_board[i][j]):
				return i, j

	raise Exception("boards were the same")


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


# Static evaluation function from the perspective
# of Player 1.
# Should return 100 if a move here is a win for P1
# Should return -100 if a move here is a loss for P1
# Otherwise, return # of ways P1 can win - # of ways P2 can win
def Eval(board):
	if (IsWin(board, 1)):
		return 100
	elif (IsWin(board, 2)):
		return -100


	finalscore = 0

	for win_state in range(len(all_win_states)):
		p1tmp = 0
		p2tmp = 0

		for row in range(len(all_win_states[win_state])):
			for col in range(len(all_win_states[win_state][row])):
				if (all_win_states[win_state][row][col] == 1):
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


def IsLeaf(board):
	# Check if either player has won the game
	if(IsWin(board, 1) or IsWin(board, 2)):
		return True

	# If there are no more available spaces the game is over
	for i in board:
		for j in i:
			if j == 0:
				return False

	return True


def IsWin(board, player):
	row_status = [0, 0, 0, 0]
	col_status = [0, 0, 0, 0]

	for row in range(len(board)):
		for col in range(len(board[row])):
			# A single spot taken by a player counts for
			# the row and column.
			if (board[row][col] == player):
				row_status[row] = 1
				col_status[col] = 1

	# If there are any 0s left then there is a row/column
	# that has yet to be filled.
	if (0 in row_status or 0 in col_status):
		return False
	else:
		return True
