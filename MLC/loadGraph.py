'''
Created on 31 Mar 2018

@author: DanyK
'''
import numpy as np
import networkx as nx


def getGraph(filename, dlmt):
    #space delimited columns (2 columns)
    x, y = np.loadtxt('../data/graphs/' + filename, unpack=True, delimiter=dlmt)
    nodes = np.unique([x, y]).tolist()
    print("Done loading nodes")
    #create the graph
    G = nx.Graph()
    G.add_nodes_from(nodes)
    connections = zip(x, y)
    G.add_edges_from(connections)
    return G

#G = getGraph("simple1.txt")
#print(nx.info(G))