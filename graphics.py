import pygame 
import sys
import time
from pygame.locals import *
import time
   
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 800
WINDOW_WIDTH =800


def main(state):
    global SCREEN, CLOCK
    WINDOW_HEIGHT=state.size*50
    WINDOW_WIDTH=state.size*50
    if WINDOW_WIDTH < 200 :
        WINDOW_WIDTH=200
    pygame.init()
    time.sleep(0.1)
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    pygame.display.set_caption(str(state.size)+" puzzle")
    #while True:
    drawGrid(state)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


def drawGrid(state):
    blockSize = state.size #Set the size of the grid block
    for x in range(0,blockSize):
        for y in range(0,blockSize):
            rect = pygame.Rect(x*50, y*50,50, 50)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
            if state.cell[x][y]!=0:
                SCREEN.blit(pygame.font.SysFont('Ariel', 35).render(str(state.cell[x][y]), True, WHITE), (x*50+20, y*50+20))

