import networkx as nx

G = nx.Graph()

G.add_node('A')
G.add_node('B')
G.add_node('C')

G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=3)

shortest_path = nx.dijkstra_path(G, 'A', 'C')

print(G)
print(shortest_path)