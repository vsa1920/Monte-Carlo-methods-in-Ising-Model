from matplotlib import pyplot as plt

file1 = open("Output1.txt", 'r')
data = [[float(x) for x in line.split()] for line in file1.readlines()]

t_data = []
s_data = []

data.sort()
for s in data:
    t_data.append(s[0])
    s_data.append(s[1])

plt.plot(t_data, s_data, 'ro-')
plt.savefig("Susceptibility.png")
print ("Output generated")
