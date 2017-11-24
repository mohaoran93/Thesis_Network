import matplotlib.pyplot as plt
from networkx.algorithms import core
import pandas as pd
from src.getRawData import getRawData
from src.mytools import tools
from src.getRawData import getGraph
import networkx as nx
tool = tools()

'''
Algorithm 2
==Algorithm 2 unnameS (unname Search)==
 input: 
        node : the given node to be used in search
        k: (optional) 
        distance_threshold: radius-threshold 
        
 output: 
        circle: a  having tuple form (nodes,(o,r))
        o: (longitude,latitude)
        r: the final radius which is smaller than distance_threshold
'''
class algorithm2(object):

    def __init__(self,size):
        graphReader = getGraph()
        reader = getRawData()


        self.pos_org = reader.read(filename='totallocation',type='pos')  # location file is very large
        partedges, pos = graphReader.getgraph(size=size)
        nodes_to_be_remove = tool.get_nodes_without_checkin(pos=self.pos_org)

        self.G1 = nx.from_pandas_dataframe(partedges,'n1','n2')
        self.G1.remove_nodes_from(nodes_to_be_remove)

        nx.set_node_attributes(G=self.G1,values=pos)
        self.subgraphs = []
        self.circles = []
    def excut(self,node=None,distance_threshold=None,k = 3):
        #
        import queue as Q
        queue = Q.PriorityQueue()
        # Init Queue, S, T
        # dn: dictionary  key: distance value node
        # S set of nodes close to the given node
        # T
        dn = []
        dn.append({0:node})
        queue.put(0)
        S = []
        #T = []
        G = self.G1
        while(queue.maxsize()>0):
            #p = dn
            #p = queue.get()
            # for n in G.neighbors(p):
            #     if nx.degree(G,n) > k:
            #         if tool.distance(n,node):
                        #
            pass
        return
