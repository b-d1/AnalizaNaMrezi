import networkx as nx

G = nx.read_edgelist('soc-sign-bitcoinotc.csv', delimiter=',', nodetype=int, data=(('weight', int), ('timestamp', float)), encoding="utf-8")


degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
load_centrality = nx.load_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)

degree_pearson_correlation_coefficient = nx.degree_pearson_correlation_coefficient(G)

print("Degree centrality:", degree_centrality)
print("Betweenness centrality:", betweenness_centrality)
print("Load centrality:", load_centrality)
print("Eigenvector centrality:", eigenvector_centrality)
print("Closeness centrality:", closeness_centrality)

print("Degree pearson correlation coefficient:", degree_pearson_correlation_coefficient)