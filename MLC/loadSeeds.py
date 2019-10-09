'''
Created on 19 Sep 2018

@author: DanyK
'''
def getSeeds(seedsFile): #seedsFile should be a column vector
    seeds = []
    for line in open('../data/seeds/' + seedsFile, 'r'): #loop over the seeds
        line = [int(word) for word in line.split()]
        seeds.append(line[0])
    return seeds

# seeds = getSeeds("seedsA1.txt")
#print("Found ", str(len(seeds))+ " seeds")   
# print(seeds)   