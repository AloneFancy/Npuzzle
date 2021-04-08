#!/usr/bin/python3
import random
import os
import time
import sys

def swap(cell,ax,ay,bx,by):
	cell[ax][ay],cell[bx][by] = cell[bx][by],cell[ax][ay]	
class State:
	def __init__(self,N):
		self.size=N
		self.cell = [[0 for x in range(N)] for y in range(N)]
		self.empty_cell=[self.size-1,self.size-1	] 
	def random(self):
		self.pool=[i for i in range (1,self.size*self.size)]
		for col in range(0,self.size):
			for row in range(0,self.size):
				if not self.pool:
					self.cell[row][col]=0
					break
				self.cell[col][row] = random.choice(self.pool)
				self.pool.remove(self.cell[col][row])

	def check_illegal(self,move,col,row):
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
		""" Check if we get to final state"""
		for row in (0,self.size):
			for col in (0,self.size):
				if ((row==self.size-1) and (col==self.size-1)) :
					continue
				else :
					if (self.cell[col][row]!=col*self.size+row):
						return False		
		return True

	def terminal_display(self):
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

	def animated_on_terminal(self):	
		while(True):
			self.terminal_display()	
			time.sleep(0.5)


#test=State(4)
#test.random()
#test.animated_on_terminal()

