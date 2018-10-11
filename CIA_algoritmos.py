#!/usr/bin/python
# -*- coding: latin-1 -*-
import copy

graph_obj = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,1]]

graph_start = [[0,1,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]
			   
def initialize(objective, start):

    nodes_obj = {
        "no": objective,
        "distance": float('inf'),
        "parent": None,
        "gama": 0
    }

    nodes_start = {
        "no":start,
        "distance": 0,
        "parent": None,
        "gama": 0
    }

    return nodes_obj, nodes_start

def bfs():
    queue = []
    objective, start = initialize(graph_obj,graph_start)
    queue.append(start)

    while queue:
        u = queue.pop(0)
        if u["no"]==objective["no"]:
            print u["no"][0]
            print u["no"][1]
            print u["no"][2]
            print u["no"][3]
            print ""

            getPath(u["parent"], objective)
            return

        queue.append({"no": left(copy.deepcopy(u["no"])), "distance": u["distance"]+1, "parent": u})
        queue.append({"no": right(copy.deepcopy(u["no"])), "distance": u["distance"]+1, "parent": u})
        queue.append({"no": up(copy.deepcopy(u["no"])), "distance": u["distance"]+1, "parent": u})
        queue.append({"no": down(copy.deepcopy(u["no"])), "distance": u["distance"]+1, "parent": u})

def dfs():
    queue = []
    visited = []
    objective, start = initialize(graph_obj,graph_start)
    queue.append(start)

    while queue:
        
        u = queue.pop(0)        
        if not(u["no"] in visited):

            if u["no"]==objective["no"]:
                print u["no"][0]
                print u["no"][1]
                print u["no"][2]
                print u["no"][3]
                print ""

                getPath(u["parent"], objective)
                return

            queue.insert(0,{"no": left(copy.deepcopy(u["no"])), "distance": u["distance"]+1, "parent": u })
            queue.insert(0,{"no": right(copy.deepcopy(u["no"])), "distance": u["distance"]+1, "parent": u })
            queue.insert(0,{"no": up(copy.deepcopy(u["no"])), "distance": u["distance"]+1, "parent": u })
            queue.insert(0,{"no": down(copy.deepcopy(u["no"])), "distance": u["distance"]+1, "parent": u })

            visited.append(copy.deepcopy(u["no"]))

        
def getPath(nodes, targetNode):
    
    if nodes["parent"] == None:
        i = 0
        while i<len(nodes["no"]):
            print nodes["no"][i]
            i+=1                
        print ""
        return
    
    y = 0
    while y<len(nodes["no"]):
        print nodes["no"][y]
        y+=1                
    print ""
    getPath(nodes["parent"],targetNode)

#auxiliary
def getIndex(node):
    z = 0
    while z<len(node):
        for index, item in enumerate(node[z]):
            if item == 1:
                return z, index
        z+=1
		
#operators BFS AND DFS
def left(node):
    indexX, indexY = getIndex(node)
  
    if indexY == 0: 
        return node[:][:]
  
    node[indexX][indexY] = 0
    node[indexX][indexY-1] = 1

    return node[:][:]

def right(node):
    indexX, indexY = getIndex(node)
  
    if indexY == 3: 
        return node[:][:]
  
    node[indexX][indexY] = 0
    node[indexX][indexY+1] = 1
  
    return node[:][:]

def up(node):
    indexX, indexY = getIndex(node)
  
    if indexX == 0: 
        return node[:][:]
  
    node[indexX][indexY] = 0
    node[indexX-1][indexY] = 1

    return node[:][:]

def down(node):
    indexX, indexY = getIndex(node)
  
    if indexX == 3: 
        return node[:][:]
  
    node[indexX][indexY] = 0
    node[indexX+1][indexY] = 1

    return node[:][:]
	
bfs()
#dfs()