import feedparser
import re
import networkx as nx

def parse_vbn(vbn_link, G):

    """ parse a VBN Forskningsportal RSS feed and returns a graph with nodes corresponding to researchers and edges
        corresponding to collaborations to papers.
    """

    # initialize
    people = list()

    # parse website (input is not validated!)
    d = feedparser.parse(vbn_link)

    # create the graph
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

    return G
