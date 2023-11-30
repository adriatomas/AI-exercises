import pygame
import sys
from queue import PriorityQueue
from time import sleep



BLOCK_SIZE = 20
WIDTH=400
HEIGHT=400
ROWS= int(HEIGHT/BLOCK_SIZE)
COLS= int(WIDTH /BLOCK_SIZE)

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (24, 210, 74)
PURPLE = (141, 57, 166)
RED = (247, 12, 12)
CYAN = (78, 235, 249)

TRAVELED_LIST = {}
BARRIERS = {}

INIT = None
GOAL = None
END= (int(WIDTH/BLOCK_SIZE), int(HEIGHT/BLOCK_SIZE))

FROM_WHERE_I_COME = {}
click = pygame.time.Clock()
    
# como pintar un cuadrado: pygame.draw.rect(screen, BLACK, (0, 0, BLOCK_SIZE, BLOCK_SIZE)) (SCREEN, COLOR, (X, Y, WIDTH, HEIGHT))
# x y

def distance(cell1, cell2):  
   x1, y1 = cell1
   x2, y2 = cell2 

   return abs(x1 - x2) + abs(y1 - y2)

def drawGrid(screen):
  for column in range(ROWS):
   for row in range(COLS): 
      pygame.draw.line(screen, BLACK, (0, column * BLOCK_SIZE), (WIDTH, column * BLOCK_SIZE))
      pygame.draw.line(screen, BLACK, (row * BLOCK_SIZE, 0), (row * BLOCK_SIZE, WIDTH))
def createGrid(screen):
  for column in range(ROWS):
   for row in range(COLS): 
      TRAVELED_LIST[(row, column)] = float('inf')
  
def printCell(screen, cell, color=BLACK):
  x, y = cell
  pygame.draw.rect(screen, color, ((x * BLOCK_SIZE) +1, (y * BLOCK_SIZE) + 1, BLOCK_SIZE-1, BLOCK_SIZE-1))

def trackNextPosition(next, current, priorityQueue):
  if (TRAVELED_LIST[next] > TRAVELED_LIST[current] + 1):
    FROM_WHERE_I_COME[next] = current
    TRAVELED_LIST[next] = TRAVELED_LIST[current] + 1
    priorityQueue.put((TRAVELED_LIST[next] + distance(next, GOAL), next))
  # else:
    # printCell(screen, next, RED)

def startAlgorithm():
  priorityQueue = PriorityQueue()
  priorityQueue.put((0 + distance(INIT, GOAL), INIT))
  TRAVELED_LIST[INIT] = 0

  while not priorityQueue.empty():
    current = priorityQueue.get()[1]

    # printCell(screen, current, GREEN)
    row, col = current
    next = None
    if goGoNext(row, col + 1) == True:
      next = (row, col + 1) 
      trackNextPosition(next, current,priorityQueue)

    if goGoNext(row, col - 1) == True:
      next = (row, col - 1)
      trackNextPosition(next, current,priorityQueue)

    if goGoNext(row + 1, col) == True:
      next = (row + 1, col)
      trackNextPosition(next, current,priorityQueue)

    if goGoNext(row - 1, col) == True:
      next = (row - 1, col)
      trackNextPosition(next, current,priorityQueue)
  
  cell = GOAL
  path = {}
  while cell != INIT:
     path[cell] = FROM_WHERE_I_COME[cell]
     cell = FROM_WHERE_I_COME[cell]
  
  return path
      
def goGoNext(row, col):
  row_edge, col_end = END
  return (row, col) not in BARRIERS and row < row_edge and col < col_end and col >= 0 and row >= 0

def printAndSetGoal(cell):
  global GOAL
  x, y = cell
  row, col = int(x / BLOCK_SIZE), int(y / BLOCK_SIZE)
  printCell(screen, (row, col), CYAN)
  GOAL = (row, col)

def printAndSetInit(cell):
  global INIT
  x, y = cell
  row, col = int(x / BLOCK_SIZE), int(y / BLOCK_SIZE)
  printCell(screen, (row, col), PURPLE)
  INIT = (row, col)

def printAndSetBarrier(cell):
  x, y = cell
  row, col = int(x / BLOCK_SIZE), int(y / BLOCK_SIZE)
  printCell(screen, (row, col))
  BARRIERS[(row, col)] = (row, col)



def main():
  pygame.init()
  global screen
  global INIT
  global GOAL
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  clock = pygame.time.Clock()
  running = True
  screen.fill(WHITE)
  clickCounter = 0
  path = {}
  createGrid(screen)
  while running:
      # poll for events
      # pygame.QUIT event means the user clicked X to close your window

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
          if event.type == pygame.MOUSEBUTTONUP:
            clickCounter +=1
            if clickCounter == 1: 
              printAndSetInit(event.pos)
            elif clickCounter == 2:   
              printAndSetGoal(event.pos)
            else:
              printAndSetBarrier(event.pos)
          if event.type == pygame.MOUSEMOTION and clickCounter > 2:
              if pygame.mouse.get_pressed()[0]:
                printAndSetBarrier(event.pos)

              

            # if pygame.mouse.get_pressed(3):
            #   print('mouse up, pressed 2')
          # if event.type == pygame.MOUSEMOTION:
          #     row , col = event.pos
          #     printCell(screen, (int(row / BLOCK_SIZE), int(col / BLOCK_SIZE)))
          screen.fill((0, 20, 20))
      
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_RETURN:
                path = startAlgorithm()

          for r in range(COLS):
            for c in range(ROWS):
              # sleep(0.4)
              cell = (r,c)
              printCell(screen, cell, WHITE)
              if (cell in path):
                printCell(screen, cell, GREEN)
              elif TRAVELED_LIST[cell] != float('inf') and TRAVELED_LIST[cell] not in path:
                printCell(screen, cell, RED)
              elif cell == GOAL:
                  printCell(screen, cell, CYAN)
              elif cell == INIT:
                  printCell(screen, cell, PURPLE)
              elif cell in BARRIERS:
                  printCell(screen, cell, BLACK)


                
  

      # fill the screen with a color to wipe away anything from last frame


      # # RENDER YOUR GAME HERE
    
      # #set init
      # printCell(screen, INIT, BLACK)
      # #set goal
      # printCell(screen, GOAL, RED)
      # path = startAlgorithm()
      # for index, cell in enumerate(path):
      #    if index > 0:
      #     printCell(screen, cell, PURPLE)



      # flip() the display to put your work on screen
      pygame.display.flip()

      # clock.tick(60)  

  pygame.quit()
  sys.exit()

main()


