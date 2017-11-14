import matplotlib.pyplot as plt
from networkx.algorithms import core
import pandas as pd
from src.getRawData import getRawData
from src.mytools import tools
from src.getRawData import getGraph
import networkx as nx

tool = tools()
reader = getRawData()
#
graphReader = getGraph()
loc = reader.read('totallocation',type='pos')
# partedges, pos = graphReader.getgraph(size=300)
# G1 = nx.from_pandas_dataframe(partedges,'n1','n2')
# # attrs = {0: {'attr1': 20, 'attr2': 'nothing'}, 1: {'attr2': 3}}
#
# nx.set_node_attributes(G=G1,values=pos)
# print(G1.nodes[0]['latitude'])
#
#
# nodes = []
# center = {}
node_without_checkin = tool.get_nodes_without_checkin(pos=loc)

print(node_without_checkin)
