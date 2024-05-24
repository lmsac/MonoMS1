# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:15:17 2022

@author: lenovo
"""

import numpy as np
import pandas as pd
import csv

from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.metrics import classification_report
from mpl_toolkits.mplot3d import Axes3D

from train import yuchuli
from train import xunlian
fra = pd.read_csv('DB search psm.csv')
fra1 = fra['Fraction']
fraction = list(set(fra1.values.tolist()))
#fraction = [1,2,3] #fraction = [1,2,3,4]
for fra in fraction:
    if fra == 1:
        ks = 1
    else:
        ks = -1
    file = pd.read_csv('DB search psm_charge2_f{0}.csv'.format(fra))
    base = pd.read_csv('database.csv')
    base = pd.DataFrame(base,columns = ['sequence','mass','ionMobility-2','irt','detect'])
    yuchuli.pretreatment(file,base,'sequence',fra,2,'DBmsms_charge2.csv',ks)
    file = pd.read_csv('peptide features2_f{0}.csv'.format(fra))
    yuchuli.pretreatment(file,base,'Feature Id',fra,2,'ms1_charge2.csv',ks)
    file = pd.read_csv('DB search psm_charge3_f{0}.csv'.format(fra))
    base = pd.read_csv('database.csv')
    base = pd.DataFrame(base,columns = ['sequence','mass','ionMobility-3','irt','detect'])
    yuchuli.pretreatment(file,base,'sequence',fra,3,'DBmsms_charge3.csv',ks)
    file = pd.read_csv('peptide features3_f{0}.csv'.format(fra))
    yuchuli.pretreatment(file,base,'Feature Id',fra,3,'ms1_charge3.csv',ks)

file = pd.read_csv('DBmsms_charge2.csv')
msmstrain_2 = yuchuli.normalization(file,'DBmsms2.csv')
file = pd.read_csv('ms1_charge2.csv')
ms1train_2 = yuchuli.normalization(file,'2ms1.csv')
file = pd.read_csv('DBmsms_charge3.csv')
msmstrain_3 = yuchuli.normalization(file,'DBmsms3.csv')
file = pd.read_csv('ms1_charge3.csv')
ms1train_3 = yuchuli.normalization(file,'3ms1.csv')
xunlian.train(msmstrain_2,ms1train_2,'result_charge2.csv',1)
xunlian.train(msmstrain_3,ms1train_3,'result_charge3.csv',1)