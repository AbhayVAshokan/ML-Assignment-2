# Importing necessary libraries
 
import numpy as np
import pandas as pd
 
from sklearn.model_selection import train_test_split
 
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
 
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

dataset = pd.read_csv('abalone.csv')
print(dataset.head())
print(dataset.describe())

le = LabelEncoder()
dataset['sex'] = le.fit_transform(dataset['sex'])

X = dataset.iloc[:,:8].values
y = dataset.iloc[:,8].values
y = [1 if i>=9 else 0 for i in y]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

knn_mod = KNeighborsClassifier(n_neighbors = 61)
knn_mod.fit(X_train, y_train)

y_pred = knn_mod.predict(X_test)

print('Confusion Matrix')
print(confusion_matrix(y_test, y_pred))

print('\nPrecision')
print(precision_score(y_test, y_pred))
print('\nRecall')
print(recall_score(y_test, y_pred))
print('\nf1-score')
print(f1_score(y_test, y_pred))