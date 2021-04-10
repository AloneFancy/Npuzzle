#!/usr/bin/python3
import sys
from puzzle import *
from state import *

def main():
	N="sdsad"
	while(not isinstance(N,int)):
		try:
			N = int(input("Please choose the size for your puzzle:"))
		except ValueError:
			print("Please input an integer.")
	Npuzzle= State(N)
	Npuzzle.random()
	Npuzzle.terminal_display()
	Npuzzle.isGoal()
	DFS(Npuzzle)
		

if __name__=='__main__':
    	main()
	
