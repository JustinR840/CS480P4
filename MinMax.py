from Helpers import WhatWasTheMove, IsLeaf, Eval, Successors, WhoseTurnIsIt

num_nodes_expanded = 0


def DoMinMax(current_board):
	whose_turn_is_it = WhoseTurnIsIt(current_board)
	print("Turn: Player", whose_turn_is_it)

	better_board, val = MinMax(current_board, whose_turn_is_it, whose_turn_is_it)
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
	else:
		print("Root Node Value: 0.5 (Draw)")

	print("Best Next Move:", move)
	print("Number of Nodes Expanded:", num_nodes_expanded)


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
		_, y = MinMax(new_board, nextPlayer, original_player)
		if(current_player == original_player):
			if(y > val):
				val = y
				better_board = list(new_board)
		else:
			if(y < val):
				val = y
				better_board = list(new_board)
	return better_board, val
