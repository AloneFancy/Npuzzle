#!/usr/bin/python3
import sys
from puzzle import *
from state import *
from stackDFS import *

def main():
	N="sdsad"
	while(not isinstance(N,int)):
		try:
			N = int(input("Please choose the size for your puzzle:"))
		except ValueError:
			print("Please input an integer.")
	Npuzzle= State(N)
	Npuzzle.perfect_random()
	Npuzzle.terminal_display()
	Npuzzle.animated()
	#DFS(Npuzzle)
		

if __name__=='__main__':
    	main()
	
