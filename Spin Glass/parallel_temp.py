# Parallel Tempering
from Analyze import evaluate_energy, evaluate_magnetisation
from Metropolis import nearest_neighbours, simulate
import random
from numpy import e, var, mean
from matplotlib import pyplot as plt
#import multiprocessing as mp

N = 10
T1_lst = [0.1, 0.2, 0.3, 0.4, 0.5]
T2_lst = [0.6, 0.7, 0.8, 0.9, 1.0]
t_swap = 50
t_sim = 200
num_average = 10

# Output file
out = open("Output.txt", 'w')

def swap_ratio(state1, state2, T1, T2, J_ij):
    """
    T2 > T1. Swap ratio between parallel simulations.
    """
    beta1 = 1 / T1
    beta2 = 1 / T2
    del_E = evaluate_energy(state2, J_ij) - evaluate_energy(state1, J_ij)
    if del_E > 0:
        return e ** (-(beta1 - beta2) * del_E)
    else:
        return 1
    
def random_J(n):
    """
    Defines a random J_ij for a system of size n x n.
    """
    J_ij = {}
    for i in range(n):
        for j in range(n):
            for pos in nearest_neighbours(i, j, n):
                num = random.choice([1, -1])
                J_ij[((i, j), pos)] = num
                J_ij[(pos, (i, j))] = num
        
    return J_ij

def evaluate_susceptibility(M_lst, n, T):
    beta = 1 / T
    return beta * n * var(M_lst)
    
for i in range(len(T1_lst)):
    sus_list1 = []
    sus_list2 = []
    for j in range(num_average):
        J_ij = random_J(N)
        random_state1 = [[random.choice([1, -1]) for i in range(N)] for j in range(N)]
        random_state2 = [[random.choice([1, -1]) for i in range(N)] for j in range(N)]
        M1_lst = []
        M2_lst = []
        T1 = T1_lst[i]
        T2 = T2_lst[i]
        swap = False
        for k in range(t_swap):
            for t in range(t_sim):
                if t % 2:
                    simulate(random_state1, J_ij, N * N, T1)
                simulate(random_state2, J_ij, N * N, T2)
                if swap and t > (t_sim / 4):
                    M1_lst.append(evaluate_magnetisation(random_state2))
                    M2_lst.append(evaluate_magnetisation(random_state1))
            if swap:
                p = swap_ratio(random_state1, random_state2, T2, T1, J_ij)
            else:
                p = swap_ratio(random_state1, random_state2, T1, T2, J_ij)
            if random.random() < p:
                if swap:
                    swap = False
                else:
                    swap = True
                T1, T2 = T2, T1
        if swap:
            T1, T2 = T2, T1
        sus_list1.append(evaluate_susceptibility(M1_lst, N ** 2, T1))
        sus_list2.append(evaluate_susceptibility(M1_lst, N ** 2, T2))
    out.write("%f \t\t\t %f \n" %(T1_lst[i], mean(sus_list1)))
    out.write("%f \t\t\t %f \n" %(T2_lst[i], mean(sus_list2)))

out.close()
print ("Output generated.")
"""
if swap:
    plt.imshow(random_state2)
else:
    plt.imshow(random_state1)

plt.show()
""" 
    
    
