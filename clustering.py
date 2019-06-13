import networkx as nx

G = nx.read_edgelist('soc-sign-bitcoinotc.csv', delimiter=',', nodetype=int, data=(('weight', int), ('timestamp', float)), encoding="utf-8")

degrees = nx.degree(G)
nodes = nx.nodes(G)
nodes_num = len(nodes)

triangles = nx.triangles(G)
transitivity = nx.transitivity(G)
clustering = nx.clustering(G)
average_clustering = nx.average_clustering(G)
square_clustering = nx.square_clustering(G)
# diameter = nx.diameter(G)
degree_centrality = nx.degree_centrality(G)

print("Number of triangles:", triangles)
print("Transitivity coefficient:", transitivity)
print("Clustering coefficient:", clustering)
print("Average clustering coefficient:", average_clustering)
print("Square clustering coefficient:", square_clustering)
# print("Diameter:", diameter)
print("Degree centrality:", degree_centrality)