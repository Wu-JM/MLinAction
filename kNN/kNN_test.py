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

