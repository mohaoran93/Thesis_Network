import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import core
import pandas as pd
from src.getRawData import getRawData
from src.mytools import tools
from src.getRawData import getGraph
import networkx as nx
tool = tools()
reader = getRawData()

class algorithm1():

    def __init__(self,size):
        graphReader = getGraph()
        pos_org = reader.read(filename='totallocation',type='pos')
        partedges, pos = graphReader.getgraph(size=size)

        self.G1 = nx.from_pandas_dataframe(partedges,'n1','n2')

        nodes_to_be_remove = tool.get_nodes_without_checkin(pos=pos_org)
        self.G1.remove_nodes_from(nodes_to_be_remove)

        nx.set_node_attributes(G=self.G1,values=pos)
        self.subgraphs = []
        self.circles = []
    def execute(self,edges=None,location=None,node=None,distance_threshold=None,k = 3):
    # @parameter
    # edges: all egdes
    # node: the given node for search
    # threshold: the distance limitation
        G = self.G1
        Gk,k_max = self.Gk_with_max_k(n=node,G=G,k=k)
        #components = list(nx.connected_component_subgraphs(G=Gk,copy=True))
        Xset = nx.node_connected_component(G=Gk,n=node)
        X = list(Xset)  # X is the list of Nodes of k-core graph
        print("The {0}-core subgraph of given node {1} has {2} nodes".format(k_max,node,len(X)))
        for i in range(3,len(X),1):
            for j in range(1,i-2,1):
                for h in range(j+1,i-1,1):
                    xx,xy,R = self.mcc1(i,j,h,X)
                    d_node_center = tool.distance(lat1=Gk.nodes[node]['latitude'],
                                                  lon1=Gk.nodes[node]['longitude'],
                                                  lat2=xx,
                                                  lon2=xy)
                    if R<distance_threshold and d_node_center<distance_threshold:
                        self.circles.append((xx, xy, R))

        max_size = 0 # = len(nodes)
        for circle in self.circles:
            # select largest one from the possible circles
            xx = circle[0]
            xy = circle[1]
            R = circle[2]
            nodes = [] # clear up
            for x in X:
                node_to_center = tool.distance(lat1=Gk.nodes[x]['latitude'],
                                               lon1=Gk.nodes[x]['longitude'],
                                               lat2=xx,
                                               lon2=xy)
                if node_to_center < R:
                    nodes.append(x)
            if max_size<len(nodes):
                max_size = len(nodes)
                print(max_size)
                nodes_circle = (nodes,circle)
        print("The size of possible centers is {0}".format(len(self.circles)))
        return nodes_circle
    def statistics(self):
        # y: subgraph size x: k-core
        sizes = []
        Xsize = []
        ks = range(3,35,1)
        G = self.G1
        total = G.size()
        Xsize_total = len(G)
        for i in ks:
            Gk = core.k_core(G,k=i)
            s = Gk.size()
            print(len(Gk))
            sizes.append(s/total)
            Xsize.append(len(Gk)/Xsize_total)
        plt.plot(ks,Xsize)
        plt.xlabel('k-core')
        plt.ylabel('(# of subgraph nodes / # of full graph nodes)')
        plt.show()
        # size(number of edges) over k and distance threshold
        # first plot size-k value
    def statistics_2(self):
        #Y: community size X1: K-core X2: distance threshold
        return
    def add_node(self,node,Gk):
        if node in list(Gk):
            return Gk
        else:
            Gk.add_edges_from()
            return Gk
    def Gk_with_max_k(self,n,G,k):
        Gk = core.k_core(G,k=k)
        while n not in list(Gk):
            k = k-1
            Gk = core.k_core(G,k=k)
        return Gk,k

    def mcc1(self,i,j,h,X):
        # latitude,longitude
        lat1 = self.G1.nodes[X[i]]['latitude']
        lon1 = self.G1.nodes[X[i]]['longitude']
        lat2 = self.G1.nodes[X[j]]['latitude']
        lon2 = self.G1.nodes[X[j]]['longitude']
        lat3 = self.G1.nodes[X[h]]['latitude']
        lon3 = self.G1.nodes[X[h]]['longitude']
        xc = (lat1+lat2+lat3)/3
        xy = (lon1+lon2+lon3)/3
        R = tool.distance(lat1=lat1,lat2=lat2,lon1=lon1,lon2=lon2)
        # todo return the number of this circle include
        return xc,xy,R
    def mcc2(self,i,j,h,X):
        #TODO  get the locaiton information
        L1 = tool.distance(self.G1.nodes[X[i]]['latitude'],self.G1.nodes[X[i]]['longitude'],self.G1.nodes[X[j]]['latitude'],self.G1.nodes[X[j]]['longitude'])
        L2 = tool.distance(self.G1.nodes[X[j]]['latitude'],self.G1.nodes[X[j]]['longitude'],self.G1.nodes[X[h]]['latitude'],self.G1.nodes[X[h]]['longitude'])
        L3 = tool.distance(self.G1.nodes[X[i]]['latitude'],self.G1.nodes[X[i]]['longitude'],self.G1.nodes[X[h]]['longitude'],self.G1.nodes[X[h]]['longitude'])
        if L1<L2 and L1<L3:
            center = (self.G1.nodes[X[i]]['latitude']-self.G1.nodes[X[j]]['latitude'])/2,(self.G1.nodes[X[i]]['longitude'] - self.G1.nodes[X[j]]['longitude'])/2
            R = L1/2
        elif L2<L1 and L2<L3:
            center = (self.G1.nodes[X[i]]['latitude']-self.G1.nodes[X[j]]['latitude'])/2,(self.G1.nodes[X[i]]['longitude'] - self.G1.nodes[X[j]]['longitude'])/2
            R = L2/2
        elif L3<L2 and L3<L1:
            center = (self.G1.nodes[X[i]]['latitude']-self.G1.nodes[X[j]]['latitude'])/2,(self.G1.nodes[X[i]]['longitude'] - self.G1.nodes[X[j]]['longitude'])/2
            R = L3/2
        return center,R
