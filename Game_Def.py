import numpy as np
import random

def new_game():
	return generate_block([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

def apply_move(board_state, move):
	temp_board_state = board_state
	#rotate board to move direction
	if move !=0:
		for i in range(move):
			temp_board_state = board_rotate_cclockwise(temp_board_state)
	#update blocks
	temp_board_state = board_collapse(temp_board_state, move)
	#return board to original direction
	if move !=0:
		for i in range(4 - move):
			temp_board_state = board_rotate_cclockwise(temp_board_state)
	#generate new random block
	if board_state != temp_board_state:
		temp_board_state = generate_block(temp_board_state)
	return temp_board_state

#add new random block on the board	
def generate_block(board_state):
	num_zero = sum(row.count(0) for row in board_state)
	pos_new_block = random.randint(0, num_zero)
	for i in range(4):
		for j in range(4):
			if (board_state[i][j] == 0):
				pos_new_block = pos_new_block - 1
				if (pos_new_block == 0) : board_state[i][j] = random.randint(1, 2)
	return board_state

#check if the game can continue
def has_empty_space(board_state):
	return (sum(row.count(0) for row in board_state) != 0)

#updating board
def board_collapse(temp_board_state, move):
	for i in range(4):
		temp_line = collapse_line([b[i] for b in temp_board_state])
		for j in range(4):
			temp_board_state[j][i] = temp_line[j]
	return temp_board_state

def collapse_line(line):
	line = list(filter((0).__ne__, line))
	i = 0
	while (len(line) - 1 > i) and (len(line) > 1) :
		if line[i] == line[i + 1]:
			del line[i]
			line[i] = line[i] + 1
		i = i + 1
	while (len(line) != 4):
		line.append(0)
	return line

#rotate the board clockwise by 90 degrees	
def board_rotate_cclockwise(temp_board_state):
	#transpose, reverse rows
	return list(map(list, zip(*temp_board_state)))[::-1]
