# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 19:41:20 2018

@author: DanyK
"""
import networkx as nx


def getConductance(G, communities):
    sum_cond = 0
    sum_len =0
    conductances = {}
    for L in communities:
        sum_len += len(L)
        cond = nx.conductance(G, L)
        conductances.update({str(L): cond})
        sum_cond += cond
    avg_cond = sum_cond / len(communities)
    avg_len = sum_len / len(communities)
    return avg_cond, avg_len

