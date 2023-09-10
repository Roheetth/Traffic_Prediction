from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
import numpy as np
import pickle


import numpy as np
import pandas as pd
#from sklearn.preprocessing import LabelEncoder




knn = pickle.load(open(r'C:\Users\HP\Downloads\Project\Project\FINAL_CODE\FRONTEND\traffic_project\traffic_knn.pkl', 'rb'))
rf = pickle.load(open(r'C:\Users\HP\Downloads\Project\Project\FINAL_CODE\FRONTEND\traffic_project\traffic_rf.pkl', 'rb'))

data = pd.read_csv(r'C:\Users\HP\Downloads\Project\Project\FINAL_CODE\FRONTEND\traffic_project\new_test_data.csv')
print(data.head(1))
print(data.shape)
#x = data.drop(['Unnamed: 0'],axis=1)

def predict(algo,row):
	#print(x.columns)
	test_data=data.loc[row].values.reshape(1,-1)
	print(test_data.shape)
	#print(test_data.columns)
	if algo == 'knn':
		y_pred = knn.predict(test_data)
		return y_pred[0]
	elif algo == 'rf':
		y_pred = rf.predict(test_data)
		return y_pred[0]
	