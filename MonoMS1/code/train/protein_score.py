# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 18:33:59 2022

@author: lenovo
"""

import csv
import pandas as pd
import numpy as np
from pandas import DataFrame
from collections import Counter
test=[]
test1 = []
test2 = []
def count_ku(file1):
    t=[]
    data5 = pd.read_csv(file1)
    M=[]
    from collections import Counter
    for i in range(len(data5)):
        list1 = data5.iloc[i]['protein_group'].split(";")
        list1 = [a for a in list1 if a != '']
        for s in range(len(list1)) :
            M.append(list1[s])
    #print(M)
    recounted = Counter(M) #M为待统计数组
    dict(recounted) #转换为字典
    for key,value in recounted.items():
        t.append([key,value])
    t = DataFrame(t,columns=['protein_group','count'])    
    return t

def count_pep1(file2):
    t=[]
    data = file2
    M=[]
    from collections import Counter
    for i in range(len(data)):
        list1 = data.iloc[i]['protein_group'].split(";")
        list1 = [a for a in list1 if a != '']
        if len(list1) == 1 :
            M.append(list1[0])
    #print(M)
    recounted = Counter(M) #M为待统计数组
    df1 = dict(recounted) #转换为字典
    return df1

def count_pep2(file2):
    t=[]
    data7 = file2
    M=[]
    from collections import Counter
    for i in range(len(data7)):
        list1 = data7.iloc[i]['protein_new'].split(";")
        list1 = [a for a in list1 if a != '']
        if len(list1) == 1 :
            M.append(list1[0])
    #print(M)
    recounted = Counter(M) #M为待统计数组
    dict(recounted) #转换为字典
    for key,value in recounted.items():
        t.append([key,value])
    t = DataFrame(t,columns=['protein_group','count'])    
    return t

def protein(file1,ku):
    pep=[]
    test=[]
    test1 = []
    test2 = []
    data = pd.read_csv(file1)
    dic = ku
    all1=[]
    #with open('3-0705.txt', 'w') as f:
    for i in range(len(data)):
        pro = data.iloc[i]['protein_group']
        list1 = pro.split(';')
        list1 = [a for a in list1 if a != '']
        if len(list1)>1:
            slis=[]
            for s in range(len(list1)):
                if list1[s] in dic: 
                    slis.append(list1[s])
            if len(slis) == 1:
                pep.append([data.iloc[i]['p1'],data.iloc[i]['p2'],data.iloc[i]['fraction'],slis[0]])
                #print(data.iloc[i]['p1'],data.iloc[i]['p2'],slis[0],file=f)
            if len(slis) >1:
                #print(len(slis),data.iloc[i]['p1'],data.iloc[i]['p2'])
                k = []
                v = []
                for a in slis:
                    k.append(a)
                    v.append(dic[a])
                px = dict(zip(k,v))
                #print(px)
                protein = sorted(px.items(),key=lambda x:(x[1],x[0]),reverse=True)
                pep.append([data.iloc[i]['p1'],data.iloc[i]['p2'],data.iloc[i]['fraction'],protein[0][0]])
                #print(data.iloc[i]['p1'],data.iloc[i]['p2'],protein[0][0],file=f)
            if len(slis) == 0:
                all1 = all1+list1
    
    recounted = Counter(all1) #M为待统计数组
    dict(recounted)    
    for d in range(len(data)):
        pro = data.iloc[d]['protein_group']
        list1 = pro.split(';')
        list1 = [a for a in list1 if a != '']
        if len(list1)>1:
            slis = []
            for s in range(len(list1)):
                
                if list1[s] in dic: 
                    slis.append(list1[s])
            if len(slis) == 0:
                #print(list1)
                k = []
                v = []
                for a in list1:
                    k.append(a)
                    v.append(recounted[a])
                px = dict(zip(k,v))
                #print(px)
                px.pop('',None)
                px.pop('',None)
                protein = sorted(px.items(),key=lambda x:(x[1],x[0]),reverse=True)
                pep.append([data.iloc[d]['p1'],data.iloc[d]['p2'],data.iloc[d]['fraction'],protein[0][0]])
                #print(data.iloc[d]['p1'],data.iloc[d]['p2'],protein[0][0],file=f)
    pep = DataFrame(pep,columns=["p1",'p2','fraction','protein_group'])
    return pep

def chuli(file_name,base):
    file = pd.read_csv(file_name)
    ku = count_pep1(file)
    pep = protein(file_name,ku)
    shuju = pd.read_csv(file_name)
    x1 = shuju.set_index(['p1','p2','fraction'])['protein_group']
    x2 = pep.set_index(['p1','p2','fraction'])['protein_group']
    x1.update(x2)
    shuju['protein_new'] = x1.values
    shuju.to_csv(file_name,index=None)
    database = count_ku(base)
    shuju = pd.read_csv(file_name)
    x1 = shuju.set_index(['protein_new'])['k']
    x2 = database.set_index(['protein_group'])['count']
    x1.update(x2)
    shuju['ku_N'] = x1.values
    shuju.to_csv(file_name,index=None)

    shuju = pd.read_csv(file_name)
    shuju1 = shuju.drop_duplicates(subset=['p2','protein_new'],keep='first')
    count_pep = count_pep2(shuju1)
    x1 = shuju.set_index(['protein_new'])['k']
    x2 = count_pep.set_index(['protein_group'])['count']

    x1.update(x2)
    shuju['pep_K'] = x1.values
    shuju.to_csv(file_name,index=None)
