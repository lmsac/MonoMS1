# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:42:08 2022

@author: lenovo
"""
import numpy as np
import pandas as pd
from pandas import DataFrame
def tihuan(file1,file2,factor1,tag1,factor2,tag2,name):
    df1 = file1
    x1 = df1.set_index(factor1)[tag1]
    df2 = file2
    x2 = df2.set_index(factor2)[tag2]
    x1.update(x2)
    df1[name] = x1.values
    return df1

def match(file):
    sum11=0
    sum22=0
    list1=[]
    data1 = file
    for i in range(len(data1)):
        print(i)
        if str(data1.iloc[i]['DB peptide']).find(str(data1.iloc[i]['p2']))!=-1:
            list1.append(1)
            sum11=sum11+1
        if type(data1.iloc[i]['DB peptide']) == str:
            sum22=sum22+1
            if str(data1.iloc[i]['DB peptide']).find(str(data1.iloc[i]['p2']))==-1:
                list1.append(-1)
        if type(data1.iloc[i]['DB peptide']) != str:
            list1.append(0)
    data1['target']=list1
    print(sum11,sum22)
    return data1

