'''
Created on 6 Apr 2018

@author: DanyK
'''
import numpy as np
import difflib
import math
import collections
from collections import Counter


def computeF1Score(groundTruth, detectedCommunities):
    #get similar community from the list of communities
    #Option 1:
    sum_F1 = 0
    i = 0
    for com in groundTruth:
        sim = {}
        for detected in detectedCommunities:
            counterA = Counter(detected)
            counterB = Counter(com)
            similarity = counter_cosine_similarity(counterA, counterB)
            sim.update({similarity: detected})
        od = collections.OrderedDict(sorted(sim.items()))
        item = od.popitem()  # removes the last item
        max_sim, nodes = item

#          #Option 2:
#         for com in all_communities:
#             similarity=difflib.SequenceMatcher(None, ground_truth, com)
#             sim.update({similarity.ratio():com}) # similarity in %
#         max_sim,nodes=getMaxSimilarity(sim)

#         print("Ground truth: ", com)
#         print("Most similar: ", nodes)
        #print("Similarity: ", max_sim)
        #print("\n")

        #evaluation
        tp = np.intersect1d(com, nodes)  # nodes in common
        # len(nodes)-tp.size #total returned - the number of true returned
        fp = [node for node in nodes if node not in com]
        # len(communities)-tp.size #total correct - correct returned
        fn = [node for node in com if node not in nodes]
#         print("Community: ",ground_truth)
#         print("Returned: ",nodes)
#         print("Common nodes: ",tp)
#         print("Additional nodes returned: ",fp,len(fp))
#         print("Nodes not returned: ",fn, len(fn))
#         print("# of community nodes: ", len(ground_truth))
#         print("# of common nodes: ",len(tp))
        prec = len(tp) / (len(tp) + len(fp))
        rec = len(tp) / (len(tp) + len(fn))
        if len(tp) == 0 and len(fp) == 0 and len(fn) == 0: #avoid division by zero 
            prec = 1
            rec = 1
            F1 = 1
        elif prec == 0:
            F1 = 0
        else:
            F1 = (2 * prec * rec) / (prec + rec)
        #print("F1: ", F1)
        sum_F1 += F1
        i += 1
    avg_F1 = sum_F1 / i
    return avg_F1


def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)


def getMaxSimilarity(similarity_list):
    max_sim = next(iter(similarity_list))
    for item in similarity_list.items():  
        sim, nodes = item
        if sim > max_sim:
            max_sim = sim
            nodes = nodes
    return max_sim, nodes
