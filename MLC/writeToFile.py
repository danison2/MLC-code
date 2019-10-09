'''
Created on 20 Sep 2018

@author: DanyK
'''
def writeF1(graphFile,nber_seeds, avgF1):
    #write average F1 scores from all seeds
    with open('../F1/' + graphFile, "a") as myfile:
            myfile.write(" Average F1: " + str(avgF1) +
                         " for " + str(nber_seeds) + " seeds \n")
def writeConductances(graphFile,community_length, avgCond):      
    #write average conductance of comunities detected from all seeds
    with open('../Cond/' + graphFile, "a") as myfile:
            myfile.write(" Average conductances: " + str(avgCond) +
                         " for " + str(community_length) + " seeds \n")
            