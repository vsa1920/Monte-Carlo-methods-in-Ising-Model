from matplotlib import pyplot
from Wolff import nearest_neighbours, Wolff
import random
from math import e

# A function to read states from text files

# Constants
J = 1

def read_func(file_name):
    file = open(file_name, 'r')
    state = []
    for i in file.readlines():
        row = []
        for j in i.split():
            row.append(int(j))
        state.append(row)
    return state

def evaluate_energy(state):
    E = 0
    n = len(state)
    for i in range(n):
        for j in range(n):
            for pos in nearest_neighbours(i, j, n):
                E += -J * state[i][j] * state[pos[0]][pos[1]]
    return E / 2

def evaluate_magnetisation(state):
    """
    Returns Magnetisation per spin of a state.
    """
    M = 0
    n = len(state)
    for i in range(n):
        for j in range(n):
            M += state[i][j]
    return M / (n * n)


