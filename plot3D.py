from src.mytools import tools
from src.visualization import Visualization
from src.algorithm1 import algorithm1
tool = tools()
visualization = Visualization()
#algo1_3000 = algorithm1(size=3000)
algo1 = algorithm1(size=1000)

nodes_cirle = algo1.execute(node=10,k=3,distance_threshold=10)

print("the size of community is {0} and the circle center is {1}, the finally radius is {2} km"
      .format(len(nodes_cirle[0]),(nodes_cirle[1][0],nodes_cirle[1][1]),nodes_cirle[1][2]))

print(nodes_cirle[0])
# size = 1000 node=10,k=3,distance_threshold=1000
# The size of possible centers is 16798
# the size of community is 46 and the circle center is (47.454848999999996, 3.3208309999999996), the finally radius is 973.5249576741207 km
# [10, 28, 53, 60, 77, 79, 95, 114, 154, 165, 221, 248, 256, 264, 267, 282, 379, 385, 408, 447, 459, 463, 502, 554, 564, 629, 630, 641, 646, 653, 656, 664, 670, 677, 681, 710, 716, 736, 784, 834, 835, 839, 843, 847, 889, 952]
