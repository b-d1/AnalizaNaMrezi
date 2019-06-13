import networkx as nx

G = nx.read_edgelist('soc-sign-bitcoinotc.csv', delimiter=',', nodetype=int, data=(('weight', int), ('timestamp', float)), encoding="utf-8")

core_number = nx.core_number(G)
k_core = nx.k_core(G)
enumerate_cliques = nx.enumerate_all_cliques(G)
find_cliques = nx.find_cliques(G) # all maximal cliques
graph_clique_number = nx.graph_clique_number(G) # all maximal cliques
graph_number_of_cliques = nx.graph_number_of_cliques(G) # all maximal cliques

edge_betweenness_centrality = nx.edge_betweenness_centrality(G)

print("Core number for each node: ", core_number)
print("K-core: ", k_core)
print("Cliques: ", enumerate_cliques)
print("All maximal cliques: ", find_cliques)
print("Graph clique number - size of the largest clique for the graph: ", graph_clique_number)
print("Number of maximal cliques in the graph:  ", graph_number_of_cliques)
print("Edge betweenness: ", edge_betweenness_centrality)