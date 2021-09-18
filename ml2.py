# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 11:49:33 2021

@author: Asus
"""
import pandas as pd
from sklearn.model_selection import train_test_split

location="negative.csv"
e=pd.read_csv(location)

location1="positive.csv"
e1=pd.read_csv(location1)



train, test = train_test_split(e, test_size=0.20)

frames=[e1,test]
testdata=pd.concat(frames)

pp=pd.DataFrame(data=train )
pp.to_csv('train.csv',index=False) 


pp1=pd.DataFrame(data=testdata )
pp1.to_csv('test.csv',index=False) 
