#!/usr/bin/python3
import time
import state
import collections
import os
import ctypes
move=['left','right','up','down']
check_finished=False

def check_visted(current_state,visited):   
    """
    CHECK IF THE STATE IS PASSED 
    """
    for element in visited:       
        if element ==current_state:
            return True
    return False   

def convert_to_store(theState):                                 
    """
    Convert N-d dimension array to 1D array
    """
    temp=[]
    for i in range(0,theState.size):
        for j in range(0,theState.size):
            temp.append(theState.cell[i][j])
    return temp

def DFS(theState):    
    visited=[]
    afinished=DFSUtil(theState,visited)        
    if afinished:
        print("Bingo we have a solution")
    else :
        print("No solution")


def DFSUtil(theState,visited):
        """
        Start iterating throughout the puzzle
        """
        global check_finished               #CHECK FINISHED VARIABLE FOR DISPLAYING MESSAGE BOX
        if (theState.isGoal()):     
            ctypes.windll.user32.MessageBoxW(0, "The program will continue to run until it have no new state", "Final state", 1) #USE THIS WITH WINDOWS PLS I WILL CRY ON LINUX PAIN
            print(visited)          #PRINT THE PATH
            os.system("pause")      
            return True        
        theState.terminal_display()                                                 
        visited.append(convert_to_store(theState)[:])                               # ADD A NEW STATE TO THE VISITED
        if not check_finished:                                                                          # Not found goal state yet
            for i in move:
                if not theState.check_illegal(i,theState.empty_cell[0],theState.empty_cell[1]):         # Check
                    last_state=theState.cell[:]
                    theState.movement(i)                             
                    if not check_visted(convert_to_store(theState),visited):       #CHECK IF THE NEW STATE IS VISITED OR NOT                
                        theState.animated()                                         #DRAW THE NEW MOVE
                        DFSUtil(theState,visited)    
                        roll_back(i,theState)                                       # WHEN WE FINISHED THE CURRENT RECURSION WE NEED TO GET BACK TO THE PREVIOUS STATE
                        theState.animated()                                         # DRAW THE OLD MOVE
                    else:
                        roll_back(i,theState)                                       #SINCE WE TRIED TO MOVE BEFORE CHECK VISITED, WE HAVE TO REVERSE IT
            return False

def roll_back(i,theState):
    if i=="left":
        theState.movement("right")
    elif i=="right":
        theState.movement("left")
    elif i=="up":
        theState.movement("down")
    elif i=="down":
        theState.movement("up")