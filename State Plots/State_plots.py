# An imshow plot of a given state

from matplotlib import pyplot as plt

T_lst = [1.4, 2.2, 2.26, 2.4, 2.46, 2.6, 4.8]

def read_func(file_name):
    file = open(file_name, 'r')
    state = []
    for i in file.readlines():
        row = []
        for j in i.split():
            row.append(int(j))
        state.append(row)
    return state

plt.axis("off")
for T in T_lst:
    state = read_func("T = " + str(T) +".txt")
    plt.imshow(state)
    plt.savefig("T = " + str(T) + ".png")
    plt.clf()

print ("Graphs generated.")
    
