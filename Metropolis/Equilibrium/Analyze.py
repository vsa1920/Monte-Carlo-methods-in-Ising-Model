from matplotlib import pyplot
from Metropolis import nearest_neighbours, acceptance_ratio
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

def measure_simulate(state, n, T):
    """
    Simulates at temperature T for N iterations.
    """
    E = evaluate_energy(state)
    M = evaluate_magnetisation(state)
    # Single flipping
    for dummy in range(n):
        switch = (random.choice(range(len(state))), random.choice(range(len(state))))
        neighbours = nearest_neighbours(switch[0], switch[1], len(state))
        change_E = 0
        for pos in neighbours:
            change_E += 2 * J * state[pos[0]][pos[1]] * state[switch[0]][switch[1]]
        change_M = -2 * state[switch[0]][switch[1]] 
        p = acceptance_ratio(change_E, T)
        rand_num = random.random()
        if rand_num <= p:
            state[switch[0]][switch[1]] *= -1
            E += change_E
            M += change_M
    return E, M

def measure(state, num_cycles, T):
    E = 0
    M = 0
    N = len(state)
    for dummy in range(num_cycles):
        e, m = measure_simulate(state, N * N, T)
        E += e
        M += m
    return E / num_cycles, M / num_cycles
    
