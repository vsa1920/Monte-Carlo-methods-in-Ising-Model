# Implementation of Metropolis algorithm

import random
from math import e


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

def simulate(state, J_ij, n, T):
    """
    Simulates at temperature T for N iterations.
    """
    # Single flipping
    for dummy in range(n):
        switch = (random.choice(range(len(state))), random.choice(range(len(state))))
        neighbours = nearest_neighbours(switch[0], switch[1], len(state))
        change_E = 0
        for pos in neighbours:
            change_E += 2 * J_ij[((switch[0], switch[1]), pos)] * state[pos[0]][pos[1]] * state[switch[0]][switch[1]]
        p = acceptance_ratio(change_E, T)
        rand_num = random.random()
        if rand_num <= p:
            state[switch[0]][switch[1]] *= -1
    return state



