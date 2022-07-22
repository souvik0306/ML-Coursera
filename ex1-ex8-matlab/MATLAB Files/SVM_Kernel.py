import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mayavi import mlab

def f(x, l):
    f1 = np.exp(-(x-l)**2/1)
    return (f1)

x1_label1 = np.linspace(0, 10, 20)
l = np.linspace(3, 5, 20)
x2_label2 = np.linspace(0,6,20)

X, Y = np.meshgrid(x1_label1, x2_label2)

Z = f(X, l)
fig = plt.figure()

ax = plt.axes(projection='3d')
surf = ax.contour3D(X, Y, Z, 400, cmap='turbo')     
# matplotlib.cm.coolwarm

ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('z')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

