#!/usr/bin/python3
import time
import state
import collections
import os
move=['left','right','up','down']
visited=[]
def check_visted(current_state):
    for element in visited:
        print(visited,"\n",current_state)
        if collections.Counter(element) == collections.Counter(current_state):
            return True
    return False
    #return set(cell).issubset(visited)
def puzzle(theState):
    while not theState.isGoal():
        temp=[]
        for i in range(0,theState.size):
            for j in range(0,theState.size):
                temp.append(theState.cell[i][j])
        for i in move:
            print(i)
            if not theState.check_illegal(i,theState.empty_cell[0],theState.empty_cell[1]) :
                os.system("pause")
                if not check_visted(temp):
                    visited.append(temp)
                    theState.movement(i)
                    theState.terminal_display()
                    puzzle(theState)
            