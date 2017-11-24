import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, FixedFormatter
from sklearn.neighbors.kde import KernelDensity
from scipy.stats import norm
from src.getRawData import getRawData
from src.mytools import tools


tool = tools()
reader = getRawData()
df = reader.read(filename="totallocation",type='pos')
df = tool.remove_zero(df = df)
# there are 4492668 nodes
size =500000#0
df = df[0:size]
# df['latitude']   df['longitude']
Cx = df['longitude'][:, np.newaxis]
# print(df)
Cy = df['latitude'][:, np.newaxis]

# part 1: category the locations

# test





f,ax = plt.subplots(2,2)
plotX = False
if plotX == True:
    x = Cx
    X_plot = np.linspace(-180, 180, len(x))[:, np.newaxis]
else:
    x = Cy
    X_plot = np.linspace(-90, 90, len(x))[:, np.newaxis]

# KDE
kde = KernelDensity(kernel='epanechnikov', bandwidth=0.05).fit(x) # gaussian
log_dens = kde.score_samples(X_plot)
ax[0,0].fill(X_plot[:, 0], np.exp(log_dens), fc='#AAAAFF')
# ax[0,0].text(x = 'left',y = 'bottom',s= "epanechnikov Kernel, size =50k, b=0.05")
ax[0,0].set_title(label="epanechnikov Kernel, size ="+str(size/1000)+"k, b=0.05",loc="center")
# KDE
kde = KernelDensity(kernel='epanechnikov', bandwidth=0.75).fit(x) # gaussian
log_dens = kde.score_samples(X_plot)
ax[0,1].fill(X_plot[:, 0], np.exp(log_dens), fc='#AAAAFF')
ax[0,1].set_title(label="epanechnikov Kernel, size ="+str(size/1000)+"k, b=0.75",loc="center")
# KDE
kde = KernelDensity(kernel='epanechnikov', bandwidth=2.25).fit(x) # gaussian
log_dens = kde.score_samples(X_plot)
ax[1,0].fill(X_plot[:, 0], np.exp(log_dens), fc='#AAAAFF')
ax[1,0].set_title(label="epanechnikov Kernel, size ="+str(size/1000)+"k, b=2.25",loc="center")
# KDE
kde = KernelDensity(kernel='epanechnikov', bandwidth=3).fit(x) # gaussian
log_dens = kde.score_samples(X_plot)
ax[1,1].fill(X_plot[:, 0], np.exp(log_dens), fc='#AAAAFF')
ax[1,1].set_title(label="epanechnikov Kernel, size ="+str(size/1000)+"k, b=3",loc="center")


plt.show()


# # part 2 plot
# nullfmt = NullFormatter()         # no ticks labels
#
# # definitions for the axes
# left, width = 0.1, 0.65
# bottom, height = 0.1, 0.65
# bottom_h = left_h = left + width + 0.02
#
# rect_scatter = [left, bottom, width, height]
# rect_histx = [left, bottom_h, width, 0.2]
# rect_histy = [left_h, bottom, 0.2, height]
#
# # start with a rectangular Figure
# plt.figure(1, figsize=(8, 8))
#
#
# axScatter = plt.axes(rect_scatter)
# axHistx = plt.axes(rect_histx)
# axHisty = plt.axes(rect_histy)
#
# # no labels
# axHistx.xaxis.set_major_formatter(nullfmt)
# axHisty.yaxis.set_major_formatter(nullfmt)
#
# # the scatter plot:
# axScatter.scatter(x, y)
#
# # now determine nice limits by hand:
# binwidth = 0.15
# xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
# lim = (int(xymax/binwidth) + 1) * binwidth
# limx = lim
# limy = 120
#
# axScatter.set_xlim((-limx, limx)) # the limits
# axScatter.set_ylim((-75, 100))
# axScatter.set_xlabel(xlabel='longitude')
# axScatter.set_ylabel(ylabel='latitude')
# # axScatter.set_title('scatter plot of locations') # problem the title will be covered by histogram thus invisible.
#
# bins = np.arange(-lim, lim + binwidth, binwidth)
# axHistx.hist(x, bins=bins)
# axHisty.hist(y, bins=bins, orientation='horizontal')
# axHistx.set_title('histogram of longitudes')
# axHisty.set_title('histogram of latitude')
#
# axHistx.set_xlim(axScatter.get_xlim())
# axHisty.set_ylim(axScatter.get_ylim())
#
# plt.show()
