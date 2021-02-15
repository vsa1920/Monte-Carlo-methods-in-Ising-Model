# Plotting the data

from matplotlib import pyplot
import numpy
from Analytical import free_energy, magnetization, derivative

file = open("Output1.txt", 'r')
file1 = open("Output.txt", 'r')
data = [[float(x) for x in line.split()] for line in file.readlines()[1:]]
data1 = [[float(x) for x in line.split()] for line in file1.readlines()[1:]] 
t_data = []
t_data1 = []  
s_data = []
s_data1 = []
error = []
error1 = []


for s in data:
    t_data.append(s[0])
    s_data.append(s[1])
    error.append(s[3])

for s in data1:
    t_data1.append(s[0])
    s_data1.append(s[1])
    error1.append(s[2])
    
#pyplot.scatter(t_data, s_data)

pyplot.errorbar(t_data, s_data, error, fmt = ".", label = "Metropolis")
pyplot.errorbar(t_data1, s_data1, error1, fmt = ".", label = "Wolff")

x_grid = numpy.arange(0.2, 1, 0.001)
y_grid = [free_energy(1/x) for x in x_grid]
x1_grid, y1_grid = derivative(x_grid, y_grid)
x2_grid, y2_grid = derivative(x1_grid, y1_grid)
s_grid = [-(x2_grid[i] ** 2) * (y2_grid[i]) for i in range(len(x2_grid))]
t_grid = [1 / x for x in x2_grid]

pyplot.plot(t_grid, s_grid, label = "Exact solution")
pyplot.ylim(0, 2.5)
pyplot.legend()
pyplot.savefig("Specific_heat.png")
print ("Graph saved as .png image.")


