from sklearn import tree

X = [[0, 0], [0.4, 0.4], [1, 1]]
Y = [0, 5, 1]

clf = tree.DecisionTreeClassifier()
clf.fit(X,Y)

print(clf.predict([0.4, 0.4]))
