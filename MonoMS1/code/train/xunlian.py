# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 16:00:27 2022

@author: lenovo
"""

import numpy as np
import pandas as pd


from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.metrics import classification_report
from mpl_toolkits.mplot3d import Axes3D

def train(file1,file2,output,tar):
    sum1=0
    sum2=0
    test=[]
    list2=[]
    data = file1
    x1 = data['mass'] 
    x2 = data['ion'] 
    x3 = data['irt']
    x4 = data['detect'] 
    a1=1
    a2=1
    a3=1
    a4=1
    data['h'] = a3*x3*x3+a1*x1*x1+a2*x2*x2+a4*x4*x4
    for t in range(25):
        print(t)
        with open('记录.txt', 'a') as f:
            f.write(str(t)+' ')
            f.close()
        sum1=0
        sum2=0
        test=[]
        list2=[]
        g = data.groupby(['p1','fraction','charge'])
        for pp,list1 in g:
    
            min_h = min(list1['h'])
            index = list1['h'].idxmin()
            if data.iloc[index]['p1'] == data.iloc[index]['p2']:
                sum1 = sum1+1
                list2.append(index)
                test.append([data.iloc[index,2]*data.iloc[index,2]*a1,data.iloc[index,3]*data.iloc[index,3]*a2,data.iloc[index,4]*data.iloc[index,4]*a3,data.iloc[index,5]*data.iloc[index,5]*a4,0])
                list1 = list1.drop([index],axis=0)
                if len(list1)>0:
                    index_1 = list1['h'].idxmin()
                    test.append([data.iloc[index_1,2]*data.iloc[index_1,2]*a1,data.iloc[index_1,3]*data.iloc[index_1,3]*a2,data.iloc[index_1,4]*data.iloc[index_1,4]*a3,data.iloc[index_1,5]*data.iloc[index_1,5]*a4,1])
        
            else:
                sum2 = sum2+1
                test.append([data.iloc[index,2]*data.iloc[index,2]*a1,data.iloc[index,3]*data.iloc[index,3]*a2,data.iloc[index,4]*data.iloc[index,4]*a3,data.iloc[index,5]*data.iloc[index,5]*a4,1])
     
        print(sum1,sum2)
        with open('记录.txt', 'a') as f:
            f.write(str(sum1)+','+str(sum2))
            f.close()

        test_new1= DataFrame(test)
        #test_new1.to_csv('xunlian.csv',index=None,header=None)
    
        #test_new2 = np.genfromtxt('xunlian.csv',delimiter=',')
        x_data = test_new1.iloc[:,:-1]
        y_data = test_new1.iloc[:,-1]
        logistic = linear_model.LogisticRegression(solver='liblinear')
        logistic.fit(x_data,y_data)        
        print(logistic.intercept_,logistic.coef_)
        predictions = logistic.predict(x_data)
        print(logistic.score(x_data,y_data, sample_weight=None))
        with open('记录.txt', 'a') as f:
            f.write(str(logistic.intercept_)+str(logistic.coef_))
            f.write('\n')
            f.close()
        a1=logistic.coef_[0][0]*a1
        a2=logistic.coef_[0][1]*a2
        a3=logistic.coef_[0][2]*a3
        a4=logistic.coef_[0][3]*a4
        data['h'] = a3*x3*x3+a1*x1*x1+a2*x2*x2+a4*x4*x4
        print(x_data)
        print(a1,a2,a3,a4)
        with open('weight.txt', 'a') as f:
            f.write(str(a1)+str(a2)+str(a3)+str(a4))
            f.write('\n')
            f.close()
 
    data = file2
    x1 = data['mass'] 
    x2 = data['ion'] 
    x3 = data['irt']
    x4 = data['detect'] 
    data['h'] = a3*x3*x3+a1*x1*x1+a2*x2*x2+a4*x4*x4
    try1 = [0]
    for t in try1:
        print(t)
        sum1=0
        sum2=0
        test=[]
        test1=[]
        list2=[]
        g = data.groupby(['p1','fraction','charge'])
        for pp,list1 in g:
    
            min_h = min(list1['h'])
            index = list1['h'].idxmin()
            list2.append(index)
            list3 = list1.drop([index],axis=0)
            if len(list3)>0:
                index_1 = list1['h'].idxmin()
                min_h2 = min(list3['h'])
                delta = min_h2-min_h
            
            else:
                delta = 0
            test.append([data.iloc[index]['p1'],data.iloc[index]['p2'],min_h,delta,len(list1),data.iloc[index]['fraction'],data.iloc[index]['charge']])
        
        test_new1= DataFrame(test)
        if tar == 1:
            test_new1.to_csv(output,mode='a',index=None,header=['p1','p2','min_h','delta','data','fraction','charge'])
        elif tar == -1:
            test_new1.to_csv(output,mode='a',index=None,header=None)

    