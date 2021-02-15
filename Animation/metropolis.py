# Implementation of Metropolis algorithm

import random
from math import e

# Value of J
J = 1

# Size of grid
N = 100
T = 1.2

random_state = [[random.choice([1, -1]) for i in range(N)] for j in range(N)]
ground_state = [[-1 for i in range(N)] for j in range(N)]
state = random_state

def nearest_neighbours(i, j, N):
    """
    Returns the nearest neighbours of a site in the lattice according to periodic boundary conditions.
    """
    return [((i - 1) % N, j), (i, (j - 1) % N), ((i + 1) % N, j), (i, (j + 1) % N)]

def acceptance_ratio(del_E, T):
        """
        Calculates the acceptance ratio.
        """
        # value of beta = 1 / (boltzmann constant * T)
        beta = 1 / T
        if (del_E) < 0:
            return 1
        else:
            return e ** (-beta * (del_E))
        
def simulate(n, T, start = False):
    global state
    """
    Simulates at temperature T for N iterations.
    """
    step = 0
    cycle = 0
    # Single flipping
    for dummy in range(n):
        switch = (random.choice(range(len(state))), random.choice(range(len(state))))
        neighbours = nearest_neighbours(switch[0], switch[1], len(state))
        change_E = 0
        for pos in neighbours:
            change_E += 2 * J * state[pos[0]][pos[1]] * state[switch[0]][switch[1]]
        p = acceptance_ratio(change_E, T)
        step += 1
        if step == 100 * 100:
            cycle += 1
        rand_num = random.random()
        if rand_num <= p:
            state[switch[0]][switch[1]] *= -1
            if start:
                break


from matplotlib import pyplot
from matplotlib import animation, rc
from IPython.display import HTML, Image

rc('animation', html='html5')

fig = pyplot.figure()

pyplot.axis("off")
im = pyplot.imshow(state, animated = True)

def update_fig(*args):
    global state
    simulate(N ** 2, T)
    im.set_data(state)
    return im,

ani = animation.FuncAnimation(fig, update_fig, frames = 50, interval = 50, blit = True)
ani.save("metropolis.gif", writer = 'imagemagick', fps = 10)
#pyplot.show()
print ("Animation saved.")
