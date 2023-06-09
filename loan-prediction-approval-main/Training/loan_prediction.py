# -*- coding: utf-8 -*-
"""Loan Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14vOj9-kHfGlwsIWLtWkC1lCJhlQCSlD3
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier,RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import RandomizedSearchCV
import imblearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix, f1_score

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/content/drive')

# %cp '/content/drive/MyDrive/Colab Notebooks/loan_prediction.csv' '/content/'

#importing the dataset which is in csv file
data = pd.read_csv('loan_prediction.csv')
data

data.info

#fining rthe sum of null values un each column
data.isnull().sum()

data['Gender'] = data['Gender'].fillna(data['Gender'].mode()[0])

data['Marrieed'] = data['Married'].fillna(data['Married'].mode()[0])

#replacing + with space for filling the non values
data['Dependents']=data['Dependents'].str.replace('+','')

data['Dependents']=data['Dependents'].fillna(data['Dependents'].mode()[0])

data['Self_Employed']  = data['Self_Employed'].fillna(data['Self_Employed'].mode()[0])

data['LoanAmount'] = data['LoanAmount'].fillna(data['LoanAmount'].mode()[0])

data['Loan_Amount_Term'] = data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mode()[0])

data['Credit_History'] = data['Credit_History'].fillna(data['Credit_History'].mode()[0])

#changing th datatype of each float column to int
data['Gender']=data['Gender'].astype('int64')
data['Married']=data['Married'].astype('int64')
data['Dependents']=data['Dependents'].astype('int64')
data['Self_Employed']=data['Self_Employed'].astype('int64')
data['CoapplicantIncome']=data['CoapplicationIncome'].astype('int64')
data['LoanAmount']=data['LoanAmount'].astype('int64')
data['Loan_Amount_Term']=data['Loan_Amount_Term'].astype('int64')
data['Credit_History']=data['Credit_History'].astype('int64')

#Balancing the dataset by using smote
from imblearn.combine import SMOTETomek

smote = SMOTETomek(0.90)

#dividing the dataset into dependent and independent y and x respectively
y = data['Loan_Status']
x = data(columns=['Loan_Status'],axis=1)

#creating a new x and y variables for the balnced set
x_bal,y_bal, = smote.fit_resample(x,y)

#printing the values of y before balancing the data and after
print(y.value_counts())
print(y_bal.value_counts())

data.describe()

#plotting the using displot
plt.figure(figsize=(12,5)
plt.subplot(121)
sns.distplot(data['ApplicantIncome'], color='r')
plt.subplot(122)
sns.distplot(data[Credit_History'])
plt.show

#plotting the count plot
plt.figure(figsize=(18,4))
plt.subplot(1,4,1)
sns.countplot(data['Gender'])
plt.sublot(1,4,2)
sns.countplot(data['Education'])
plt.show()

#visualsing two colunms againist each other
plt.figure(figsize=(20,5))
plt.subplot(131)
sns.countplot(data['Married'],hue=data['Gender'])
plt.subplot(132)
sns.countplot(data['Self_Employed'],hue=data['Education'])
plt.subplot(133)
sns.countplot(data['Property_Area'],hue=data['Loan_Amount_Term'])

#visulaized based gender and income what would be the application status
sns.swarmplot(data['Gender'],data['ApplicantIncome'],hue = data['Loan_Status'])

#perfroming feature scaling operation using standard scaller on x part of the dataset because
#there different type of values  in the colunms
sc=StandardScaler()
x_bal=sc.fit_transform(x_bal)

x_bal = pd.DataFrame(x_bal,colunms=names)

#splitting the dataset in train and test on balnmced dataset
x_train, x_test, y_train, y_test = train_test_split(x_bal, y_bal, test_size=0.33, random_state=42)

def decisionTree(x_train,x_test,y_train,y_test)
    dt=DecisionTreeClassifier()
    dt.fit(x_train,y_train)
    yPred = dt.predict(x_test)
    print('***DecisionTreeClassifier***')
    print('Confusion matrix')
    print(confusion_matrix(y_test,yPred))
    print('Classification report')
    print(classification_report(y_test,ypred))

def randomForest(x_train, x_test, y_train, y_test):
    rf = RandomForestClassifier()
    rf.fit(x_train,y_train)
    yperd = rf.predict(x_test)
    print('***RandomForestClassifier***')
    print('Confusion matrix')
    print(confusion_matrix(y_test,ypred))
    print('Classification report')
    print(classification_report(y_test,ypred))

def KNN(x_train, x_test, y_train, y_test):
    knn = KNeighborsClassifier()
    knn,fit(x_train,y_train)
    ypred = knn.predict(x_test)
    print('***KNeighborsClassifier***')
    print('confusion matrix')
    print('Confusion matrix')
    print(confusion_matrix(y_test,ypred))
    print('Classification report')
    print(classification_report(y_test,ypred))

def xgboost(x_train, x_test, y_train, y_test):
    xg = GradientBoostingClassifier()
    xg.fit(x_train,y_train)
    ypred = xg.Predict(x_test)
    print('***GradientBoostingClassifier***')
    print('Confusion matrix')
    Print(confusion_matrix(y_test,ypred))
    print('Classification report')'
    print(classification_report(y_test,ypred)

#Importing the keras libraries and packages
import imblearn.tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#Initialising the ANN
classifier = Sequential()

#Adding the input layer and the first hidden layer
classifier.add(Dense(units=100, activation='relu', input_dim=11))

#Adding the second hidden layer
classifier.add(Dense(units=50,activation='relu'))

#Adding the output layer
classifier.add(Dense(units=1,activation='sigmoid'))

#compiling the ANN
classifier.compile(optimizer='adam',loss='binary'_crossentropy',metrics=['accuracy'])

#Fitting the ANN to the Training set
model_hostory = classifier.fit(x_train, y_train, batch_size=100,validation_split=0.2,epochs=100)

#Gender Married Dependents Education Self_Employed Application CoapplicantIncome LoanAmount Loan_Amount_Term Credit_History Property_Area
dtr.predict([[1,1,0,1,1,4276,1542,145,240,0,1]])

#Gender Married  Dependents Education Self_Employed ApplicantIncome CoapplicantIncome LoanAmount Loan_Amount_Term Credit_History Property_Area
rfr.Predict([[1,1,0,1,1,4276,1542,145,240,0,1]])

#Gender Married Dependents Education Self_Employed ApplicantIncome CoapplicantIncome LoanAmount Loan_Amount_Term Credit_History property_Area
knn.predict([[1,1,0,1,1,4276,145,240,0,1]])

#Gender Married Dependents Education Self_Employed ApplicantIncome CoapplicantIncome LoanAmount Loan_Amount_Term Credit_History property_Area
xgb.predict([[1,1,0,1,1,4276,145,240,0,1]])

# Commented out IPython magic to ensure Python compatibility.
classifier.save("loan.h5")

# %cp '/content/loan.h5'

#predicting the Test set rsults
y_pred = classifier.predict(x_test)

y_pred

y_pred = (y_pred > 0.5)
y_pred

def predit_exit(sample_value):
  sample_value = np.array(sample_value)
  sample_value = sample_value.reshape(1,-1)
  sample_value = sc.transform(sample_data)
  return classifier.predict(sample_value)

sample_value = [[1,1,0,1,1,4276,1542,145,240,0,1]]
if predict_exit(sample_values)>0.5:
  print('prediction:High chance of Loan Approval!')
else:
  print('prediction:Low chance Loan Approval.')

sample_value=[[1,0,1,1,45,14,45,240,1,1]]
if predict_exit(sample_value)>0.5:
  print('prediction:High chance of Loan Approval!')
else:
  print('prediction:Low chance of Loan Approval.')

def compareModel(x_train,x_test,y_train,y_test):
  decisionTree(x_train,x_test,y_train,y_test)
  print('_'*100)
  RandomForest(x_train,x_test,y_train,y_test)
  print('_'*100)
  xGB(x_train,_test,y_train,y_test)
  print('_'*100)
  KNN(x_train.x_test,y_train,y_test)
 # print('_'*100_)

#compareModel(x_train,x_test,y_train,y_test_)

#ypred = classifier.predict(x_test)
#print(accuracy_score(y_pred,y_test))
#print("ANN Model")
#print("Confusion_Matrix")
#print(confusion_matrix(y_test,y_pred))
#print("Classification Report")
#print(classification_report(y_test,y_pred))

from sklearn.model_selection import cross_val_score

#rf = RandomForestClassifier()
#rf.fit(x_train,y_train)
#ypred = rf.predict(x_test)

#f1_score(ypred,y_test,average='weighted')

#cv = cross_val_score(rf,x,y,cv=5)

#np.mean(cv)

#saving the model by using pickle funtion
#pickle.dump(model,open('rdf.pkl','wb'))