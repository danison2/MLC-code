'''
Created on 4 Apr 2018

@author: DanyK
'''
import networkx as nx
import numpy as np
from loadGraph import getGraph
from loadSeeds import getSeeds
from loadGroundTruth import getGroundTruth
from getNumberClusters import getNumberClusters
import getScoringFx as score
from writeToFile import writeConductances, writeF1
from computeF1Score import computeF1Score
from createFolders import createFolders
from detectCommunities import getCommunities
from plotCommunities import plotSubgraph
from BFS import sampleGraph
graphFiles=['graphA.txt']
communityFile='newComA.txt'
seedsFiles=['seedsA3.txt']
delimiter = "\t"

# graphFiles = ['simple1.txt']
# communityFile = 'com-simple1.txt'
# seedsFiles = ['seedsSimple1.txt']
# delimiter = " "

max_level = 2
alpha = 0.75

def main():
    for graphFile, seedsFile in zip(graphFiles, seedsFiles): #multiple graphs in array
        #prepare folders
        createFolders()
        f1 = open('../F1/' + graphFile, "w+")
        f1.close()
        f2 = open('../Cond/' + graphFile, "w+")
        f2.close() 
        #step 1: 
        G = getGraph(graphFile, delimiter)
        #step2:
        seeds = getSeeds(seedsFile)
        #step3:
        SumF1 = 0
        i = 0
        for seed in seeds:
            print("Seed: ", seed)
            sampled = sampleGraph(G, seed, max_level)
            subG = nx.subgraph(G, sampled)
            #step4:
            clusters = getNumberClusters(subG)
            detected = getCommunities(subG, clusters, alpha)
            print("Detected: ", str(len(detected)) + " communities")
            #step5: evaluation
            groundTruth = getGroundTruth(communityFile, seed)
            print("Ground truth: ", str(len(groundTruth)) + " communities")
            #optional
            #plot the communities
#             plotSubgraph(subG, detected)
            sumLen = 0
            avgLen = 0
            for k in range(len(groundTruth)):
                sumLen += len(groundTruth[k])
            avgLen = int(sumLen / (k + 1))
            if avgLen <= 20:  # work with communities not bigger than 20 nodes
            #end optional
                F1 = computeF1Score(groundTruth, detected)

                SumF1 += F1
                i += 1
                AvgF1 = np.round(SumF1 / i, 2)
                print("Average F1 for detected communities: ", str(AvgF1))
                        
                AvgConductance, AvgComLen = score.getConductance(G, detected)
                print("Average Conductance for detected communities: ", str(AvgConductance))
                writeConductances(graphFile,AvgComLen, AvgConductance)
                
                if i == 100:
                    break
        writeF1(graphFile,i, AvgF1)
main()