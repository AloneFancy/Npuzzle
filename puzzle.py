#!/usr/bin/python3
import time
import state
import collections
import os
import ctypes
move=['left','right','up','down']
check_finished=False

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
    afinished=DFSUtil(theState,visited)        
    if afinished:
        print("finished")
    else :
        print("dead")


def DFSUtil(theState,visited):
        """
        Start iterating throughout the puzzle
        """
        global check_finished
        if (theState.isGoal()):     
            #print("The path of states: ",visited)        
            ctypes.windll.user32.MessageBoxW(0, "The program will continue to run until it have no new state", "Final state", 1)
            os.system("pause")      #Check final goal
            return True        
        theState.terminal_display()
        visited.append(convert_to_store(theState)[:])  
        if not check_finished:                                                                          # Not found goal state yet
            for i in move:
                if not theState.check_illegal(i,theState.empty_cell[0],theState.empty_cell[1]):         # Check
                    last_state=theState.cell[:]
                    theState.movement(i)                             
                    if not check_visted(convert_to_store(theState),visited):                       
                        theState.animated()                    
                        #print(i)
                        #print("before recursion",visited)
                        DFSUtil(theState,visited)    
                        roll_back(i,theState)
                        theState.animated()
                    else:
                        roll_back(i,theState)
            return False

def roll_back(i,theState):
    #print("visited",i)                   
    if i=="left":
        theState.movement("right")
    elif i=="right":
        theState.movement("left")
    elif i=="up":
        theState.movement("down")
    elif i=="down":
        theState.movement("up")
