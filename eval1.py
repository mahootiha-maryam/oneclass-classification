# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 16:15:57 2021

@author: Asus
"""


import pandas as pd
location="labeloftest.csv"
e=pd.read_csv(location)

location1="label1.csv"
e1=pd.read_csv(location1)

truepositive=[]
falsengative=[]
falsepositive=[]
truenegative=[]

precision=0
recall=0
f=0
s=0


for x in enumerate(e['id']):
    s+=1
       
for i,j in enumerate(e['id']):
    for m in range(i,s):
        
        if j== e1.iloc[m,0]:
            if e.iloc[i,1]==1 and e1.iloc[m,1]==1:
                truepositive.append(j)
            if e.iloc[i,1]==1 and e1.iloc[m,1]==-1:
                falsengative.append(j)
            if e.iloc[i,1]==-1 and e1.iloc[m,1]==-1:
                truenegative.append(j)
            if e.iloc[i,1]==-1 and e1.iloc[m,1]==1: 
                falsepositive.append(j)

tp=len(truepositive)
fn=len(falsengative)
fp=len(falsepositive)
tn=len(truenegative)


NPV=(tn/(tn+fn))
specificity=(tn/(tn+fp))
precision=(tp/(tp+fp))
recall=(tp/(tp+fn))
f=2*((precision*recall)/(precision+recall))


print("the precision/PPv is:",precision)
print("the NPV is:", NPV)
print("the sensitivity is:",recall)
print("the specificity is:",specificity)
print("the f score is:",f)

