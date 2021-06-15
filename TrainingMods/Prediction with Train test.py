import pickle
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split

data = pd.read_csv("4-diseases.csv")

x_train, x_test = train_test_split(data, test_size=0.3, random_state=1)

a_train = np.array(x_train)[:, :-1]
b_train = np.array(x_train)[:, -1]
a_test = np.array(x_test)[:, :-1]
b_test = np.array(x_test)[:, -1]

kneriestNeighbour = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
kneriestNeighbour.fit(a_train, b_train)

y_pred = kneriestNeighbour.predict(a_test)
test_dataset_original = x_test.copy()
test_dataset_original["predicted_Disease"] = y_pred

score = kneriestNeighbour.score(a_test, b_test)
print("\n")
print("Accuracy score : ")
print("=================")
print(score)


filename = 'four diseases.pkl'
pickle.dump(kneriestNeighbour, open(filename, 'wb'))
