# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 14:05:40 2021

@author: lenovo
"""

import numpy as np
import pandas as pd
from pandas import DataFrame

def step1(file):
    data1 = file
    x = data1.iloc[:,0]
    y = data1.iloc[:,1]
    list1 = []
    list2 =[]
    irt_rt=[]
    k = (x[0]-1)
    for i in range(len(x)):
        if k<= x[i] <k+1:
            list1.append(y[i])
        elif k+1<= x[i] <k+2:
            ave = np.median(list1)
            list2.append([k,ave])
            list1 = []
            list1.append(y[i])
            k = k+1
        elif k+2<= x[i] <k+3:
            ave = np.median(list1)
            list2.append([k,ave])
            list1 = []
            list1.append(y[i])
            k = k+2
        elif k+3<= x[i] <k+4:
            ave = np.median(list1)
            list2.append([k,ave])
            list1 = []
            list1.append(y[i])
            k = k+3
        elif k+4<= x[i] <k+5:
            ave = np.median(list1)
            list2.append([k,ave])
            list1 = []
            list1.append(y[i])
            k = k+4
        elif k+5<= x[i] <k+6:
            ave = np.median(list1)
            list2.append([k,ave])
            list1 = []
            list1.append(y[i])
            k = k+5
        elif k+6<= x[i] <k+7:
            ave = np.median(list1)
            list2.append([k,ave])
            list1 = []
            list1.append(y[i])
            k = k+6
        elif k+7<= x[i] <k+8:
            ave = np.median(list1)
            list2.append([k,ave])
            list1 = []
            list1.append(y[i])
            k = k+7
        elif k+8<= x[i] <k+9:
            ave = np.median(list1)
            list2.append([k,ave])
            list1 = []
            list1.append(y[i])
            k = k+8
        elif k+9<= x[i] <k+10:
            ave = np.median(list1)
            list2.append([k,ave])
            list1 = []
            list1.append(y[i])
            k = k+9
        elif k+10<= x[i] <k+11:
            ave = np.median(list1)
            list2.append([k,ave])
            list1 = []
            list1.append(y[i])
            k = k+10
        elif k+11<= x[i] <k+12:
            ave = np.median(list1)
            list2.append([k,ave])
            list1 = []
            list1.append(y[i])
            k = k+11
        elif k+12<= x[i] <k+13:
            ave = np.median(list1)
            list2.append([k,ave])
            list1 = []
            list1.append(y[i])
            k = k+12
        elif k+13<= x[i] <k+14:
            ave = np.median(list1)
            list2.append([k,ave])
            list1 = []
            list1.append(y[i])
            k = k+13
    irt_rt.append([0,-50])
    for t in list2:
        irt_rt.append([t[0]+0.5,t[1]])
    irt_rt.append([60,250])
    irt_rt = DataFrame(irt_rt,columns = ['rt','irt'])
    irt_rt.dropna(how='any', axis=0, inplace=True)
    irt_rt.reset_index(inplace=True,drop=True)
    return irt_rt


def get_line(xn, yn):
    def line(x):
        index = -1
        for i in range(1, len(xn)):
            if x <= xn[i]:
                index = i-1
                break
            else:
                i += 1
         
        if index == -1:
            return -100
        result = (x-xn[index+1])*yn[index]/float((xn[index]-xn[index+1])) + (x-xn[index])*yn[index+1]/float((xn[index+1]-xn[index]))         
        return result
    return line

def step2(irt_rt,file):
    chazhi = []
    data1 = irt_rt
    data2 = file
    set11 = data1.iloc[:,0]
    set22 = data1.iloc[:,1] 
    set33 = data2['RT']
    xn = set11*100
    yn = set22
    lin = get_line(xn, yn)
    x = set33*100
    y = [lin(i) for i in x]
    for i in range(len(x)):
        chazhi.append([x[i]/100,y[i]])
    chazhi = DataFrame(chazhi,columns = ['rt','irt'])
    return chazhi

def xianxing(file):
    x = file['ion']
    y = file['ion_pre']
    z1 = np.polyfit(x, y, 1)
    p1 = np.poly1d(z1)
    y_pre = p1[0]+p1[1]*x
    file['ionMobility']=y_pre
    return p1
    
def shaixuan(file,name,i):
    df = file
    g = df.groupby([name])
    for pp,list1 in g:
        if pp == i:
            return list1

def high_msms(file):
    data = file
    test=[]
    list2=[]
    g = data.groupby(['Peptide'])
    for pp,list1 in g:
        index = list1['-10lgP'].idxmax()
        test.append(data.iloc[index])
        list2.append(index)
    test=DataFrame(test)
    return test      

def tihuan(file1,file2,factor1,tag1,factor2,tag2,name):
    df1 = file1
    x1 = df1.set_index([factor1])[tag1]
    df2 = file2
    x2 = df2.set_index([factor2])[tag2]
    x1.update(x2)
    df1[name] = x1.values
    return df1


def mass(file,charge):
    data = file
    x1 = data['m/z']
    x2 = data['Mass']
    x3 = charge*x1-1.00794*charge
    x4 = x2-x3
    media = sum(x4)/len(x4)
    x5 = x3 + media
    data['mass'] = x5.values
    #with open('mass.txt','a') as f:
        #print(np.median((x2-x5)/x5),file = f)
        #f.close()
    return data,media