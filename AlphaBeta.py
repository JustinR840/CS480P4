from Helpers import IsLeaf, Eval, Successors, WhatWasTheMove, WhoseTurnIsIt

num_nodes_expanded = 0


def DoAlphaBeta(current_board):
	whose_turn_is_it = WhoseTurnIsIt(current_board)
	print("Turn: Player", whose_turn_is_it)

	better_board, val = AlphaBeta(current_board, -999, 999, whose_turn_is_it, whose_turn_is_it, 14)
	move = WhatWasTheMove(current_board, better_board)

	for i in current_board:
		print(i)

	if(whose_turn_is_it == 1):
		other_player = 2
	else:
		other_player = 1

	if(val == 100):
		print("Root Node Value:", val, "(Player", whose_turn_is_it, "Wins)")
	elif(val == -100):
		print("Root Node Value:", val, "(Player", other_player, "Wins)")
	# else:
	# 	print(0.5, "draw")

	print("Best Next Move:", move)
	print("Number of Nodes Expanded:", num_nodes_expanded)


def AlphaBeta(current_board, alpha, beta, current_player, original_player, depth):
	global num_nodes_expanded
	num_nodes_expanded += 1

	better_board = list(current_board)
	if(IsLeaf(current_board) or depth == 1):
		return better_board, Eval(current_board)

	if(current_player == 1):
		nextPlayer = 2
	else:
		nextPlayer = 1

	if(current_player == original_player):
		res = alpha
		for new_board in Successors(current_board, current_player):
			x, val = AlphaBeta(new_board, res, beta, nextPlayer, original_player, depth - 1)
			if(val > res):
				res = val
				better_board = list(x)
			#res = max(res, val)
			if(res >= beta):
				return better_board, res
	else:
		res = beta
		for new_board in Successors(current_board, current_player):
			x, val = AlphaBeta(new_board, alpha, res, nextPlayer, original_player, depth - 1)
			if(val < res):
				res = val
				better_board = list(x)
			#res = min(res, val)
			if(res <= alpha):
				return better_board, res

	return better_board, res
