from sklearn import datasets
digits = datasets.load_digits()


X = digits.data
y = digits.target



import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()

for i, x in enumerate(X[0:10], 0):
    sp = fig.add_subplot(2, 5, (i + 1))
    sp.imshow(x.reshape(8, 8), cmap = "gray")
    
    
X_train = X[:1201]
X_test  = X[1201:]
y_train = y[:1201]
y_test  = y[1201:]


from sklearn.svm import SVC
classifier = SVC(kernel = "linear")
classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test)
print(y_pred)
print(y_test)


from sklearn import metrics
print(metrics.confusion_matrix(y_test, y_pred))


print(metrics.classification_report(y_test, y_pred))
