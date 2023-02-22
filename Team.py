import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('REAL.csv')
X = data[['X', 'Y']]
y = data['Z']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
# save_model(model)

Pred = (1,15)
Pred1 = np.asarray(Pred)
Pred2 = Pred1.reshape(1,-1)
realpre = clf.predict(Pred2)
print(realpre[0])


