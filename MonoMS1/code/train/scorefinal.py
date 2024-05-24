# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:02:42 2022

@author: lenovo
"""
import numpy as np
import pandas as pd
from pandas import DataFrame
def choose_score(file,pre,name):
    list_score=[]
    data2 = file
    data2 = data2[['p2','t',name]]
    data2 = data2.sort_values(by=[name])
    data2.drop_duplicates(subset='p2', keep='first', inplace=True, ignore_index=True)
    wrong=0
    for i in range(len(data2)):
        print(i)
        right = 1
        wrong = 0
        c=data2.iloc[i][name]
        data3=data2[data2[name] >= c]
        g = data3.groupby(['t'])
        for p1,list1 in g:
            if p1 == 0:
                right=len(list1)
            elif p1 == 1:
                wrong=len(list1)
        #if right2/right1>0.9:
        if right/(right+wrong) >= pre:
            list_score.append(c)
    min_c = min(list_score)
    return min_c

