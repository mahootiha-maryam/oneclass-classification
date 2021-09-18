# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 11:14:34 2021

@author: Asus
"""
import pandas as pd
location="datasetnew.csv"
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

for sh1,sh2 in enumerate(e['class1']):
    if sh2=="positive":
        ids.append(e.iloc[sh1,0])
        mcg.append(e.iloc[sh1,1])
        gvh.append(e.iloc[sh1,2])
        alm.append(e.iloc[sh1,3])
        mit.append(e.iloc[sh1,4])
        erl.append(e.iloc[sh1,5])
        pox.append(e.iloc[sh1,6])
        vac.append(e.iloc[sh1,7])
        nuc.append(e.iloc[sh1,8])
        class1.append(e.iloc[sh1,9])
        
        
rel=list(zip(ids,mcg,gvh,alm,mit,erl,pox,vac,nuc,class1))
pp=pd.DataFrame(data=rel,columns=['ids','mcg','gvh','alm','mit','erl','pox','vac','nuc','class1'] )
pp.to_csv('positive.csv',index=False) 
###################################################################################
location="datasetnew.csv"
e=pd.read_csv(location)
mcg=[]
gvh=[]
alm=[]
mit=[]
erl=[]
pox=[]
vac=[]
nuc=[]
class1=[]

for sh1,sh2 in enumerate(e['class1']):
    if sh2=="negative":
        ids.append(e.iloc[sh1,0])
        mcg.append(e.iloc[sh1,1])
        gvh.append(e.iloc[sh1,2])
        alm.append(e.iloc[sh1,3])
        mit.append(e.iloc[sh1,4])
        erl.append(e.iloc[sh1,5])
        pox.append(e.iloc[sh1,6])
        vac.append(e.iloc[sh1,7])
        nuc.append(e.iloc[sh1,8])
        class1.append(e.iloc[sh1,9])
        
rel=list(zip(ids,mcg,gvh,alm,mit,erl,pox,vac,nuc,class1))
pp=pd.DataFrame(data=rel,columns=['ids','mcg','gvh','alm','mit','erl','pox','vac','nuc','class1'] )
pp.to_csv('negative.csv',index=False) 
#####################################################################################

from sklearn.model_selection import train_test_split
location="negative.csv"
e=pd.read_csv(location)

train, test = train_test_split(e, test_size=0.25)


print(len(test))