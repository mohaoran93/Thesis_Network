from src.mytools import tools
from src.visualization import Visualization
from src.algorithm1 import algorithm1
import sys
import os
tool = tools()

abs_dir = os.path.dirname(os.path.abspath(__file__))
fd = os.path.abspath(os.path.join(abs_dir, os.pardir))
print(fd)

# algo1 = algorithm1(size=500)
#
# nodes_cirle = algo1.execute(node=10,k=3,distance_threshold=1000)
#
# print("the size of community is {0} and the circle center is {1}, the finally radius is {2} km"
#       .format(len(nodes_cirle[0]),(nodes_cirle[1][0],nodes_cirle[1][1]),nodes_cirle[1][2]))
#
# print(nodes_cirle[0])
