import pandas as pd
from src.mytools import tools

class getRawData():

    def __init__(self):
        pass
    def read(self,filename = '',type = 'pos'):
        if type == 'edges':
            edges = pd.read_table("data/"+str(filename)+".txt") #totallocation.txt
            edges.columns=['n1', 'n2']
            return edges
        elif type == 'pos':
            posdata = pd.read_table("data/"+str(filename)+".txt")
            posdata.columns=['node', 'time', 'latitude', 'longitude', 'id']
            return posdata
        elif type == 'artificial':
            artificial_location = pd.read_table("data/"+str(filename)+".txt")
            artificial_location.columns=['node', 'time', 'latitude', 'longitude', 'id']
            return artificial_location
        else:
            df = pd.read_table("data/"+str(filename)+".txt")
            return df
class getGraph():
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
