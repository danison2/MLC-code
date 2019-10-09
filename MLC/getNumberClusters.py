'''
Created on 5 Apr 2018

@author: DanyK
'''
import numpy as np
import networkx as nx
from getMembership import getMembership
from decomposition import decomposition


def getNumberClusters(G):
    A = nx.adjacency_matrix(G).todense()
    (_, n) = A.shape
    # estimate the number of communities starting from 1
    for k in range(1,n):
        _, H = decomposition(A, k)
        M = getMembership(H)
        #print(np.transpose(np.round(M,2)))

        #we assume a  community should have at least one centroid
        # Therefore, we filter only those nodes with 1's and make others 0's
        M[M < 1] = 0
#         print(np.transpose(np.round(M,2)))
        
#         print(M.any(axis=0))
        
        if (~M.any(axis=0)).any():
            #index = np.where(~M.any(axis=0))[0]
#             print("We estimated " + str(k) + " communities because #" + 
#                   str(k + 1) + " yields communities without cluster centers")
            break
    return k-1

# from loadGraph import getGraph
# from BFS import sampleG
# G = getGraph("simple1.txt")
# sampled = [int(node) for node in sampleG(G, 4, 3)]
# subG = nx.subgraph(G, sampled)
# 
# nber = getNumberClusters(subG)
# print("Number of communities after sampling G: ", nber)
