import Evolutions as evolution
import pickle

evo_1 = evolution.Evolution([16, 10, 4])

Results = evo_1.evolve(2, 100, 0.05, save_file = True)

with open("./Results/R_2_100_005.in", 'w') as f:
	for a in range(len(Results)):
		f.write("\n" + str(Results[a]))
