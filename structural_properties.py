import networkx as nx

G = nx.read_edgelist('soc-sign-bitcoinotc.csv', delimiter=',', nodetype=int, data=(('weight', int), ('timestamp', float)), encoding="utf-8")

jaccard_coefficient = nx.jaccard_coefficient(G)
degree_assortativity_coefficient = nx.degree_assortativity_coefficient(G)
degree_mixing_matrix = nx.degree_mixing_matrix(G)

print("Degree assortativity coefficient: ", degree_assortativity_coefficient)
print("Degree mixing matrix: ", degree_mixing_matrix)
print("Jaccard coefficients between each node (u and v): ")

for u, v, p in jaccard_coefficient:
    print(u, v, p)

