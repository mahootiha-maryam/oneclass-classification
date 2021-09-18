# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 12:00:16 2021

@author: Asus
"""

import pandas as pd 



def svm(location1,location2):
    
    lid=[]
    data=pd.read_csv(location1)
    data_columns=data.columns
    xtrain = data[data_columns[data_columns != 'class1']] 

    
    data1=pd.read_csv(location2)
    data1_columns=data1.columns
    xtest = data1[data1_columns[data1_columns != 'class1']] 
    
    for i,j in enumerate(data1['ids']):
        lid.append(j)
    
    from sklearn import svm
    clf=svm.OneClassSVM(gamma='scale', nu=0.01)
    clf.fit(xtrain)
    ypredict=clf.predict(xtest)
    rel=list(zip(lid,ypredict))
    pp=pd.DataFrame(data=rel,columns=['id','label'])
    pp.to_csv('label.csv',index=False)
##############################################################################
def maketags(location2):

    e=pd.read_csv(location2)
    
    tags=[]
    idof=[] 
    
    for i,l in enumerate(e['class1']):
        if l=="negative":
            tags.append(1)
            idof.append(e.iloc[i,0])
        else:
            tags.append(-1)
            idof.append(e.iloc[i,0])
            
    rel=list(zip(idof,tags))
    pp=pd.DataFrame(data=rel,columns=['id','tag'])
    pp.to_csv('labeloftest.csv',index=False)
    


##############################################################################

location1="train.csv"
location2="test.csv"

svm(location1,location2)


maketags(location2)


