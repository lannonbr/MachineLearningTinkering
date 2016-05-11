from sklearn import datasets, svm

iris = datasets.load_iris()
print(iris.data)

X_train = iris.data[:-1]
Y_train = iris.target[:-1]

clf = svm.SVC()

clf.fit(X_train, Y_train)

print(clf)
print(clf.predict(iris.data[-1:]))
