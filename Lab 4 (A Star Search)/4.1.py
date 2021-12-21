# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 02:47:31 2021

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 00:55:42 2021

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 20:31:33 2021

@author: User
"""

def aStar(start, stop):
    open_set = {start}
    closed_set = set()
    g = {}
    parents = {}
    g[start] = 0
    parents[start] = start
    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
         
        if n == stop or graph_nodes[n] == None:
            pass
        else:
            neighbours=get_neighbors(n)
            ng=neighbours.split()
            for i in range(0,len(ng),2):
                if ng[i] not in open_set and ng[i] not in closed_set:
                    open_set.add(ng[i])
                    parents[ng[i]] = n
                    g[ng[i]] = g[n] + int(ng[i+1])
                else:
                    if g[ng[i]] > g[n] + int(ng[i+1]):
                       g[ng[i]] = g[n] + int(ng[i+1])
                       parents[ng[i]] = n
        if n == None:
            print("Path does not exist")
            return None
        if n == stop:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start)
            path.reverse()
            print("Path found: {}".format(path))
            return path
        open_set.remove(n)
        closed_set.add(n)
    print("Path does not exist")
    return None

def get_neighbors(v):
    if v in graph_nodes:
        return graph_nodes[v]
    else:
        return None
    
def heuristic(n):
    h_dist = {
        'Arad' : 366,
        'Craiova' : 160,
        'Dobreta' : 242,
        'Fagaras' : 78,
        'Giurgiu' : 77,
        'Lugoj' : 244,
        'Mehadia' : 241,
        'Oradea' : 380,
        'Pitesti' : 98,
        'RimnicuVilcea' : 193,
        'Sibiu' : 253,
        'Timisoara' : 329,
        'Zerind' : 374,
        'Bucharest' : 0,
        }
    return h_dist[n]

graph_nodes = {
    'Arad':'Zerind 75 Timisoara 118 Sibiu 140',
    'Zerind':'Oradea 71 Arad 75',
    'Timisoara':'Arad 118 Lugoj 111',
    'Sibiu':'Arad 140 Oradea 151 Fagaras 99 RimnicuVilcea 80',
    'Oradea':'Zerind 71 Sibiu 151',
    'Lugoj':'Timisoara 111 Mehadia 70',
    'RimnicuVilcea':'Sibiu 80 Pitesti 97 Craiova 146',
    'Mehadia':'Lugoj 70 Dobreta 75',
    'Craiova':'Dobreta 120 RimnicuVilcea 146 Pitesti 138',
    'Pitesti':'RimnicuVilcea 97 Craiova 138 Bucharest 101',
    'Fagaras':'Sibiu 99 Bucharest 211',
    'Dobreta':'Mehadia 75 Craiova 120',
    'Bucharest':'Fagaras 211 Pitesti 101 Giurgiu 90',
    'Giurgiu':'Bucharest 90',
    }
print()
aStar('Arad', 'Bucharest')