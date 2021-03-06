# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:16:59 2020

@author: Gurman
"""

import sys
import bisect
import numpy as np
import copy

final_state = {'_':[0,0],'1':[0,1],'2':[0,2],'3':[1,0],'4':[1,1],'5':[1,2],'6':[2,0],'7':[2,1],'8':[2,2]}
#final_state = {'4':[0,0],'1':[0,1],'2':[0,2],'7':[1,0],'_':[1,1],'5':[1,2],'6':[2,0],'3':[2,1],'8':[2,2]}
final_pzl = [['_','1','2'],['3','4','5'],['6','7','8']]

def astar(init,heur):
    frontier = [init]   #Keeps track of all unexplored nodes
    explored = []       #Leeps track of all explored nodes
    paths = [[init]]    #Stores a list of all possible paths
    print("Input configuration:")
    print(init.conf)
    while True:
        if not frontier:
            print('No solution Found')
            raise IndexError
        current = frontier.pop(0)
        flag = False
        for path in paths:
            if areNeighbours(current, path[-1],heur):
                flag = True
                path.append(current)
                break
            
        for path in paths:
            if flag:
                break
            for i, node in enumerate(path): #Need for creating new path
                if areNeighbours(current, node, heur):
                    newpath = path[0:i+1]
                    newpath.append(current)
                    flag = True
                    paths.append(newpath)
                    break
        if (current.hcost == 0 and heur != '0') or np.array_equal(current.conf, final_pzl):
            return paths
        explored.append(current)
        flag = True
        for nbrindex, nbr in enumerate(getNeighbors(current,heur)):     #Inserting all the neighbours of current node to the frontier according to their priorities.
            if not inArray(nbr,frontier) and not inArray(nbr,explored):
                flag = False
                keys = [o.pcost+o.hcost for o in frontier]
                index = bisect.bisect_right(keys,nbr.pcost+nbr.hcost)
                frontier.insert(index, nbr)
            for i in frontier: #Updating frontier pcosts if a new shorter path to a particular node in frontier is found
                if np.array_equal(i.conf, nbr.conf) and i.pcost > nbr.pcost:
#                    print('updated {} from {} to {}'.format(i.conf, i.pcost, nbr.pcost))
                    i.pcost = nbr.pcost

def areNeighbours(pzl1,pzl2,heur):  #two nodes are neighbours if we can reach from one configuration to other in a single step
    if np.array_equal(pzl1,pzl2):
        return False
    pos1 = np.where(pzl1.conf == '_')
    pos2 = np.where(pzl2.conf == '_')
    flag = False
    if(pos1[0] == pos2[0]):
        if abs(pos1[1]-pos2[1]) == 1:
            flag = True
        else:
            return False
    elif(pos1[1] == pos2[1]):
        if abs(pos1[0] - pos2[0]) == 1:
            flag = True
        else:
            return False
    if flag == False:
        return False
    tmp = switch(pzl1, pos1, pos2, heur)
    return np.array_equal(tmp.conf,pzl2.conf)

def inArray(node, nodelist):
    for inode in nodelist:
        if np.array_equal(inode.conf,node.conf):
            return True
    return False

def getNeighbors(node,heur):
    nbrs  = []
    blankPos = np.where(node.conf == '_')
    
    if(blankPos[0] < 2):
        nbrs.append(switch(node,blankPos,[blankPos[0]+1,blankPos[1]],heur))
    if(blankPos[0] > 0):
        nbrs.append(switch(node,blankPos,[blankPos[0]-1,blankPos[1]],heur))
    if(blankPos[1] < 2):
        nbrs.append(switch(node,blankPos,[blankPos[0],blankPos[1]+1],heur))
    if(blankPos[1] > 0):
        nbrs.append(switch(node,blankPos,[blankPos[0],blankPos[1]-1],heur))
    return nbrs

def switch(node, pos1, pos2, heur):
    nbr = copy.deepcopy(node)
    nbr.conf[tuple(pos1)] = nbr.conf[tuple(pos2)]
    nbr.conf[tuple(pos2)] = '_'
    nbr.pcost += 1
    nbr.hcost = getHeuristicValue(nbr,heur)
    return nbr
    

def getHeuristicValue(pzl,heur):
    if heur == '0':
        return 0
    heuristic = 0
    for i in range(1,9):
        current_pos = np.where(pzl.conf == str(i))
        heuristic += abs(final_state[str(i)][0] - current_pos[0])
        heuristic += abs(final_state[str(i)][1] - current_pos[1])
    return heuristic

def isValid(src):
    if len(src) > len(set(src)):
        print('The input should be unique numbers in the range of 1 to 8')
        return False

    count = 0
    for i,num in enumerate(src):
        if num == '_':
            continue
        if not num.isnumeric() or int(num) > 8 or int(num)<1:
            print('The input should be numbers in the range of 1 to 8')
            return False
        for num2 in src[i+1:]:
            if num2 == '_':
                continue
            if num > num2:
                count += 1
    if count%2 != 0:
        print("The given instance of puzzle is insolvable because it has an odd number of inversions.")
        return False
    return True

class Node:
  def __init__(self, pzl, pcost, hcost):
    self.conf = np.asarray(pzl).reshape((3,3))
    self.pcost = pcost
    self.hcost = hcost

if __name__=="__main__":
    if(len(sys.argv)!=11):
        raise ValueError("invalid Number of Arguments : ", len(sys.argv))
    src = sys.argv[2:]
#    heur = input("Please enter heuristic to be used (0 for 0, 1 or anything else for Manhattan distance) : ") 
    heur = sys.argv[1]
    if heur == '0':
        print("Heuristic used: 0")
    else:
        print("Heuristic used: Manhattan Distance")
    if isValid(src):#Reason for this validated from https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
        pzl = Node(src,0,0)
        pzl.hcost = getHeuristicValue(pzl,heur)
        res = astar(pzl,heur)
        fres=[]
        for path in res:
            if path[-1].hcost == 0 and heur != '0':
                fres = path
            elif np.array_equal(path[-1].conf, final_pzl):
                fres = path
        print('The final path represented as a sequence of puzzle states:\n')
        [print('\n',pzl.conf, pzl.pcost) for pzl in fres]
        