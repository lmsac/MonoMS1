# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:48:03 2022

@author: lenovo
"""

import csv
import math
import pandas as pd
from pandas import DataFrame
import numpy as np
from scipy import stats
def final(file,base):
    test=[]
    data = file
    g = data.groupby(['t'])
    for pp,list1 in g:
        if pp == 1:
            list1 = list1.drop_duplicates(subset='p2', keep="first", inplace=False, ignore_index=False)
            long = len(list1)
            print(long)
    data_base = base
    ba = data_base.groupby(['k'])
    for p,q in ba:
        if p == 1:
            base_len = len(q)
    for i in range(len(data)):
        print(i)
        if data.iloc[i]['ku_N'] != data.iloc[i]['ku_N']:
            score = 0
        elif data.iloc[i]['ku_N'] == data.iloc[i]['ku_N']:
            n = data.iloc[i]['ku_N']
            p = long/base_len
            n = int(n)
            p = float(p)
            t = data.iloc[i]['pep_K']
            t = int(t)
            y = []
            for j in range(t+1,n+1):
                k = stats.binom.pmf(j,n,p)
                y.append(k)
            sum1 = sum(y)
            if n<5:
                score = 0
            elif sum1 == 0 and n>=5:
                score = 50
            else:
                score = -math.log(sum1)
        test.append(score)
        #with open('log1-result_ecoli-1.txt', 'a') as f:
            #print(i,data.iloc[i]['ku_N'],data.iloc[i]['pep_K'],score,file=f)

    test = DataFrame(test,columns = ['score'])
    file['score'] = test
    test_n = file['score']
    kk = file['pep_K']
    log_kk = np.log10(kk)
    #file['score_f'] = log_kk*test_n
    return file
