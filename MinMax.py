from Helpers import WhatWasTheMove, IsLeaf, Eval, Successors, WhoseTurnIsIt, IsMaxNode

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
		print("Root Node Value: 0.5 (Draw) (Actual:", val, ")")

	print("Best Next Move:", move)
	print("Number of Nodes Expanded:", num_nodes_expanded)


def MinMax(current_board, current_player, original_player):
	global num_nodes_expanded
	num_nodes_expanded += 1

	better_board = current_board
	if(IsLeaf(current_board)):
		return better_board, Eval(current_board, original_player)

	if(current_player == 1):
		next_player = 2
	else:
		next_player = 1

	if(IsMaxNode(current_board, original_player)):
		val = -999
	else:
		val = 999

	for new_board in Successors(current_board, current_player):
		x, y = MinMax(new_board, next_player, original_player)

		if(IsMaxNode(current_board, original_player)):
			if(y > val):
				val = y
				better_board = x
		else:
			if(y < val):
				val = y
				better_board = x
	return better_board, val
