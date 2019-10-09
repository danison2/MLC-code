'''
Created on 20 Sep 2018

@author: DanyK
'''
import os
def createFolders():
# prepare the folders
        if os.path.exists('../F1/'):
            pass
        else:
            os.makedirs('../F1/')
        if os.path.exists('../Cond/'):
            pass
        else:
            os.makedirs('../Cond/')