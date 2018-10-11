#!/usr/bin/python
# -*- coding: latin-1 -*-
import copy

graph_start = [
      ['.','.','.','.','.','.','O','.','.','.','.','.','.','O','.','.','.','.','.','.'],
      ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
      ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
      ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
      ['.','.','.','.','.','.','O','.','.','.','.','.','.','O','.','.','.','.','.','.'],
      ['.','.','.','.','.','.','O','.','.','.','.','.','.','O','.','.','.','.','.','.'],
      ['O','O','.','.','.','O','O','O','O','.','.','.','O','O','O','O','O','O','O','O'],
      ['.','.','.','.','.','.','O','.','.','.','.','.','.','O','.','A','.','.','.','.'],
      ['.','.','.','.','.','.','.','.','.','.','.','.','.','O','.','.','.','.','.','.'],
      ['@','.','.','.','.','.','.','.','.','.','.','.','.','O','.','.','.','.','.','.'],
      ['.','.','.','.','.','.','.','.','.','.','.','.','.','O','.','.','.','.','.','.'],
      ['.','.','.','.','.','.','O','.','.','.','.','.','.','O','.','.','.','.','.','.'],
      ['.','.','.','.','.','.','O','.','.','.','.','.','.','O','.','.','.','.','.','.'],
      ['O','.','.','.','O','O','O','O','.','.','.','O','O','O','O','O','.','.','.','O'],
      ['.','.','.','.','.','.','O','.','.','.','.','.','.','O','.','.','.','.','.','.'],
      ['.','.','.','.','.','.','.','.','.','.','.','.','.','O','.','.','.','.','.','.'],
      ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
      ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
      ['.','.','.','.','.','.','O','.','.','.','.','.','.','.','.','.','.','.','.','.'],
      ['.','.','.','.','.','.','O','.','.','.','.','.','.','O','.','.','.','.','.','.']]

# graph_start = [
# ['@','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','O','.','.','.','.','.','.','.'],
# ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','O','.','.','.','.','.','.','.'],
# ['.','.','.','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','.','.','.','O','.','.','.','O','O','O','O'],
# ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','O','.','.','.','.','.','.','.','.','.','.','.'],
# ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','O','.','.','.','.','.','.','.','.','.','.','.'],
# ['.','.','.','O','O','O','O','O','O','O','O','O','O','O','O','.','.','.','O','O','O','O','O','O','O','O','O','.','.','.'],
# ['.','.','.','.','.','.','O','.','.','.','.','.','.','.','O','.','.','.','O','.','.','.','.','.','.','.','.','.','.','.'],
# ['.','.','.','.','.','.','O','.','.','.','.','.','.','.','O','.','.','.','O','.','.','.','.','.','.','.','.','.','.','.'],
# ['.','.','.','O','.','.','O','O','O','.','.','.','O','O','O','.','.','.','O','O','O','O','O','O','O','O','O','.','.','.'],
# ['.','.','.','O','.','.','.','.','.','.','.','.','O','.','.','.','.','.','.','.','.','.','.','.','.','.','O','.','A','.'],
# ['.','.','.','O','.','.','.','.','.','.','.','.','O','.','.','.','.','.','.','.','.','.','.','.','.','.','O','.','.','.'],
# ['.','.','.','O','O','O','O','O','O','O','O','O','O','.','.','.','O','O','O','O','O','O','.','.','.','O','O','O','O','O'],
# ['.','.','.','O','.','.','.','.','.','.','.','.','O','.','.','.','.','.','O','.','.','.','.','.','.','.','.','.','.','.'],
# ['.','.','.','O','.','.','.','.','.','.','.','.','O','.','.','.','.','.','O','.','.','.','.','.','.','.','.','.','.','.'],
# ['.','.','.','O','O','O','O','O','O','O','.','.','O','O','O','.','.','.','O','.','.','.','O','O','O','O','O','.','.','.'],
# ['.','.','.','.','.','.','.','O','.','.','.','.','O','.','.','.','.','.','O','.','.','.','O','.','.','.','O','.','.','.'],
# ['.','.','.','.','.','.','.','O','.','.','.','.','O','.','.','.','.','.','O','.','.','.','O','.','.','.','O','.','.','.'],
# ['O','O','O','O','.','.','.','O','.','.','O','O','O','.','.','.','O','O','O','.','.','.','O','.','.','.','O','.','.','.'],
# ['.','.','.','O','.','.','.','O','.','.','O','A','.','.','.','.','O','.','.','.','.','.','O','.','.','.','O','.','.','.'],
# ['.','.','.','O','.','.','.','O','.','.','O','.','.','.','.','.','O','.','.','.','.','.','O','.','.','.','O','.','.','.'],
# ['.','.','.','O','.','.','.','O','.','.','O','.','.','.','O','O','O','.','.','O','O','O','O','.','.','.','.','.','.','.'],
# ['.','.','.','O','.','.','.','O','.','.','O','.','.','.','.','.','O','.','.','.','.','.','O','.','.','.','.','.','.','.'],
# ['.','.','.','O','.','.','.','O','.','.','O','.','.','.','.','.','O','.','.','.','.','.','O','O','O','O','O','O','O','O'],
# ['.','.','.','O','.','.','.','O','.','.','O','O','O','O','O','O','O','O','O','O','.','.','.','.','.','.','.','.','.','.'],
# ['.','.','.','O','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','O','.','.','.','.','.','.','.','.','.','.'],
# ['.','.','.','O','.','.','.','.','.','.','.','O','O','O','O','.','.','.','.','O','O','O','O','O','O','O','O','.','.','.'],
# ['.','.','.','O','.','.','.','.','.','.','.','O','.','.','.','.','.','.','.','O','.','.','.','.','.','.','O','.','.','.'],
# ['.','.','.','O','.','.','.','O','.','.','.','O','.','.','O','O','O','O','O','O','.','.','.','O','O','O','O','.','.','.'],
# ['.','.','.','.','.','.','.','O','.','.','.','O','.','.','.','.','.','.','.','.','.','.','.','O','.','.','.','.','.','.'],
# ['.','.','.','.','.','.','.','O','.','.','.','O','.','.','.','.','.','.','.','.','.','.','.','O','.','A','.','.','.','.']]

