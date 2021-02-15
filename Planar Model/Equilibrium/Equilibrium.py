# Running Simultations for various temperatures
# Computational Experiment

from Metropolis import simulate, nearest_neighbours
import random
from matplotlib import pyplot
from Analyze import read_func, evaluate_energy, evaluate_magnetization
import numpy as np
from numpy import pi, cos, sin
import time

N = 50
T_lst = [round(i, 2) for i in np.arange(1.0, 1.2, 0.02)]
J = 1
t1 = time.time()

for T in T_lst:
    t_a = time.time()
    random_state = [[random.random() * (2 * pi) for i in range(N)] for j in range(N)]
    ground_state = [[pi / 2 for i in range(N)] for j in range(N)]
    # Plotting correlation functions
    x_grid = []
    y_grid = []
    y2_grid = []
    for i in range(20000):
        x_grid.append(i)
        y_grid.append(evaluate_energy(ground_state))
        y2_grid.append(evaluate_energy(random_state))
        simulate(random_state, N * N, T)
        simulate(ground_state, N * N, T)
    pyplot.plot(x_grid, y_grid)
    pyplot.plot(x_grid, y2_grid)
    pyplot.savefig("T = " + str(T) + "E.png")
    pyplot.clf()
    
    
    # Save equibrium state at the temperature
    state = random_state
    file = open("T = " + str(T) +".txt", 'w')
    for i in range(len(state)):
        for j in range(len(state)):
            file.write(str(state[i][j]) + ' ')
        file.write('\n')
    file.close()

    # Quiver Plot of the state
    """
    xv_grid = [[j for i in range(N)] for j in range(N)]
    yv_grid = [[i for i in range(N)] for j in range(N)]
    u_grid = [[cos(state[i][j]) for i in range(N)] for j in range(N)]
    v_grid = [[sin(state[i][j]) for i in range(N)] for j in range(N)]

    pyplot.quiver(xv_grid, yv_grid, u_grid, v_grid)
    pyplot.savefig("Quiver T = " + str(T) + ".png")
    pyplot.clf()
    """
    t_b = time.time()
    print (T, (t_b - t_a) / 60)
    

print ("Output generated")
t2 = time.time()
print ("Time Taken:", (t2 - t1) / 60)
