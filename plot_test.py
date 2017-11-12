from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

ks = range(3,10,1)
distanc_thresholds = range(300,1,-10)

ks,distanc_thresholds = np.meshgrid(ks,distanc_thresholds)
results = (distanc_thresholds)-(5*ks)^2
results = np.sin(results)
fig1 = plt.figure()
ax = Axes3D(fig1)
ax.plot_surface(ks, distanc_thresholds, results, rstride=1, cstride=1, cmap=cm.viridis)
plt.show()


# X = np.arange(1, 5, 1)
# Y = np.arange(1, 4, 1)
# print(X,Y)
#
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# print("詹丁1")
# print(X,'詹丁2\n',Y,R)
