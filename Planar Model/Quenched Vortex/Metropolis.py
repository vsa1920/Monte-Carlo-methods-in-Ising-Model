# Implementation of Metropolis algorithm

import random
from math import e, cos, sin, pi
from matplotlib import pyplot as plt

# Value of J
J = 1


def nearest_neighbours(i, j, N):
    """
    Returns the nearest neighbours of a site in the lattice according to periodic boundary conditions.
    """
    return [((i - 1) % N, j), (i, (j - 1) % N), ((i + 1) % N, j), (i, (j + 1) % N)]

def acceptance_ratio(del_E, T):
    """
    Calculates the acceptance ratio.
    """
    if (del_E) < 0:
        return 1
    elif T == 0:
        return 0
    else:
        beta = 1 / T
        return e ** (-beta * (del_E))
    

def simulate(state, n, T):
    """
    Simulates at temperature T for N iterations.
    """
    # Single flipping
    for dummy in range(n):
        switch = (random.choice(range(len(state))), random.choice(range(len(state))))
        neighbours = nearest_neighbours(switch[0], switch[1], len(state))
        random_theta = random.random() * (2 * pi)
        change_E = 0
        for pos in neighbours:
            change_E -= J * cos(state[pos[0]][pos[1]] - random_theta) - J * cos(state[pos[0]][pos[1]] - state[switch[0]][switch[1]])
        p = acceptance_ratio(change_E, T)
        rand_num = random.random()
        if rand_num <= p:
            state[switch[0]][switch[1]] = random_theta
    return state

N = 20                                                                               
state = [[random.random() * (2 * pi) for i in range(N)] for j in range(N)]
x_grid = [[j for i in range(N)] for j in range(N)]
y_grid = [[i for i in range(N)] for j in range(N)]
u_grid = [[cos(state[i][j]) for i in range(N)] for j in range(N)]
v_grid = [[sin(state[i][j]) for i in range(N)] for j in range(N)]

plt.axis("off")
plt.quiver(x_grid, y_grid, u_grid, v_grid)
plt.savefig("random.png")
plt.clf()

simulate(state, 200 * (N * N), 0)
x_grid = [[j for i in range(N)] for j in range(N)]
y_grid = [[i for i in range(N)] for j in range(N)]
u_grid = [[cos(state[i][j]) for i in range(N)] for j in range(N)]
v_grid = [[sin(state[i][j]) for i in range(N)] for j in range(N)]

plt.axis("off")
plt.quiver(x_grid, y_grid, u_grid, v_grid)
plt.savefig("vortex.png")

print ("Plots saved as .png image")
