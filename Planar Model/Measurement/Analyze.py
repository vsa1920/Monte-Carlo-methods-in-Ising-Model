from matplotlib import pyplot
from Metropolis import nearest_neighbours
import random
from math import e, cos, sin, pi
import numpy as np

# A function to read states from text files

# Constants
J = 1

def read_func(file_name):
    file = open(file_name, 'r')
    state = []
    for i in file.readlines():
        row = []
        for j in i.split():
            row.append(float(j))
        state.append(row)
    return state

def evaluate_energy(state):
    E = 0
    n = len(state)
    for i in range(n):
        for j in range(n):
            for pos in nearest_neighbours(i, j, n):
                E += -J * cos(state[i][j] - state[pos[0]][pos[1]])
    return E / 2

def evaluate_magnetization(state):
    """
    Returns Magnetisation per spin of a state.
    """
    M = np.array([0, 0])
    n = len(state)
    for i in range(n):
        for j in range(n):
            M = M + np.array([cos(state[i][j]), sin(state[i][j])])
    return M / (n * n)
