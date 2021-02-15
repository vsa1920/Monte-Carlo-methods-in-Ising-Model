# Implementation of Cluster-Wolff algorithm for Ising Model

import random
from math import e
import sys

sys.setrecursionlimit(2000)

# Value of J
J = 1

def nearest_neighbours(i, j, N):
    """
    Returns the nearest neighbours of a site in the lattice according to periodic boundary conditions.
    """
    return [((i - 1) % N, j), (i, (j - 1) % N), ((i + 1) % N, j), (i, (j + 1) % N)]


def develop_cluster(state, site, T, cluster):
    """
    Develop Cluster with a choosing probability.
    """
    beta = 1 / T
    p = 1 - e ** (-2 * beta * J)
    cluster.append(site)
    spin = state[site[0]][site[1]]
    for neighbour in nearest_neighbours(site[0], site[1], len(state)):
        if state[neighbour[0]][neighbour[1]] == spin:
            if neighbour not in cluster:
                num = random.random()
                if num < p:
                    cluster = develop_cluster(state, neighbour, T, cluster)
    return cluster

def Wolff(state, T, N):
    """
    The Wolff algorithm for Ising model.
    """
    for i in range(N):
        choice = (random.choice(range(len(state))), random.choice(range(len(state))))
        flip = develop_cluster(state, choice, T, [])
        for site in flip:
            state[site[0]][site[1]] *= -1
    return state

"""
random_state = [[random.choice([1, -1]) for i in range(10)] for j in range(10)]
ground_state = [[1 for i in range(10)] for j in range(10)]
from matplotlib import pyplot
Wolff(ground_state, 3, 10000)
pyplot.imshow(ground_state)
pyplot.show()
"""
    

