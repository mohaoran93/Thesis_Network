from math import sin, cos, sqrt, atan2, radians
import pandas as pd
import networkx as nx

class tools():
    def distance(self,lat1,lon1,lat2,lon2):
        # approximate radius of earth in km
        R = 6373.0
        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return distance

    def get_nodes_without_checkin(self,pos = pd.DataFrame):
        pos = pos[pos.iloc[:,4] != '00000000000000000000000000000000']
        nodes_list = pos['node'].drop_duplicates().tolist()
        # number of nodes: 58227
        node_without_checkin = list(set(list(range(0,58228))) - set(nodes_list))
        return node_without_checkin

    def remove_zero(self,df,cols = []):
        # remove rows that satisfying all attributes in col[] list are zero
        if len(cols) > 0:
            conditions = [0.0]*len(cols)
            df = df[eval(' & '.join(["df.iloc[:,{0}] != {1}".format(col,condition) for col, condition in zip(cols,conditions)]))]
        else:
            # case 1
            df = df[df.iloc[:,4] != '00000000000000000000000000000000']
            #nodes_list = df['nodes'].value().tolist()
        return df
    def decrease(self, edges, posdf, size):
        posdf = posdf.drop_duplicates(subset=['node'], keep='first') # the first means the most new location
        posdf = posdf.sort_values(by='node') # The order is important for the next line of code.
        posdf = posdf.iloc[:size, :] # it's approximate to the max node num.

        pos ={}
        for i in range(len(posdf)):
            currentid = posdf.iloc[i, 0]
            pos[currentid] = {'latitude':posdf.iloc[i, 2], 'longitude':posdf.iloc[i, 3]}
        partedges = edges[(edges.n1 < size) & (edges.n2 < size)]
        return partedges, pos
    def artificallocation(self,org = pd.DataFrame,newdf = None):
        temp = pd.read_table("data/"+str(newdf)+".txt")
        # org = org.append(temp,ignore_index=True)
        org = temp
        return org



