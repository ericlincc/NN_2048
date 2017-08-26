import Evolutions as evolution
import pickle

NN_size = [16, 10, 4]
Num_Gen = 20
Num_Pop = 200
Num_Avg = 2000
M_Rate = 0.1

evo_1 = evolution.Evolution(NN_size)

Results = evo_1.evolve(Num_Gen, Num_Pop, M_Rate, num_avg = Num_Avg, save_file = True)

with open("./Results/training_1.in", 'w') as f:
	f.write(str(NN_size) + " " + str(Num_Gen) + " " + str(Num_Pop) + " " + str(Num_Avg) + " " + str(M_Rate))
	for a in range(len(Results)):
		f.write("\n" + str(Results[a]))

with open("./Results/training_1.pkl", 'wb') as output:
	pickle.dump( evo_1, output, pickle.HIGHEST_PROTOCOL)