def initialize(start): #def initialize(objective, start):

    # nodes_obj = {
    #     "no": objective,
    #     "distance": float('inf'),
    #     "parent": None,
    #     "gama": 0
    # }

    nodes_start = {
        "no":start,
        "distance": 0,
        "parent": None,
        "gama": 0
    }

    return nodes_start #return nodes_obj, nodes_start

def wavefront():
    queue = []
    visited = []
    gama = 0
    start = initialize(graph_start) # objective, start = initialize(graph_obj,graph_start)
    queue.append(start)

    while queue:
        
        #ordernar por gama
        queue.sort(key=orderGama) #, reverse=True #mau resultado..

        #escolher sucessor
        u = queue.pop(0)

        #se sucessor ainda não tiver sido explorado
        if not(u["no"] in visited):
            #se sucessor for o objectivo terminar já
            if isObjective(u, countObjectives(start)): #if u["no"]==objective["no"]:
                i = 0
                while i<len(u["no"]):
                    print u["no"][i]
                    i+=1                
                print ""
                print "profundidade-> ", u["distance"]
                print "gama-> ", u["gama"]

                getPath(u["parent"]) #getPath(u["parent"], objective)
                return
            
            #incrementar gama
            gama+=1

            noAux = left(copy.deepcopy(u["no"]))
            if not(noAux in visited):
                queue.append({"no": left(copy.deepcopy(u["no"])), "distance": u["distance"]+1, "parent": u, "gama": gama})
            
            noAux = right(copy.deepcopy(u["no"]))
            if not(noAux in visited):
                queue.append({"no": right(copy.deepcopy(u["no"])), "distance": u["distance"]+1, "parent": u, "gama": gama})

            noAux = up(copy.deepcopy(u["no"]))
            if not(noAux in visited):
                queue.append({"no": up(copy.deepcopy(u["no"])), "distance": u["distance"]+1, "parent": u, "gama": gama})

            noAux = down(copy.deepcopy(u["no"]))
            if not(noAux in visited):  
                queue.append({"no": down(copy.deepcopy(u["no"])), "distance": u["distance"]+1, "parent": u, "gama": gama})

            visited.append(copy.deepcopy(u["no"]))
       
def getPath(nodes): #def getPath(nodes, targetNode):
    
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
    print "" #UNCOMMENT ALL TO SEE SOLUTION PATH
    getPath(nodes["parent"])

#auxiliary
def getIndex(node):
    z = 0
    while z<len(node):
        for index, item in enumerate(node[z]):
            if item == '@':
                return z, index
        z+=1

def orderGama(elem):
    return elem["gama"]

#operators WAVEFRONT
def left(node):
    indexX, indexY = getIndex(node)
    
    if indexY == 0: 
        return node[:][:]
    
    if node[indexX][indexY-1] == 'O' or node[indexX][indexY] == 'O':
        return node[:][:]
    else:
        node[indexX][indexY] = '.'
        node[indexX][indexY-1] = '@'

    return node[:][:]

def right(node):
    indexX, indexY = getIndex(node)
    
    if indexY == len(node[0])-1: 
        return node[:][:]
    
    if node[indexX][indexY+1] == 'O' or node[indexX][indexY] == 'O':
        return node[:][:]
    else:
        node[indexX][indexY] = '.'
        node[indexX][indexY+1] = '@'
    
    return node[:][:]

def up(node):
    indexX, indexY = getIndex(node)
    
    if indexX == 0: 
        return node[:][:]
    
    if node[indexX][indexY] == 'O' or node[indexX-1][indexY] == 'O':
        return node[:][:]
    else:
        node[indexX][indexY] = '.'
        node[indexX-1][indexY] = '@'

    return node[:][:]

def down(node):
    indexX, indexY = getIndex(node)
    
    if indexX == len(node)-1: 
        return node[:][:]
    
    if node[indexX][indexY] == 'O' or node[indexX+1][indexY] == 'O':
        return node[:][:]
    else:
        node[indexX][indexY] = '.'
        node[indexX+1][indexY] = '@'

    return node[:][:]

def countObjectives(node):
    count = 0
    i = 0
    while i<len(node["no"]):
        count += node["no"][i].count('A')
        i+=1 

    return count

def isObjective(node, numberOfStartingObjectives):   
    count = 0
    i = 0
    while i<len(node["no"]):
        count += node["no"][i].count('A')
        i+=1 

    return count < numberOfStartingObjectives

wavefront()
