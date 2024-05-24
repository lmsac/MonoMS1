# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:44:15 2022

@author: lenovo
"""

import numpy as np
import pandas as pd
from pandas import DataFrame
def pretreatment(file,base,name,fraction,charge,outputfile,t):
    data1 = file
    data2 = base
    list1 = []
    yuchuli=[]
    sum1=0
    for i in range(len(data1)):
        print(i)
        a = data1.iloc[i]['mass']
        user_requried = data2['mass'].map(lambda x : 0.999985*a<x<1.000015*a)
        some = data2[user_requried]
    
        if len(some)>0:
            sum1=sum1+1
            for j in range(len(some)):
            
                b=some.values[j][1]-data1.iloc[i]['mass']
                c=some.values[j][2]-data1.iloc[i]['ionMobility']
                d=some.values[j][3]-data1.iloc[i]['irt']
                e=some.values[j][4]
                yuchuli.append([data1.iloc[i][name],some.values[j][0],float(b),float(c),float(d),float(e),int(fraction),int(charge)])
        else:
            list1.append(i)
    print(sum1,list1,len(list1))
    if t == 1:
        df1 = DataFrame(yuchuli,columns=["p1","p2","mass","ion","irt","detect","fraction","charge"])
        df1.to_csv(outputfile, mode='a', index=False)
    elif t == -1:
        df1 = DataFrame(yuchuli)
        df1.to_csv(outputfile, mode='a', index=False,header=None)
    return df1



def normalization(file,new_file):
    df1 = DataFrame(file)
    x1 = df1[:]['mass']
    x2 = df1[:]['ion']
    x3 = df1[:]['irt']
    x4 = df1[:]['detect']
    y1 = min(abs(x1))
    y2 = min(abs(x2))
    y3 = min(abs(x3))
    z1 = max(abs(x1))
    z2 = max(abs(x2))
    z3 = max(abs(x3))
    print(y1,y2,y3,z1,z2,z3)
    x1.update((abs(x1)-y1)/(z1-y1))
    x2.update((abs(x2)-y2)/(z2-y2))
    x3.update((abs(x3)-y3)/(z3-y3))

    df1['mass'] = x1.values
    df1['ion'] = x2.values
    df1['irt'] = x3.values
    df1['detect'] = x4.values
    #df1.to_csv(new_file,index=None) 
    return df1