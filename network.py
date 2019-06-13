import networkx as nx
import matplotlib.pyplot as plt
import math
import numpy as np

G = nx.read_edgelist('soc-sign-bitcoinotc.csv', delimiter=',', nodetype=int, data=(('weight', int), ('timestamp', float)), encoding="utf-8")

degrees = nx.degree(G)
nodes = nx.nodes(G)
nodes_num = len(nodes)
sorted_degrees = sorted(degrees, key= lambda pair: pair[0])
degs = [item[0] for item in sorted_degrees]
cnts = [item[1] for item in sorted_degrees]

# Plot degrees with counts for each degree
plt.subplot(2, 2, 1)
plt.bar(degs, cnts, width=0.80, color='b')

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")

# plt.show()


frequencies = []
for item in sorted_degrees:
    freq = item[1]/nodes_num
    frequencies.append(freq)

# Plot degrees with frequencies
plt.subplot(2, 2, 2)

plt.plot(degs, cnts, '.')

plt.title("Frequencies plot")
plt.ylabel("Frequency")
plt.xlabel("Degree")


log_degrees = []
log_frequencies = []

for i in range(nodes_num):
    log_degrees.append(math.log10(degs[i]))
    log_frequencies.append(math.log10(frequencies[i]))

plt.subplot(2, 2, 3)

# Plot log log plot
plt.plot(log_degrees, log_frequencies, '.')

order = np.argsort(log_degrees)
logk_array = np.array(log_degrees)[order]
logPk_array = np.array(log_frequencies)[order]
m, c = np.polyfit(logk_array, logPk_array, 1)

# 2 < M < 3 for scale free network
print("M", m)

plt.plot(logk_array, m*logPk_array + c, "-")

plt.title("Log log plot")
plt.ylabel("Log frequency")
plt.xlabel("Log degree")

plt.subplot(2, 2, 4)

nx.draw(G)
plt.title("Plot drawing")


plt.show()
