import networkx as nx
import matplotlib.pyplot as plt
import vbn_parser as p

# initialize
G = nx.Graph()
link = 'http://vbn.aau.dk/da/organisations/antennas-propagation-and-radio-networking(c2c38bb3-3d28-4b2c-8bc4-949211d2d486)/publications.rss?altordering=publicationOrderByPublicationYearThenCreated&pageSize=500'

# populate the graph
p.parse_vbn(link, G)

# visualize the graph
labels = nx.get_node_attributes(G, 'name')
nx.draw(G, labels=labels)

plt.show()
nx.write_graphml(G,"test1.graphml")
