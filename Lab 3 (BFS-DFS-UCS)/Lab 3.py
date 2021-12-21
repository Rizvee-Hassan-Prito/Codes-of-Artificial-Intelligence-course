# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:01:02 2021

@author: User
"""

import queue as Q
def search(graph,st,ed):
    if st not in graph:
        raise TypeError (str(st) + ' not found in graph !')
        return
    if ed not in graph:
        raise TypeError (str(ed) + ' not found in graph !')
        return
    queue = Q.PriorityQueue()
    queue.put((0, [st]))
    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        
        if ed in node[1]:
            print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            break
        
        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))
def readGraph():
    lines = int( input() )
    graph = {}
    for line in range(lines):
        line = input()
        tokens = line.split()
        node = tokens[0]
        graph[node] = {}
        print
        for i in range(1, len(tokens) - 1, 2):
            print(node, tokens[i], tokens[i + 1])
    return graph
search(graph, 'Arad', 'Bucharest')
