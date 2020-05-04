from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import csv
import time
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
import seaborn as sns
import scikitplot as skplt 
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB


def fengr():
	#import the dataset
	df = pd.read_csv('D:/University/MS/Thesis/Current/W16/2-data/test_train_split/shuffled/shuffled_train_subset.csv', low_memory=False)
	df2= pd.read_csv('D:/University/MS/Thesis/Current/W16/2-data/test_train_split/shuffled/shuffled_test_subset.csv', low_memory=False)


	del df['from_address']
	del df2['from_address']

	del df['to_address']
	del df2['to_address']

	del df['block_timestamp']
	del df2['block_timestamp']

	del df['block_number']
	del df2['block_number']

	# Converting string labels into numbers.
	le = preprocessing.LabelEncoder()
	df['label']=le.fit_transform( df['label'])
	df2['label']=le.fit_transform( df2['label'])
	#print(df)
	le_name_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
	print(le_name_mapping)
	
	#saving training labels as dataframe
	X = df[df.columns[:-1]]
	y = df['label']	

	#dropping label column from test data
	testData = df2[df2.columns[:-1]].values
	y_test = df2['label']
	
	#apply SelectKBest class to extract top 10 best features
	bestfeatures = SelectKBest(score_func=chi2, k=10)
	fit = bestfeatures.fit(X,y)
	dfscores = pd.DataFrame(fit.scores_)
	dfcolumns = pd.DataFrame(X.columns)
	#concat two dataframes for better visualization 
	featureScores = pd.concat([dfcolumns,dfscores],axis=1)
	featureScores.columns = ['Specs','Score']  #naming the dataframe columns
	print(featureScores.nlargest(10,'Score'))  #print 10 best features


fengr()
