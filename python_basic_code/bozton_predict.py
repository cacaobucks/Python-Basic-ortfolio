from sklearn import datasets
boston = datasets.load_boston()

import pandas as pd
X_df = pd.DataFrame(boston.data)
X_df.columns = boston.feature_names
X_df.head()

y = boston.target
print(y[0:5])

import numpy as np
X = np.array(X_df.loc[:, ["RM"]])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8, test_size = 0.2)

from sklearn import linear_model
model = linear_model.LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(y_pred)
print(y_test)


%matplotlib inline
import matplotlib.pyplot as plt
plt.scatter(X_test, y_test, color = "blue")
plt.plot(X_test, y_pred, color = "red")
