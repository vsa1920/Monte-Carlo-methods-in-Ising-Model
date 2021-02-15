# Running Simultations for various temperatures
# Computational Experiment

from Metropolis import simulate, nearest_neighbours
import random
from matplotlib import pyplot
from Analyze import read_func, measure, evaluate_energy, evaluate_magnetisation
import numpy as np

N = 100
T_lst = [round(i, 1) for i in np.arange(1.0, 5, 0.2)]
print (T_lst)
J = 1
t_eq = 20000

for T in T_lst:
    ground_state = [[-1 for i in range(N)] for j in range(N)]
    random_state = [[random.choice([1, -1]) for i in range(N)] for j in range(N)]
    # Plotting correlation functions
    x_grid = []
    y_grid = []
    y2_grid = []
    y3_grid = []
    y4_grid = []
    for i in range(t_eq):
        x_grid.append(i)
        y_grid.append(evaluate_energy(ground_state))
        y2_grid.append(evaluate_energy(random_state))
        y3_grid.append(abs(evaluate_magnetisation(ground_state)))
        y4_grid.append(abs(evaluate_magnetisation(random_state)))
        simulate(random_state, N * N, T)
        simulate(ground_state, N * N, T)
    pyplot.plot(x_grid, y_grid)
    pyplot.plot(x_grid, y2_grid)
    pyplot.savefig("T = " + str(T) + "E.png")
    pyplot.clf()
    pyplot.plot(x_grid, y3_grid)
    pyplot.plot(x_grid, y4_grid)
    pyplot.savefig("T = " + str(T) + "M.png")
    pyplot.clf()
    
    # Save equibrium state at the temperature
    # An estimate of critical temperature is used to improve equilibrium convergence
    if T > 2.6:
        state = random_state
    else:
        state = ground_state
    file = open("T = " + str(T) +".txt", 'w')
    for i in range(len(state)):
        for j in range(len(state)):
            file.write(str(state[i][j]) + ' ')
        file.write('\n')
    file.close()
    print (T)

print ("Output generated")
