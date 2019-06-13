import networkx as nx

G = nx.read_edgelist('soc-sign-bitcoinotc.csv', delimiter=',', nodetype=int, data=(('weight', int), ('timestamp', float)), encoding="utf-8")

greedy_modularity_communities = nx.algorithms.community.greedy_modularity_communities(G)
k_clique_communities = nx.algorithms.community.k_clique_communities(G, 1)

print("Greedy modularity communities: ", greedy_modularity_communities)
print("K-clique communities, k=1:  ", k_clique_communities)