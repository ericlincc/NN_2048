import numpy as np

import Network_V1 as network
import Game_Def as game
import random_move

class Evolution(object):
	def __init__(self, net_sizes):
		self.network = network.Network(net_sizes)
		
	def evolve(self, num_generations, num_populations, mutation_rate):
		for i in range(num_generations):
			self.network_evolve(num_populations, mutation_rate)
			
	def network_evolve(self, num_populations, mutation_rate):
		num_avg = 10
		network_1 = self.network
		network_2 = self.network
		avg_move_score_1 = self.avg_move_score(network_1, num_avg)
		avg_move_score_2 = self.avg_move_score(network_2, num_avg)
		for i in range(num_populations):
			new_network = self.network
			new_network.mutate(mutation_rate)
			new_avg_move_score = self.avg_move_score(new_network, num_avg)
			if (new_avg_move_score[1] > avg_move_score_2[1]):
				if (new_avg_move_score[1] > avg_move_score_1[1]):
					network_1 = new_network
				else:
					network_2 = new_network
		print(new_avg_move_score)
		i = 0
		for b_1, w_1, b_2, w_2 in zip(network_1.biases, network_1.weights,  
				network_2.biases, network_2.weights):
			self.network.biases[i] = (b_1 + b_2) * 0.5
			self.network.weights[i] = (w_1 + w_2) * 0.5
			i = i + 1

	def play_game_random(self):
		play_board = game.new_game()
		while True:
			[next_play_board, changed] = game.apply_move(play_board, \
					int(random_move.decide_the_move(play_board[0])))
			if (next_play_board[0] == play_board[0]):
				break
			play_board = next_play_board
			if (play_board[1][0] > 1000): 
				break
		#print(play_board[1], '\n', play_board[0])
		return play_board[1]
		
	def play_game_network(self, game_network):
		play_board = game.new_game()
		while True:
			[next_play_board, changed] = game.apply_move(play_board, \
					int(game_network.decide_the_move(play_board[0])))
			if (changed == False):
				break
			play_board = next_play_board
			if (play_board[1][0] > 1000): 
				break
			##print(play_board[1], '\n', play_board[0])
		return play_board[1]
		
	def avg_move_score(self, game_network, num_of_plays):
		avg_move_scores = [0.0, 0.0]
		for x in range(num_of_plays):
			move_score = self.play_game_network(game_network)
			avg_move_scores[0] = avg_move_scores[0] + \
					move_score[0] / num_of_plays
			avg_move_scores[1] = avg_move_scores[1] + \
					move_score[1] / num_of_plays
		return avg_move_scores
