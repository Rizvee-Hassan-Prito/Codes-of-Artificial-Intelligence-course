# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 01:24:24 2021

@author: User
"""
paths=[]
path=[]
def dfs(visited, graphs, node, goal):
# print(node)
#visited.add(node)
    path.append(node)
    if node==goal:
        paths.append(list(path))
        path.remove(node)
        return visited
    visited.append(node)
    for neighbour in graphs[node]:
        dfs(visited, graphs, neighbour,goal)
    path.remove(node)
    return visited
    # Driver Code
graphs = {
'A' : ['B','C'],
'B' : ['D', 'E'],
'C' : ['F'],
'D' : [],
'E' : ['F'],
'F' : []
}
visit = dfs([], graphs, 'A','F')
path_len=len(paths[0])
k=1
while(k<len(paths)):
    if path_len>len(paths[k]):
        shortest_path=paths[k]
        k+=1
print()
print("Shortest path from A to F:",shortest_path)
    
