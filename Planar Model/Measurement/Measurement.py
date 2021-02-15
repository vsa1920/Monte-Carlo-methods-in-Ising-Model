# Program to Measure Quantities

from matplotlib import pyplot
from Metropolis import simulate
from Analyze import evaluate_energy, evaluate_magnetization, read_func
import numpy
import random

T_lst = [round(i, 2) for i in numpy.arange(1, 1.2, 0.02)]

def measure(state, num_cycles, T):
    E = 0
    M = 0
    E_lst = []
    M_lst = []
    n = len(state)
    for dummy in range(num_cycles):
        simulate(state, n * n, T)
        E_lst.append(evaluate_energy(state))
        M_lst.append((evaluate_magnetization(state)))
    return E_lst, M_lst

def bootstrap(lst, num_samples, T, N):
    n = int(len(lst))
    readings = []
    for i in range(num_samples):
        sample = []
        for j in range(n):
            sample.append(random.choice(lst))
        readings.append(evaluate_specific_heat(sample, T, N))
    return numpy.var(readings) ** 0.5

def bootstrap_m(lst, num_samples, T):
    n = int(len(lst))
    readings = []
    for i in range(num_samples):
        sample = []
        for j in range(n):
            sample.append(random.choice(lst))
        readings.append(evaluate_susceptibility(sample, T))
    return numpy.var(readings) ** 0.5

def evaluate_specific_heat(E_lst, T, N):
    return numpy.var(E_lst) / ((T ** 2) * N)

def evaluate_susceptibility(M_lst, T):
    return numpy.var(M_lst) / (T)


file = open("Output.txt", 'w')
file.write("Temperature \t Specific Heat \t\t Error_s \t\t Magnetisation  \t Susceptibility \t Error_m \n")
for T in T_lst:
    state = read_func("T = " + str(T) +".txt")
    # An estimate of correlation time
    t = 10000
    E_read, M_lst = measure(state, t, T)
    M_read = [M_lst[i][0] for i in range(len(M_lst))]
    S = evaluate_specific_heat(E_read, T, len(state) ** 2)
    X = evaluate_susceptibility(M_read, T)
    M = numpy.mean(M_read)
    print (T, S, bootstrap(E_read, 5000, T, len(state) ** 2), M, X, bootstrap_m(M_read, 5000, T))
    file.write("%.2f \t\t %.6f \t\t %.6f \t\t %.6f \t\t %E \t\t %E \n" %(T, S, bootstrap(E_read, 5000, T, len(state) ** 2), M, X, bootstrap_m(M_read, 5000, T)))

file.close()
print ("Output generated.")
