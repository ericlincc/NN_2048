import Evolutions as evolution
import pickle

NN_size = [16, 10, 4]
Num_Gen = 20
Num_Pop = 1000
M_Rate = 0.1

evo_1 = evolution.Evolution(NN_size)

Results = evo_1.evolve(Num_Gen, Num_Pop, M_Rate, save_file = True)

with open("./Results/training_1.in", 'w') as f:
	f.write(str(NN_size) + " " + str(Num_Gen) + " " + str(Num_Pop) + " " + str(M_Rate))
	for a in range(len(Results)):
		f.write("\n" + str(Results[a]))
