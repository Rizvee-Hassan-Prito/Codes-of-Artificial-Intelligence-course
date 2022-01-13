# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 02:28:43 2022

@author: User
"""
new_path=[]
def bfs_shortest_path(graph, start, goal):
# keep track of explored nodes
    explored = []
# keep track of all the paths to be checked
    queue = [[start]]
# return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"
# keeps looping until all possible paths have been checked
    while queue:
# pop the first path from the queue
        path = queue.pop(0)
# get the last node from the path
        node = path[-1]
        #print(path)
        if node not in explored:
            neighbours = graph[node]
# go through all neighbour nodes, construct a new path and
# push it into the queue
            for neighbour in neighbours:
                new_path =list(path)
                new_path.append(neighbour)
                queue.append(new_path)
# return path if neighbour is goal
                if neighbour == goal:
                    return new_path
# mark node as explored
            explored.append(node)
# in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("

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

graph = {}
for i in range(1,len(Map_List)-1):
    for j in range(0,len(Map_List[i])):
        if(Map_List[i][j]!='#'):
            key=str(i)+','+str(j)
            lst=[]
            
            if(Map_List[i][j-1]!='#'):
                lst.append(str(i)+','+str(j-1))
            
            if(Map_List[i][j+1]!='#'):
               lst.append(str(i)+','+str(j+1))
            
            if(Map_List[i-1][j]!='#'):
                lst.append(str(i-1)+','+str(j))
               
            if(Map_List[i+1][j]!='#'):
                lst.append(str(i+1)+','+str(j))
            
            if(Map_List[i-1][j+1]!='#'):
                lst.append(str(i-1)+','+str(j+1))
               
            if(Map_List[i-1][j-1]!='#'):
                lst.append(str(i-1)+','+str(j-1))
                
            if(Map_List[i+1][j+1]!='#'):
                lst.append(str(i+1)+','+str(j+1))
                
            if(Map_List[i+1][j-1]!='#'):
                lst.append(str(i+1)+','+str(j-1))
            
            graph[key]=lst
            
path=bfs_shortest_path(graph, start, goal)
    
for i in range(1,len(path)-1):
    a=path[i]
    a=a.split(',')
    Map_List[int(a[0])][int(a[1])]='.'
for xs in Map_List:
    print("".join(map(str, xs)))

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