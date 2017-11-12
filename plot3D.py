from src.mytools import tools
from src.visualization import Visualization
from src.algorithm1 import algorithm1
tool = tools()
visualization = Visualization()
#algo1_3000 = algorithm1(size=3000)
algo1 = algorithm1(size=300)

algo1.execute(node=10,k=3,distance_threshold=100)
# (140) 10,15(5),100 -> 26932
# (140) 10,15(5),50 -> 22853
# (300) 10,15(5),50 -> 111281{The size of possible centers is}

# including given node
# (300) 10,15(5),50 -> 1{The size of possible centers is}
# (300) 10,3,50 -> 1 {The size of possible centers is}
# (300) 10,3,100 -> 29 {}
# algo1.statistics()

# for k in [3,4,5,6,7,8,9]:
#     for
