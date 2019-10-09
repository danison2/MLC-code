'''
Created on 19 Sep 2018

@author: DanyK
'''
from decomposition import decomposition
from getMembership import getMembership
import networkx as nx
from operator import itemgetter
from BFS import sampleGraph

def getCommunities(G, clusters, alpha):
    detectedCommunities = []
    A = nx.adjacency_matrix(G).todense()
    nodes = sorted(nx.nodes(G))
    _, H = decomposition(A, clusters)
    M = getMembership(H)
    #print(np.transpose(np.round(M,2)))
    M[M >= alpha] = 1
    # we assume the probability of 0.75 is enough to include a node in a community
    M[M < 1] = 0
    #print(np.transpose(np.round(M,2)))
       
    # map indices of hyperedges in M to the corresponding nodes
    numbering = list(range(len(nodes)))  # create indices 
    for k in range(0, clusters):
        # extract indices of nodes with community membership = 1
        c_indices = [j for i, j in zip(M[:, k], numbering) if i == 1]
        if len(c_indices) == 1:
            c_nodes = [nodes[c_indices[0]]]
        else:
            # convert tuple to list
            c_nodes = list(itemgetter(*c_indices)(nodes))
        
        # Do a 1 step BSF to include the neighbours of the centroids
        temp = []
        for node in c_nodes:
            neighbours = sampleGraph(G, node, 1)
            if node not in temp:
                temp.append(node)
            temp.extend([int(v) for v in neighbours if v not in temp])
        temp = sorted(temp)
        detectedCommunities.append(temp)
    return detectedCommunities
################################################################################
#sample execution
###############################################################################
# from loadGraph import getGraph
# from getNumberClusters import getNumberClusters
# G = getGraph("simple1.txt")
# seed  = 4
# sampled = [int(node) for node in sampleG(G, seed, 3)]
# subG = nx.subgraph(G, sampled)
# nber = getNumberClusters(subG)
# 
# alpha = 0.75
# communities = getCommunities(subG, nber, alpha)
# print("Detected: ", communities)
