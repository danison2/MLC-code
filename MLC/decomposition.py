'''
Created on 29 Dec 2017

@author: DanyK
'''
from sklearn.decomposition import NMF


def decomposition(A, nb):
    model = NMF(n_components=nb, init='random', random_state=0)   
    W = model.fit_transform(A);
    H = model.components_;
    return W, H