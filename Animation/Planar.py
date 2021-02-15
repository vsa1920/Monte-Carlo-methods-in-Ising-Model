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
random_state = [[random.random() * (2 * pi) for i in range(N)] for j in range(N)]
ground_state = [[0 for i in range(N)] for j in range(N)]
state = random_state

from matplotlib import animation, rc
from IPython.display import HTML, Image

rc('animation', html='html5')

fig = plt.figure()
x_grid = [[j for i in range(N)] for j in range(N)]
y_grid = [[i for i in range(N)] for j in range(N)]
u_grid = [[cos(state[i][j]) for i in range(N)] for j in range(N)]
v_grid = [[sin(state[i][j]) for i in range(N)] for j in range(N)]
plot = plt.quiver(x_grid, y_grid, u_grid, v_grid)
plt.axis('off')

def animate(*args):
    global state, x_grid, y_grid, u_grid, v_grid
    simulate(state, (N * N), 0)
    u_grid = [[cos(state[i][j]) for i in range(N)] for j in range(N)]
    v_grid = [[sin(state[i][j]) for i in range(N)] for j in range(N)]
    plot.set_UVC(u_grid, v_grid)
    return plot

ani = animation.FuncAnimation(fig, animate, interval = 1, frames = 200)
ani.save("planar.gif", writer = 'imagemagick', fps = 20)
#plt.show()
print ("Animation saved.")
                                                                                
                                                                                

