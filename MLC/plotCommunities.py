'''
Created on 20 Sep 2018

@author: DanyK
'''
import networkx as nx
from matplotlib import pyplot as plt
import itertools


def plotSubgraph(subgraph, all_communities):
    #..................plot the subgraph

    #     in case we want to use specific colors
    colors = ['c', 'm', 'blueviolet', 'orchid',
              'loyalblue', 'limegreen', 'b', 'k', 'r']

    nodes = sorted(nx.nodes(subgraph))
    n = len(nodes)
    # compute graph layout
    pos = nx.spring_layout(subgraph, dim=2, k=0.1,
                           pos=None, fixed=None, iterations=50,
                           weight='weight', scale=1.0, center=None)
    plt.figure(figsize=(5, 5))  # image is 8 x 8 inches
    plt.axis('off')

    #...............Optional

    # figsize is intentionally set small to condense the graph
    #     fig, ax = plt.subplots(figsize=(5,5))
    #     margin=0.33
    #     fig.subplots_adjust(margin, margin, 1.-margin, 1.-margin)
    #     ax.axis('equal')

    if(all_communities !=None):
        color_overlap = 'y'  # orange color for overlapping nodes
        clusters = len(all_communities)
        #loop over communities
        #current list
        remaining = []
        current_list = []

        #............ End optional
        for k in range(0, clusters):
            current_list = all_communities[k]
            remaining = [
                rem_list for rem_list in all_communities if rem_list != current_list]
            rem_flat = list(itertools.chain.from_iterable(remaining))
            overlap = [node for node in current_list if node in rem_flat]
    
            ##generate a random RBG color
            #color = np.random.rand(3,)
            #or use a color from my preference
            color = colors[k]
    
            #draw the community with the colour
            nx.draw_networkx_nodes(
                subgraph, pos, nodelist=current_list, node_color=color, 
                node_size=500, alpha=0.8)
            nx.draw_networkx_nodes(subgraph, pos, nodelist=overlap,
                                   node_color=color_overlap, 
                                   node_size=400, alpha=0.8)
            #nx.draw_networkx_nodes(subgraph, pos,node_size=600,
            #cmap=plt.get_cmap('jet'), node_color=n_colors)
    else:
        nx.draw_networkx_nodes(subgraph, pos, nodelist=nodes,
                               node_color=colors[0],
                                node_size=500, alpha=0.8)
    nx.draw_networkx_edges(subgraph, pos, alpha=0.8)
    labels = {}
    for j in range(n):
        node = nodes[j]
        labels.update({node: node})
    #draw the labels by adding customized labels
    nx.draw_networkx_labels(subgraph, pos, labels,
                            font_size=10, font_family='sans-serif')
    plt.savefig("../data/plots/graph.png")
    plt.show(subgraph)
