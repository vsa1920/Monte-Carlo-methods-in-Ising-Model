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
