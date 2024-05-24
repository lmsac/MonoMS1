# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:57:02 2022

@author: lenovo
"""
import numpy as np
import pandas as pd
from pandas import DataFrame
import math
def choose_min_h(file,pre):
    list_minh=[]
    data2 = file
    data2 = data2.sort_values(by=['min_h'])
    h = data2.groupby(['target'])
    for p2,list2 in h:
        if p2 == 1 :
            msms_all=len(list2)
            list2.reset_index(inplace=True,drop=True)
            index = int(msms_all * pre)
            min_a = list2.iloc[index]['min_h']
    return min_a

def choose_delta(file,min_a,pre):
    list_delta=[]
    data2 = file
    data2=data2[data2['min_h'] <= min_a]
    data2 = data2.sort_values(by=['delta'])
    data2.reset_index(inplace=True,drop=True)
    ks1=0
    for ks in [0,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3]:
        data3 = data2[data2['delta'] >= ks]
        g = data3.groupby(['target'])
        for p1,list1 in g:
            if p1 == 1:
                right=len(list1)
            if p1 == -1:
                wrong=len(list1)
        if right/(right+wrong) <= pre:
            ks1 = ks
        
    wrong = 1
    right = 0
    i = 0    
    while right/(right+wrong) <= pre:
        print(i)
        b=data2.iloc[i]['delta']
        if b >= ks1:
            data3=data2[i:]
            g = data3.groupby(['target'])
            for p1,list1 in g:
                if p1 == 1:
                    right=len(list1)
                if p1 == -1:
                    wrong=len(list1)
            list_delta.append(b)
        i = i+1
    min_b = max(list_delta)
    return min_b

def choose(file,min_a,min_b):
    data2 = file
    data3=data2[data2['min_h'] <= min_a]
    data3=data3[data3['delta'] >= min_b]
    return data3
