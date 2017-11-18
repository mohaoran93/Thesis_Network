import pandas as pd
from src.mytools import tools
import os
abs_dir = os.path.dirname(os.path.abspath(__file__))
fd = os.path.abspath(os.path.join(abs_dir, os.pardir))
class getRawData(object):
    def __init__(self):
        pass
    def read(self,filename = '',type = 'pos'):
    # example: reader.read(filename='totallocation',type='pos')
        if type == 'edges':
            #edges = pd.read_table("data/"+str(filename)+".txt") #totallocation.txt
            edges = pd.read_table(fd+"/data/"+str(filename)+".txt") #totallocation.txt
            edges.columns=['n1', 'n2']
            return edges
        elif type == 'pos':
            posdata = pd.read_table(fd+"/data/"+str(filename)+".txt")
            posdata.columns=['node', 'time', 'latitude', 'longitude', 'id']
            return posdata
        elif type == 'artificial':
            artificial_location = pd.read_table(fd+"/data/"+str(filename)+".txt")
            artificial_location.columns=['node', 'time', 'latitude', 'longitude', 'id']
            return artificial_location
        else:
            df = pd.read_table(fd+"/data/"+str(filename)+".txt")
            return df
class getGraph(object):
    def __init__(self):
        reader = getRawData()
        self.edges = reader.read(filename='edges',type = 'edges')
        self.posdata = reader.read(filename='totallocation',type='pos')
        self.ap = reader.read(filename='artificialpostion',type='artificial')
    def getgraph(self,size = None):
        tool = tools()
        posdata = tool.remove_zero(df=self.posdata)
        posdata = posdata.append(self.ap,ignore_index=True) # append artificial locations
        if size is not None:
            partedges, pos = tool.decrease(self.edges,posdata,size=size)
            print("size is not None")
        else:
            partedges = self.edges
            pos = posdata
        return partedges,pos
