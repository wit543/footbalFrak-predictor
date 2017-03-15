#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 23:39:22 2017

@author: Nattapat
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import numpy as np
from numpy import random
from time import time
import csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB



# Read Player_Attributes.csv into dataframe, add column for ....
f = open('datasets/Player_Attributes.csv')
player_attributes = pd.read_csv(f)


# read match
f = open('datasets/Match.csv')
match = pd.read_csv(f)
match_result = []
for i in range(0,len(match)):
    goal = match.ix[i]['home_team_goal'] - match.ix[i]['away_team_goal']

    if (goal<0):
        match_result.append("lose")
    elif (goal==0):
        match_result.append("win")
    else:
        match_result.append("win")

match['className'] = match_result
# read team attributes
f = open('datasets/Team_Attributes.csv')
teams = pd.read_csv(f)

array = []

#for i in range(0,len(match)):
#    for j in range(0,len(teams)):
#        if match.ix[i]['home_team_api_id']==teams.ix[j]['team_api_id']:
##            print(match.ix[i]['home_team_api_id'],teams.ix[j]['team_api_id'])
#            match.ix[i]['home_buildUpPlaySpeed'] = teams.ix[j]['buildUpPlaySpeed']
#matchex  = match.merge(teams, on='country')
#
#


numitems = len(match)
percenttrain = 0.9
numtrain = int(numitems*percenttrain)
numtest = numitems - numtrain
dataTrain = match[0:numtrain]
dataTest = match[numtrain:numitems]
print ('Training set', numtrain, 'items')
print ('Test set', numtest, 'items')            
            
            
# Predict position from one or more of minutes, shots, passes, tackles, saves.
# Try different features. What's the highest accuracy you can get?
features = ['match_api_id','home_team_api_id','away_team_api_id']
featurevals = dataTrain[features]
labels = dataTrain['className']
nb = GaussianNB()
nb.fit(featurevals,labels)
predictions = nb.predict(dataTest[features])
# Calculate accuracy
numtrain = len(dataTrain)
numtest = len(dataTest)

correct = 0
for i in range(0,numtest):
#    print 'Predicted:', predictions[i], ' Actual:', playersTest.ix[numtrain+i]['position']
    if predictions[i] == dataTest.ix[numtrain+i]['className']: 
        correct +=1
print ('Percent correct:', float(correct)/float(numtest))

