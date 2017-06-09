""" parse a VBN Forskningsportal RSS feed and returns a graph with nodes corresponding to researchers and edges
    corresponding to collaborations to papers.
"""

import feedparser
import re
import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
people = list()

# Read the XML file imported from VBN
vbn_link = 'http://vbn.aau.dk/da/organisations/antennas-propagation-and-radio-networking(c2c38bb3-3d28-4b2c-8bc4-949211d2d486)/publications.rss?altordering=publicationOrderByPublicationYearThenCreated&pageSize=500'
d = feedparser.parse(vbn_link)

for entry in d['entries']:
    # split the file in substrings and find those that contain a researcher's profile
    entry_s = entry['summary'].rsplit(' ')
    rn = [re.search('persons', e) for e in entry_s]
    paper = list(filter(None, rn))
    for person in paper:
        if person.string not in people:
            people.append(person.string) # [:-1]

    # reeverse search from graph indexes to people profiles
    idxs = [people.index(person.string) for person in paper]

    # add new entries to the graph
    for idx in idxs:
        # find the name and add it as node attribute
        n = re.search(r'/persons/([^(]+)', people[idx]).group(1)
        G.add_node(idx, name=n)

    for i_t in idxs:
        for i_r in idxs:
            if i_t < i_r:
                G.add_edge(i_t, i_r)

# save the people list
labels_file = open('people.txt', 'w')
for item in people:
    labels_file.write("%s\n" % item)

# visualize the graph
labels = nx.get_node_attributes(G, 'name')
nx.draw(G, labels=labels)

plt.show()
nx.write_graphml(G,"test1.graphml")
