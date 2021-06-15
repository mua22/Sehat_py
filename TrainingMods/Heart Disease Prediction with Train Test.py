import pickle
import numpy as np
import pandas as pd

from sklearn.metrics import accuracy_score, precision_score, f1_score
from sklearn.model_selection import train_test_split


dataset=pd.read_csv("heart.csv")
traindata,testdata=train_test_split(dataset,test_size=0.3,random_state=42)

x=np.array(traindata)[:,:-1]
y=np.array(traindata)[:,-1]
x_test=np.array(testdata)[:,:-1]
y_test=np.array(testdata)[:,-1]


from sklearn import svm
svm= svm.SVC(gamma='auto') 
svm.fit(x, y)


y_pred=svm.predict(x_test)
print('\nAccuracy score :\n===============\n {:.2f}'.format(svm.score(x_test, y_test)))
print("\nPrecision score:\n===============")
svmPrecision=precision_score(y_test , y_pred, average='macro')
print(svmPrecision)
print("\nf1 score:\n===============")
svmf1=f1_score(y_test , y_pred, average='macro')

file='HeartModel.sav'
pickle.dump(svm,open(file,'wb'))
