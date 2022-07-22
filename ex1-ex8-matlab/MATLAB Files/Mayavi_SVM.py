import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mayavi import mlab

x1_label1 = np.linspace(0, 10, 20)
l = np.linspace(3, 5, 20)
x2_label2 = np.linspace(0,6,20)

mlab.clf()
x, y = np.mgrid[-10:10:100j, -10:10:100j]
r = np.exp(-(x1_label1-l)**2/0.5)
mlab.surf(r, warp_scale='auto')
mlab.show()