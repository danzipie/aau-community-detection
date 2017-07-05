import networkx as nx
import community as c
import matplotlib.pyplot as plt

# import the graph
G = nx.read_graphml("test1.graphml")

# find communities
dendo = c.generate_dendrogram(G)
for level in range(len(dendo) - 1):
    print("partition at level", level, "is", c.partition_at_level(dendo, level))

partition = c.best_partition(G)
m = c.modularity(partition, G)
print(m)
agglomerate = c.induced_graph(partition, G)

# draw the graph
colors = ["blue", "green", "yellow", "violet", "black", "orange", "cyan", "red", "indigo", "pink"]

plt.figure(1)
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0.

for community in set(partition.values()):
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == community]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size=40, node_color=colors[int(count) % 10])

nx.draw_networkx_edges(G, pos, alpha=0.5)

labels = nx.get_node_attributes(G, 'name')
pos_higher = {}
y_off = 0.02

for k, v in pos.items():
    pos_higher[k] = (v[0], v[1]+y_off)
nx.draw_networkx_labels(G, pos_higher, labels=labels, font_size=10)

plt.show()
