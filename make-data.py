# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 13:46:51 2021

@author: Asus
"""

import pandas as pd
location="dataset.csv"
e=pd.read_csv(location)

ids=[]
mcg=[]
gvh=[]
alm=[]
mit=[]
erl=[]
pox=[]
vac=[]
nuc=[]
class1=[]

count=0

for i,j in enumerate(e['class1']):
    ids.append(count)
    count+=1
    mcg.append(e.iloc[i,0])
    gvh.append(e.iloc[i,1])
    alm.append(e.iloc[i,2])
    mit.append(e.iloc[i,3])
    erl.append(e.iloc[i,4])
    pox.append(e.iloc[i,5])
    vac.append(e.iloc[i,6])
    nuc.append(e.iloc[i,7])
    class1.append(e.iloc[i,8])
    
rel=list(zip(ids,mcg,gvh,alm,mit,erl,pox,vac,nuc,class1))
pp=pd.DataFrame(data=rel,columns=['ids','mcg','gvh','alm','mit','erl','pox','vac','nuc','class1'] )
pp.to_csv('datasetnew.csv',index=False) 