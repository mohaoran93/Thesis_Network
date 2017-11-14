from src.mytools import tools
from src.visualization import Visualization
from src.algorithm1 import algorithm1
tool = tools()
visualization = Visualization()
#algo1_3000 = algorithm1(size=3000)
algo1 = algorithm1(size=500)

nodes_cirle = algo1.execute(node=10,k=3,distance_threshold=1000)

print("the size of community is {0} and the circle center is {1}, the finally radius is {2} km"
      .format(len(nodes_cirle[0]),(nodes_cirle[1][0],nodes_cirle[1][1]),nodes_cirle[1][2]))

print(nodes_cirle[0])
# 1 300
# the size of community is 15 and the circle center is (51.618851666666671, 1.6824176666666661), the finally radius is 829.7859366018251 km
# [10, 28, 53, 60, 77, 79, 95, 114, 154, 221, 248, 256, 264, 267, 282]
# 1000
#


# size is not None
# The 3-core subgraph of given node 10 has 693 nodes
# Traceback (most recent call last):
#   File "/Users/mohaoran/PycharmProjects/Thesis_Network/main_test.py", line 9, in <module>
#     nodes_cirle = algo1.execute(node=10,k=3,distance_threshold=1000)
#   File "/Users/mohaoran/PycharmProjects/Thesis_Network/src/algorithm1.py", line 49, in execute
#     xx,xy,R = self.mcc1(i,j,h,X)
#   File "/Users/mohaoran/PycharmProjects/Thesis_Network/src/algorithm1.py", line 121, in mcc1
#     lat1 = self.G1.nodes[X[i]]['latitude']
# KeyError: 'latitude'
