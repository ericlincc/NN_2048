import numpy as np
import random
import math

def new_game():
	#new board: [[new 4x4 board], [#moves, score]]
	return [generate_block(generate_block([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])),[0,0]]

def apply_move(board_state, move):
	##print("before move: ", move, board_state)
	changed = False
	temp_board_state = board_state
	#rotate board to move direction
	if (move !=0):
		for i in range(move):
			temp_board_state[0] = board_rotate_cclockwise(temp_board_state[0])
	#update blocks
	[temp_board_state, changed] = board_collapse(temp_board_state[0], temp_board_state[1], move, changed)
	#return board to original direction
	if (move !=0):
		for i in range(4 - move):
			temp_board_state[0] = board_rotate_cclockwise(temp_board_state[0])
	#generate new random block, add move number
	#for i in range(4):
	#	for j in range(4):
	#		if (int(board_state[0][i][j]) != int(temp_board_state[0][i][j])): 
	#			changed = True
	##print("applied move: ", move, temp_board_state)
	##print(changed)
	if changed:
		temp_board_state[1][0] = temp_board_state[1][0] + 1
		temp_board_state[0] = generate_block(temp_board_state[0])
	##print("gen new: ", temp_board_state)
	return [temp_board_state, changed]

#add new random block on the board	
def generate_block(board_state):
	num_zero = sum(row.count(0) for row in board_state)
	if (num_zero != 0):
		pos_new_block = random.randint(1, num_zero)
		##print("check:", [num_zero, pos_new_block])
		for i in range(4):
			for j in range(4):
				if (board_state[i][j] == 0):
					pos_new_block = pos_new_block - 1
					if (pos_new_block == 0) : board_state[i][j] = random.randint(1, 2)
	return board_state

#updating board
def board_collapse(temp_board, move_score, move, changed):
	for i in range(4):
		[[temp_line, move_score[1]], changed] = collapse_line([b[i] for b in temp_board], move_score[1], changed)
		for j in range(4):
			temp_board[j][i] = temp_line[j]
	return [[temp_board, move_score], changed]

def collapse_line(line, score, changed):
	temp_line = list(filter((0).__ne__, line))
	i = 0
	while (len(temp_line) - 1 > i) and (len(temp_line) > 1):
		if temp_line[i] == temp_line[i + 1]:
			score = score + int(math.pow(2, temp_line[i] + 1))
			del temp_line[i]
			temp_line[i] = temp_line[i] + 1
		i = i + 1
	while (len(temp_line) != 4):
		temp_line.append(0)
	if (temp_line != line): 
		changed = True
	return [[temp_line, score], changed]

#rotate the board clockwise by 90 degrees	
def board_rotate_cclockwise(temp_board_state):
	#transpose, reverse rows
	return list(map(list, zip(*temp_board_state)))[::-1]
