# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 21:27:51 2022

@author: lenovo
"""

import pandas as pd

from train import pre
charge = [2,3]
database = pd.read_csv('database.csv')
fra = pd.read_csv('DB search psm.csv')
fra1 = fra['Fraction']
fraction = list(set(fra1.values.tolist()))
#fraction = [1,2,3] #fraction = [1,2,3,4]
for i in charge:
    if i == 2:
        ion = 'ionMobility-2'
    if i == 3:
        ion = 'ionMobility-3'
    
    for j in fraction:
        file  = pd.read_csv('DB search psm.csv')
        file_new = pre.shaixuan(file,'Z',i)
        file_new.reset_index(inplace=True,drop=True)
        file_new = pre.shaixuan(file_new,'Fraction',j)
        file_new.reset_index(inplace=True,drop=True)
        file_new = pre.high_msms(file_new)
        file_new.reset_index(inplace=True,drop=True)
        file_new = pre.tihuan(file_new,database,'sequence','Found By','sequence',ion,'ion_pre')
        file_new = pre.tihuan(file_new,database,'sequence','Found By','sequence','irt','irt_pre')
        rt = file_new[['RT','irt_pre']]
        rt = rt.sort_values(by="RT")
        rt.reset_index(inplace=True,drop=True)
        irt_rt = pre.step1(rt)
        chazhi = pre.step2(irt_rt,file_new)
        file_new = pre.tihuan(file_new,chazhi,'RT','Found By','rt','irt','irt')
        file_new.to_csv('DB search psm_charge{0}_f{1}.csv'.format(i,j),index=False)
        file_new = pd.read_csv('DB search psm_charge{0}_f{1}.csv'.format(i,j))
        p1 = pre.xianxing(file_new)
        x = file_new['ion']
        y_pre = p1[0]+p1[1]*x
        file_new['ionMobility']=y_pre
        file_new = pre.mass(file_new,i)[0]
        media = pre.mass(file_new,i)[1]
        file_new.to_csv('DB search psm_charge{0}_f{1}.csv'.format(i,j),index=False)


        file = pd.read_csv('peptide features.csv')
        file_new = pre.shaixuan(file,'z',i)
        file_new.reset_index(inplace=True,drop=True)
        file_new = pre.shaixuan(file_new,'Fraction',j)
        file_new.reset_index(inplace=True,drop=True)
        chazhi = pre.step2(irt_rt,file_new)
        file_new = pre.tihuan(file_new,chazhi,'RT','from Chimera','rt','irt','irt')
        file_new.to_csv('peptide features{0}_f{1}.csv'.format(i,j),index=False)
        file_new = pd.read_csv('peptide features{0}_f{1}.csv'.format(i,j))
        x = file_new['ion']
        y_pre = p1[0]+p1[1]*x
        file_new['ionMobility']=y_pre
        file_new['mass']=file_new['m/z']*i-i*1.00794+media


        file_new.to_csv('peptide features{0}_f{1}.csv'.format(i,j),index=False)
    