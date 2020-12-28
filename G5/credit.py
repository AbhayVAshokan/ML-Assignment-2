
import numpy as np
import pandas as pd

''' Import the data set'''
data = pd.read_csv("creditcard.csv")

print(data.info())
print(data.head())

'''In this data set, time is provided. There are 28 features V1 to V28 obfuscated for confidentiality purposes.
The class variable denote if the transaction is normal or fraud, Class = 1 for fraud, 0 for normal.
Lets explore the data a bit more.
'''

print (data.Amount[data.Class == 1].describe())

print (data.Amount[data.Class == 0].describe())



''' In this dataset there are very less cases of fraud- 492 compared to normal cases which are 284315.
While training any model, we'll need to make sure to train it on sufficient number of both cases.
We will implement undersampling, that is using less samples from case 0 in order to train the model correctly.
'''

normal_class = data[data.Class == 0]
fraud_class = data[data.Class == 1]
''' Here we are using same amout of normal class data as fraud class data '''
undersampled_data = pd.concat([normal_class.sample(frac = (len(fraud_class)/len(normal_class))), fraud_class.sample(frac=1)],axis=0)
X = pd.DataFrame(undersampled_data.iloc[:,undersampled_data.columns!='Class'])
y = undersampled_data.iloc[:,undersampled_data.columns == 'Class']


''' We need to scale the data'''

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X["scaled_Amount"]=  sc.fit_transform(X.iloc[:,29].values.reshape(-1,1))

'''Dropping Time and Old amount'''
X= X.drop(["Time","Amount"], axis= 1)


'''Splitting in train and test set'''
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)

'''We will make use of Support vector machine classifier'''

from sklearn.svm import SVC
classifier= SVC(C= 10, kernel= 'rbf', random_state= 0)
classifier.fit(X_train, np.array(y_train).ravel())

       


'''We will now try the model on entire data set'''

data["scaled_Amount"]=  sc.fit_transform(data.iloc[:,29].values.reshape(-1,1))
data= data.drop(["Time","Amount"], axis= 1)

label = data.iloc[:,28]
data = data.drop(["Class"],axis=1)


X_train, X_test, y_train, y_test = train_test_split(data, label, test_size = 0.25, random_state = 0)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("The accuracy is "+str((cm[1,1]+cm[0,0])/(cm[0,0] + cm[0,1]+cm[1,0] + cm[1,1])*100) + " %")
print("The recall is "+ str(cm[1,1]/(cm[1,0] + cm[1,1])*100) +" %")
print("The precision is "+ str(cm[1,1]/(cm[0,1] + cm[1,1])*100) +" %")
