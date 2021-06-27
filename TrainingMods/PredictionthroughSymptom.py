import re
import scipy
import string
import pickle
import warnings
import numpy as np
import pandas as pd


from sklearn.metrics import accuracy_score, precision_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

dataset=pd.read_csv("SymptomDataset.csv")
dataset_encoded = dataset.copy()
dataset_original = dataset.copy()

# prognosis_label_encoder = LabelEncoder()
# dataset["encoded_prognosis"] =prognosis_label_encoder.fit_transform(dataset['prognosis'])
#
# dataset_encoded[['prognosis']]=dataset[['encoded_prognosis']]

traindata,testdata=train_test_split(dataset,test_size=0.3,random_state=42)

x=np.array(traindata)[:,:-1]
y=np.array(traindata)[:,-1]
x_test=np.array(testdata)[:,:-1]
y_test=np.array(testdata)[:,-1]


logreg = LogisticRegression()
logreg = LogisticRegression(solver='liblinear')
logreg.fit(x, y)

y_pred= logreg.predict(x_test)
print('\n\nAccuracy score :\n===============\n {:.2f}'.format(logreg.score(x_test, y_test)*100))


file='SymptomBestmodel.pkl'
pickle.dump(logreg,open(file,'wb'))

