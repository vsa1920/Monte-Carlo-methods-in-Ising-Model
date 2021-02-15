# Get equilibrium states at various temperatures

from Wolff import Wolff
from Analyze import evaluate_energy, evaluate_magnetisation
from matplotlib import pyplot
import numpy
import random

# Grid size
N = 50

T_lst = [round(x, 2) for x in numpy.arange(2.3, 2.35, 0.04)]

for T in T_lst:
    random_state1 = [[random.choice([1, -1]) for i in range(N)] for j in range(N)]
    Sground_state = [[1 for i in range(N)] for j in range(N)]
    
    # Plotting Correlation Functions
    E1_grid = []
    E2_grid = []
    M1_grid = []
    M2_grid = []
    x_grid = []
    for i in range(20000):
        Wolff(random_state1, T, 1)
        Wolff(ground_state, T, 1)
        E1_grid.append(evaluate_energy(random_state1))
        E2_grid.append(evaluate_energy(ground_state))
        M1_grid.append(abs(evaluate_magnetisation(random_state1)))
        M2_grid.append(abs(evaluate_magnetisation(ground_state)))
        x_grid.append(i)
    pyplot.plot(x_grid, E1_grid)
    pyplot.plot(x_grid, E2_grid)
    pyplot.savefig("T = " + str(T) + "E.png")
    pyplot.clf()
    pyplot.plot(x_grid, M1_grid)
    pyplot.plot(x_grid, M2_grid)
    pyplot.savefig("T = " + str(T) + "M.png")
    pyplot.clf()

    print (len(x_grid))
    # Save equibrium state at the temperature
    if T < 2.69:
        state = ground_state
    else:
        state = random_state1
        
    file = open("T = " + str(T) +".txt", 'w')
    for i in range(len(state)):
        for j in range(len(state)):
            file.write(str(state[i][j]) + ' ')
        file.write('\n')
    file.close()
        
print ("Output generated.")
