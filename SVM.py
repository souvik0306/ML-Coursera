import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets._samples_generator import make_blobs

X,y = make_blobs(40,centers=2,random_state=20)

clf = svm.SVC(kernel='linear',C=100)

clf.fit(X,y)

plt.scatter(X[:,0],X[:,1],c=y,s=30,cmap=plt.cm.Paired)
plt.show()