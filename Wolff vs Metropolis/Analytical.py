# Analytical solution to the Ising Model

from scipy import integrate
from numpy import log, e, cos, cosh, sinh, pi
import numpy
from matplotlib import pyplot

def free_energy(T):
    """
    Free Energy at Temperature T.
    """
    beta = 1 / T
    J = 1
    def integrand(x):
        """
        Function to integrate.
        """
        k = (2 * sinh(2 * beta * J)) / (cosh(2 * beta * J) ** 2)
        return log(1 + (1 - (k * cos(x)) ** 2) ** 0.5)
    return -log(2) / 2 - log(cosh(2 * beta * J)) - (integrate.quad(integrand, 0, pi)[0] / (2 * pi))

def magnetization(T):
    beta = 1 / T
    J = 1
    T_c = 2 / log(1 + 2 ** 0.5)
    if T >= T_c:
        return 0
    else:
        return (1 - (sinh(2 * beta * J)) ** (-4)) ** (1 / 8)

def derivative(x_grid, y_grid):
    x1_grid = []
    der_grid = []
    for i in range(1, len(x_grid)):
        x1_grid.append(x_grid[i])
        der_grid.append((y_grid[i] - y_grid[i - 1]) / (x_grid[i] - x_grid[i - 1]))
    return x1_grid, der_grid

"""
x_grid = numpy.arange(0.2, 1, 0.001)
y_grid = [free_energy(1/x) for x in x_grid]
x1_grid, y1_grid = derivative(x_grid, y_grid)
x2_grid, y2_grid = derivative(x1_grid, y1_grid)
s_grid = [(x2_grid[i] ** 2) * (y2_grid[i] ** 2) for i in range(len(x2_grid))]
t_grid = [1 / x for x in x2_grid]

pyplot.plot(t_grid, s_grid)
pyplot.ylim(0, 100)
pyplot.show()
"""
