# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 10:36:00 2022

@author: lenovo
"""
import numpy as np
import pandas as pd
from pandas import DataFrame

from train import protein
from train import scorefinal

from train import min_h
from train import protein_score
from train import score
charge = [2,3]
for i in charge:
    df1 = pd.read_csv('result_charge{0}.csv'.format(i))
    df1['k'] = np.nan
    database = pd.read_csv('database.csv')
    df1 = min_h.tihuan(df1,database,['p2'],'k',['sequence'],'protein_group','protein_group')
    df1 = min_h.tihuan(df1,database,['p2'],'k',['sequence'],'k','t')
    df2 = pd.read_csv('peptide features.csv')
    df1 = min_h.tihuan(df1,df2,['p1','fraction','charge'],'k',['Feature Id','Fraction','z'],'sequence','DB peptide')

    df1 = min_h.match(df1)
    min_a = score.choose_min_h(df1,0.99)
    min_b = score.choose_delta(df1,min_a,0.90)
    '''with open('min_a b.txt','a') as f:
        print(min_a,min_b,i,file=f)
    f.close()'''
    if i == 2:
        d2 = score.choose(df1,min_a,min_b)
    if i == 3:
        d3 = score.choose(df1,min_a,min_b)
df_all = pd.concat([d2,d3],axis=0)
df_all.to_csv('test_result_all.csv',index=None)
protein_score.chuli('test_result_all.csv','database.csv')

file0 = pd.read_csv('test_result_all.csv')
base = pd.read_csv('database.csv')
file0 = protein.final(file0,base)

file1 = file0.sort_values(by="score")
file1.reset_index(inplace=True,drop=True)
min_c = scorefinal.choose_score(file1,0.99,'score')
file2 = file1[file1['score'] >= min_c]
file2n = file2[['p1','p2','charge','fraction','DB peptide']]
file2n = file2n.rename(columns={'p1': 'Feature Id', 'p2': 'Peptide'})
file2n.to_csv('0.99-result_final.csv',index=None)

min_c = scorefinal.choose_score(file1,0.95,'score')
file3 = file1[file1['score'] >= min_c]
file3n = file3[['p1','p2','charge','fraction','DB peptide']]
file3n = file3n.rename(columns={'p1': 'Feature Id', 'p2': 'Peptide'})
file3n.to_csv('0.95-result_final.csv',index=None)
