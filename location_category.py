import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, FixedFormatter
from src.getRawData import getRawData
from src.mytools import tools
tool = tools()
reader = getRawData()
df = reader.read(filename="totallocation",type='pos')
df = tool.remove_zero(df = df)
# there are 4492668 nodes
size =100000
df = df[0:size]
# df['latitude']   df['longitude']

#x = np.random.randn(1000)
x = df['longitude']
#y = np.random.randn(1000)
y = df['latitude']

nullfmt = NullFormatter()         # no labels
# labels = FixedFormatter(['longitude','latitude'])
# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
bottom_h = left_h = left + width + 0.02

rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom_h, width, 0.2]
rect_histy = [left_h, bottom, 0.2, height]

# start with a rectangular Figure
plt.figure(1, figsize=(8, 8))

axScatter = plt.axes(rect_scatter)
axHistx = plt.axes(rect_histx)
axHisty = plt.axes(rect_histy)

# no labels
axHistx.xaxis.set_major_formatter(nullfmt)
axHisty.yaxis.set_major_formatter(nullfmt)

# the scatter plot:
axScatter.scatter(x, y)

# now determine nice limits by hand:
binwidth = 0.25
xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
lim = (int(xymax/binwidth) + 1) * binwidth

axScatter.set_xlim((-lim, lim))
axScatter.set_ylim((-lim, lim))

bins = np.arange(-lim, lim + binwidth, binwidth)
axHistx.hist(x, bins=bins)
axHisty.hist(y, bins=bins, orientation='horizontal')

axHistx.set_xlim(axScatter.get_xlim())
axHisty.set_ylim(axScatter.get_ylim())

plt.show()