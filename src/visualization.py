import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from src.getRawData import getGraph
from src.getRawData import getRawData
from src.mytools import tools
tool = tools()
reader = getRawData()


class Visualization():
    def __init__(self):
        pass
    # visualization method 1
    # input: the node size
    # output: visualization for some nodes of given size
    def visualization_with_spatial_info(self,size):
        graphReader = getGraph()
        partedges, pos = graphReader.getgraph(size=size)
        options = {
            'node_size': 30,
            'font_size': 8,
            'alpha': 0.2,
        }
        G1 = nx.from_pandas_dataframe(partedges,'n1','n2')
        nx.draw_networkx(G1,pos=pos,**options)
        plt.show()
    # visualization method 2
    # input: the nx graph
    # output: the visualization for this graph
    def visualization_with_spatial_info(self,G):
        options = {
            'node_size': 30,
            'font_size': 8,
            'alpha': 0.2,
        }
        nx.draw_networkx(G,**options) # TODO pos=pos
        pass
# side mark
# example: location pos = {'node_name': (-118, 33),'node_name2': (-118, 33)}
