'''
Created on 31 Mar 2018

@author: DanyK
'''


def sampleGraph(graph, start, max_level):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
    levels = {}         # this dict keeps track of levels
    levels[start] = 0    # depth of start node is 0
    # to avoid inserting the same node twice into the queue
    visited = [start]
    # keep looping until there are nodes still to be checked
    while queue:
        node = queue.pop(0)
        if levels[node] <= max_level:
            explored.append(node)
            neighbours = graph.neighbors(node)
            # add neighbours of node to queue
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)
                    levels[neighbour] = levels[node] + 1
                    # print(neighbour, ">>", levels[neighbour]
    return explored
   
# from loadGraph import getGraph
# G = getGraph("simple1.txt")
# sampled = [int(node) for node in sampleG(G, 4, 3)]
# print(sampled)
