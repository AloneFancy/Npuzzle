#!/usr/bin/python3
import time
import state
import collections
import os
move=['left','right','up','down']

def check_visted(current_state,visited):   
    #print("Here is current state",current_state)    
    for element in visited:    
       # print(element)    
        if element==current_state:
            return True
    return False
   

def storing_state(theState):
    temp=[]
    for i in range(0,theState.size):
        for j in range(0,theState.size):
            temp.append(theState.cell[i][j])
    return temp

def DFS(theState):
    visited=[]
    finished=False
    DFSUtil(theState,visited,finished)
    if finished:
        print("finished")
    else :
        print("dead")


def DFSUtil(theState,visited,finished):
        visited.append(storing_state(theState))
        theState.terminal_display()
        if (theState.isGoal()):
            finished=True
            finished=staticmethod(finished)
            return
        for i in move:
            if not theState.check_illegal(i,theState.empty_cell[0],theState.empty_cell[1]) :                
                theState.movement(i)
                if not check_visted(storing_state(theState),visited):                       
                    last_state=theState.cell
                    print("before recursion",last_state)
                    DFSUtil(theState,visited,finished)   
                    theState.cell=last_state
                    print(last_state)
                    theState.terminal_display()        
                else:
                    print("visited",i)                   
                    if i=="left":
                        theState.movement("right")
                    elif i=="right":
                        theState.movement("left")
                    elif i=="up":
                        theState.movement("down")
                    elif i=="down":
                        theState.movement("up")
