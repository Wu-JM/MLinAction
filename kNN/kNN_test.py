# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 21:47:54 2020

@author: WU Jiaming
"""

from numpy import *
import operator

def createDataSet():  # create dataset and labels
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet  
    # tile() to repeat inX into a same dimension set as the existing dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMAt.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()  
    # .argsort() gets the indicies of the sorted elements
    classCount = {}  # dictionary
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1  
        # .get() return the value of the key (default 0)
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
    
        