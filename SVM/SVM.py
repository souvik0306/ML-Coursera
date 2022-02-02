import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets._samples_generator import make_blobs

X,y = make_blobs(40,centers=2,random_state=20)

clf = svm.SVC(kernel='linear',C=1)
clf.fit(X,y)
plt.scatter(X[:,0],X[:,1],c=y,s=30,cmap=plt.cm.Paired)
plt.show() 

newData = [[3,4],[5,6],[4,6]]
print(clf.predict(newData))
