import networkx as nx

G = nx.read_edgelist('soc-sign-bitcoinotc.csv', delimiter=',', nodetype=int, data=(('weight', int), ('timestamp', float)), encoding="utf-8")

is_connected = nx.is_connected(G)
number_connected_components = nx.number_connected_components(G)

# is_strongly_connected = nx.is_strongly_connected(G)
# number_strongly_connected_components = nx.number_strongly_connected_components(G)

# is_weakly_connected = nx.is_weakly_connected(G)
# number_weakly_connected_components = nx.number_weakly_connected_components(G)

is_biconnected = nx.is_biconnected(G)
biconnected_components = nx.biconnected_components(G)

# is_semiconnected = nx.is_semiconnected(G)
# is_aperiodic = nx.is_aperiodic(G)

# page_rank = nx.pagerank(G, max_iter=10000)
#
# hubs, authorities = nx.hits(G, max_iter=10000)


print("Is graph connected:", is_connected)
# print("Is graph strongly connected:", is_strongly_connected)
# print("Is graph weakly connected:", is_weakly_connected)
print("Is graph biconnected:", is_biconnected)
# print("Is graph semiconnected:", is_semiconnected)
# print("Is graph aperiodic:", is_aperiodic)

print("Number of connected components:", number_connected_components)
# print("Number of strongly connected components:", number_strongly_connected_components)
# print("Number of weakly connected components:", number_weakly_connected_components)
print("Number of bi-connected components:", biconnected_components)


# print("Page rank:", page_rank)
# print("HITS hubs:", hubs)
# print("HITS authorities", authorities)