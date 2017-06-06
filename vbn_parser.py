# parse a VBN Forskningsportal RSS feed and returns a graph with nodes corresponding to researchers and edges
# corresponding to collaborations to papers.

import feedparser
import re
import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
people = list()

# Read the XML file imported from VBN
vbn_link = 'http://vbn.aau.dk/en/organisations/massm2m(85af23ac-46dd-4e3a-95af-a3a5e68087ce)/publications.rss'
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
    G.add_nodes_from(idxs)
    for i_t in idxs:
        for i_r in idxs:
            if i_t < i_r:
                G.add_edge(i_t, i_r)

# save the people list
labels_file = open('people.txt', 'w')
for item in people:
    labels_file.write("%s\n" % item)

# visualize the graph
nx.draw(G, with_labels=True)
plt.show()
