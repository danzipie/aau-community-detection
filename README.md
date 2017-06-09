# aau-community-detection
Explore the Aalborg University social network and test graph analysis algorithms

## Dependencies

This project depends on networkx Python package and on community module.
The module can be installed with the command:

```
pip install python-louvain
```
## Purpose

The purpose of this project is to analyze the Aalborg University social network based on the collaborations among researchers. The collaborations can be downloaded by VBN website, that is open access. The collaboration graph is saved in a .graphml file.

We can open the .graphml file and perform some basic analysis, such as the community detection done in vbn_community_detection.py
