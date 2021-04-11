#!/usr/bin/python3
import time
import state
import collections
import os
import numpy as np
move=['left','right','up','down']

def check_visted(current_state,visited):   
    #print("Here is current state",current_state)    
    for element in visited:       
        if element ==current_state:
            return True
    return False   

def convert_to_store(theState):
    temp=[]
    for i in range(0,theState.size):
        for j in range(0,theState.size):
            temp.append(theState.cell[i][j])
    return temp

def DFS(theState):
    
    visited=[]
    finished=DFSUtil(theState,visited)        
    if finished:
        print("finished")
    else :
        print("dead")


def DFSUtil(theState,visited):
        """
        Start iterating throughout the puzzle
        """
        if (theState.isGoal()): 
            print("here we go")    
            os.system('pause')           #Check final goal
            return True        
        visited.append(convert_to_store(theState)[:])  
        for i in move:
            if not theState.check_illegal(i,theState.empty_cell[0],theState.empty_cell[1]):                
                last_state=theState.cell[:]
                theState.movement(i)                             
                #print("đi thử",visited,theState.cell)
                if not check_visted(convert_to_store(theState),visited):                       
                    theState.terminal_display()                    
                    print(i)
                    print("before recursion",last_state)
                    DFSUtil(theState,visited)
                    visited.pop()
                    theState.cell=np.reshape(visited[-1],(theState.size,theState.size))
                    print('quay lại')   
                    print(visited)        
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
        return False
