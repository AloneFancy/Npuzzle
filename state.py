#!/usr/bin/python3
import random
import os
import time
import sys
import graphics

def swap(cell,ax,ay,bx,by):
	cell[ax][ay],cell[bx][by] = cell[bx][by],cell[ax][ay]	
	"""
	Simply swap function?
	"""
class State:
	cell=[]
	def __init__(self,N):
		"""
		Init size, cells and empty cell coordinate for the state
		"""
		self.size=N
		self.cell = [[0 for x in range(N)] for y in range(N)]				
		self.empty_cell=[self.size-1,self.size-1] 
		sys.setrecursionlimit(1000000)

	def random(self):
		"""
			Literally random
		"""
		self.pool=[i for i in range (1,self.size*self.size)]
		for col in range(0,self.size):
			for row in range(0,self.size):
				if not self.pool:
					self.cell[row][col]=0
					break
				self.cell[col][row] = random.choice(self.pool)
				self.pool.remove(self.cell[col][row])

	def perfect_random(self):
		"""
			Randomize the game the way that can be solved by using random.choice
		"""
		for row in range(0,self.size):
			for col in range(0,self.size):
				self.cell[col][row]=row*self.size+col+1
		self.cell[self.size-1][self.size-1]=0
		move=['left','right','up','down']
		for i in range(0,1000)	:
			j=random.choice(move)
			if not self.check_illegal(j,self.empty_cell[0],self.empty_cell[1]):   
				self.movement(j)

	def check_illegal(self,move,col,row):
		"""
			Check the illegal move from input
		"""
		if move=='left' and col==0:
		 	return True
		elif move =='right' and col ==self.size-1:
		 	return True
		elif move =='down' and row==self.size-1:
		 	return True
		elif move=='up' and row ==0:
			return True
		return False

	def movement(self,move):
		"""
			Move Left Right Up Down and Set the coordinate of the empty cell
		"""
		if move=='left':
			swap(self.cell,self.empty_cell[0],self.empty_cell[1],self.empty_cell[0]-1,self.empty_cell[1])
			self.empty_cell[0]-=1			
		elif move =='right':
			swap(self.cell,self.empty_cell[0],self.empty_cell[1],self.empty_cell[0]+1,self.empty_cell[1])
			self.empty_cell[0]+=1
		elif move =='down' :
			swap(self.cell,self.empty_cell[0],self.empty_cell[1],self.empty_cell[0],self.empty_cell[1]+1)
			self.empty_cell[1]+=1
		elif move=='up' :
			swap(self.cell,self.empty_cell[0],self.empty_cell[1],self.empty_cell[0],self.empty_cell[1]-1)
			self.empty_cell[1]-=1
		
	def isGoal(self):
		""" Check if we get to final state.
			For example:
			col=0 row=1 => row(1)*2+col(0)+1=3
			-----
			|1|2|
			-----
			|3|0|
			-----
		"""
		for row in range(0,self.size):
			for col in range(0,self.size):
				if self.cell[col][row]==0:
					if ((row==self.size-1) and (col==self.size-1)) :
						return True
					else:
					 	return False
				else :
					if (self.cell[col][row]!=row*self.size+col+1):
						return False		
		return True

	def terminal_display(self):
		"""
			Display the puzzle on the terminal:
			-------------
			| 1 |   | 2 |
			-------------
			| 3 | 4 | 5 |
			-------------
			| 6 | 7 | 8 |
			-------------
		"""
		print(self.size*"------")
		for row in range (0,self.size):			
			print("|",end='', flush=True)
			for col in range(0,self.size):
				if (self.cell[col][row]!=0):
					print('{:3}'.format(self.cell[col][row]),end='', flush=True)
				else:
					print("   ",end='', flush=True)
				print("  |",end='', flush=True)
			print("\n"+self.size*"------", flush=True)

	def animated(self):	
		"""
		Call graphic module
		"""
		graphics.main(self)




#test=State(4)
#test.random()
#test.animated_on_terminal()

