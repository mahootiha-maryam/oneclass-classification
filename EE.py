# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 16:23:15 2021

@author: Asus
"""



import pandas as pd 

def isofor(location1,location2):
    
    lid=[]
    data=pd.read_csv(location1)
    data_columns=data.columns
    xtrain = data[data_columns[data_columns != 'class1']] 

    
    data1=pd.read_csv(location2)
    data1_columns=data1.columns
    xtest = data1[data1_columns[data1_columns != 'class1']] 
    
    for i,j in enumerate(data1['ids']):
        lid.append(j)
    
    from sklearn.covariance import EllipticEnvelope
    clf=EllipticEnvelope(contamination=0.01)
    clf.fit(xtrain)
    ypredict=clf.predict(xtest)
    rel=list(zip(lid,ypredict))
    pp=pd.DataFrame(data=rel,columns=['id','label'])
    pp.to_csv('label2.csv',index=False)

    
############################################################################
location1="train.csv"
location2="test.csv"

isofor(location1,location2)

