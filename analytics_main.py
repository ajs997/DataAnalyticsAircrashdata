#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 11:45:07 2017


"""

#importing pandas, numpy and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime


"""
Dataset loading section
"""

#Function for Data ingestion stage using read_csv
def readData():
    try:
        dataset=pd.read_csv('./data/Airplane_Crashes_and_Fatalities_Since_1908.csv') #storing the data in a DataFrame
        print("\nDataset loaded successfully.")
        return dataset
    except FileNotFoundError:
        print("\nThe file does not exist.")
    
    #print(crashds.head(2))
  
    
"""
Data cleaning section
"""

#Function for Data cleaning stage
def cleanData(dataset):
    print("\nCleaning data now...")
    del dataset['Summary']  #Summary column is dropped
    
    #removing invalid values
    ds1=dataset.isnull().any()
#    print(ds1)
    if True in ds1.values:  #if there are invalid value drop them
        print("\nThere are invalid values in the dataset. Deleting invalid values...")
        dataset=dataset.dropna()
        print("\nInvalid values have been dropped.\n")
#        ds1=dataset.isnull().any()
#        print(ds1)
    else:   #if there are no invalid values
        print("\nThere are no invalid values in the dataset.\n")
        
    #changing the format and type of values in Date column
    dataset['Date']=pd.to_datetime(dataset['Date'],format="%m/%d/%Y")
    
    print("\nDataset has been cleaned.")
    #returning dataset
    return dataset

#Function to check the validity of the Dataset
def dataIsValid(dataset):
    print("\nChecking for the validity of the dataset....")
    
    #filters the Aboard, Fatalities and Ground column to find invalid values
    tester_1=dataset['Aboard']<0
    tester_2=dataset['Fatalities']<0
    tester_3=dataset['Ground']<0
    
    #returns False if it has invalid values else returns true
    if True in tester_1 | True in tester_2 | True in tester_3:
        return False
    else:
        return True


"""
Data Slicing Section
"""

#Function to return columns of the dataset
def getColumns(dataset,col,rowStart,rowEnd):
    print("\nIn getColumns method....  ")
    return dataset[col].iloc[rowStart:rowEnd]

#Function to return dataset filtered by dates
def filterByDates(dataset,frm,to):
    print("\nIn filterByDate method....  ")
    filter_1=dataset['Date']>frm
    filter_2=dataset['Date']<to
    return dataset[filter_1 & filter_2]

#Function to return dataset filtered by Operator
def filterByOperator(dataset,operator):
    print("\nIn filterByOperator method....  ")
    filter_op=dataset['Operator'].str.contains(operator)
    return dataset[filter_op]

#Function to return dataset filtered by Location
def filterByLocation(dataset,location):
    print("\nIn filterByLocation method....  ")
    filter_loc=dataset['Location'].str.contains(location)
    return dataset[filter_loc]

#Function to return dataset filtered by Aboard, Fatalities, Ground
def filterByAFG(dataset,col,num):
    print("\nIn filterByAFG... ")
    filter_afg=dataset[col]>num
    return dataset[filter_afg]



"""
Descriptive Statistics Section
"""
#Function to get dataset details
def desDataset(dataset,info):
    print("\nIn desDataset method....  ")
    if info=="shape":
        return dataset.shape

#Function to describe the columns
def desColumns(dataset,col):
    print("\nIn desColumns method....  ")
    desc=dataset[col].describe()
    return desc

#Function to return sum, mode, median and correlation
def retStats(dataset,col):
    print("\nIn retStats method....  ")
    return {'total':dataset[col].sum(),'median':dataset[col].median(),'mode':dataset[col].mode()}


"""
Data Transformation Section
"""
#Function to group by sum
def groupBySum(dataset,col1,col2):
    print("\nIn groupBySum method... ")
    return dataset[[col1,col2]].groupby(col1,as_index=False).sum()



"""
Plotting Graph Section
"""
#Function to plot the graph
def plotGraph(dataset,rowStart,rowEnd,col1,col2,type_graph):
    print("\nIn plotGraph method... ")
    dataset[rowStart:rowEnd].plot(x=col1,y=col2,figsize=(15,10),grid=True,kind=type_graph)
    

#Function for displaying data regarding the data set
def defDataset(dataset):
    print("\nIn defDataset method....  ")
    #print(dataset.head())
    #print(dataset.tail())
    shape=dataset.shape
    columns=dataset.columns
    print("The Indices of the dataset: ",columns,"\nThe shape of dataset: ",shape)
    #dataset.plot(x='Operator',y='Fatalities',figsize=(15,10),kind='bar')


#Function to return column and rows of the dataset
def retData(dataset,cols,rows=0):   #cols will be a list of columns selected
    print("\nIn retData method....  ")
    columns=dataset.columns
    for x in columns:
        print(dataset[x])


#ds=readData()
#ds=cleanData(ds)
##print(ds.head(10))
#desColumns(ds,'Aboard')
