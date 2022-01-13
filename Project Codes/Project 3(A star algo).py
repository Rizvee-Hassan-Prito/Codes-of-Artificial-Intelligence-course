# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:42:12 2022

@author: User
"""
import math
path = []

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
                    g[ng[i]] = g[n] + float(ng[i+1])
                else:
                    if g[ng[i]] > g[n] + float(ng[i+1]):
                       g[ng[i]] = g[n] + float(ng[i+1])
                       parents[ng[i]] = n
        if n == None:
            print("Path does not exist")
            return None
        if n == stop:
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start)
            path.reverse()
            return path
        open_set.remove(n)
        closed_set.add(n)
    print("Path does not exist")
    return None

def get_neighbors(v):
    if v in graph_nodes:
        return graph_nodes[v]


def heuristic(n):
    n=n.split(',')
    gl=goal.split(',')
    return math.sqrt((int(n[0]) - int(gl[0])) ** 2 + (int(n[1]) - int(gl[1])) ** 2) 

Map_List=[]
while True:
    ln=input()
    if ln:
        Map_List.append(list(ln))
    else:
        break
    
for i in range(0,len(Map_List)):
    for j in range(0,len(Map_List[i])):
        if(Map_List[i][j]=='o'):
            start=str(i)+','+str(j)
for i in range(0,len(Map_List)):
    for j in range(0,len(Map_List[i])):
        if(Map_List[i][j]=='x'):
            goal=str(i)+','+str(j)
            
            
graph_nodes = {}
for i in range(1,len(Map_List)-1):
    for j in range(0,len(Map_List[i])):
        if(Map_List[i][j]!='#'):
            key=str(i)+','+str(j)
            
            Values=''
            Values1=''
            Values2=''
            Values3=''
            Values4=''
            Values5=''
            Values6=''
            Values7=''
            Values8=''
            
            if(Map_List[i][j-1]!='#'):
                Values1=str(i)+','+str(j-1)+" "+"1.0" +" "
            
            if(Map_List[i][j+1]!='#'):
               Values2=str(i)+','+str(j+1)+" "+"1.0"+" "
            
            if(Map_List[i-1][j]!='#'):
                Values3=str(i-1)+','+str(j)+" "+"1.0"+" "
               
            if(Map_List[i+1][j]!='#'):
                Values4=str(i+1)+','+str(j)+" "+"1.0"+" "
            
            if(Map_List[i-1][j+1]!='#'):
                Values5=str(i-1)+','+str(j+1)+" "+"1.7"+" "
               
            if(Map_List[i-1][j-1]!='#'):
                Values6=str(i-1)+','+str(j-1)+" "+"1.7"+" "
                
            if(Map_List[i+1][j+1]!='#'):
                Values7=str(i+1)+','+str(j+1)+" "+"1.7"+" "
                
            if(Map_List[i+1][j-1]!='#'):
                Values8=str(i+1)+','+str(j-1)+" "+"1.7"+" "
            
            Values=(Values1+Values2+Values3+Values4+Values5+
                    Values6+Values7+Values8)
            graph_nodes[key]=Values
            
aStar(start,goal)
Map_List
for i in range(1,len(path)-1):
    a=path[i]
    a=a.split(',')
    Map_List[int(a[0])][int(a[1])]='.'
for x in Map_List:
    print("".join(map(str, x)))

"""
    Sample Map for Input:
    ##############################
    #         #              #   #
    # ####    ########       #   #
    #   o#    #              #   #
    #    ###     #####  ######   #
    #      #   ###   #           #
    #      #     #   #  #  #x  ###
    #     #####    #    #  #     #
    #              #       #     #
    ##############################
"""