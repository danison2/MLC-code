'''
Created on 29 Dec 2017

@author: DanyK
'''
import numpy as np


def getMembership(H):
    HT = np.transpose(H)
    M = HT / HT.sum(axis=1)[:, None] # rows are node probabilities, columns are communities
    return M