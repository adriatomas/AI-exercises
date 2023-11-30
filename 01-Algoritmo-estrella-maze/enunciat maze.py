import time
import pyamaze as maze
from queue import PriorityQueue


# inicio maze bottom-right - final top-left
# (1,1) > row/col, dentro de maze.map hay las posiciones
# 1 abierto, 0 cerrado
# fila -> celda (no es array 1 es 1 no 0)
# before: 0.11550378799438477 -> 0.08526206016540527

ROWS = 200
COLS = 200
# ROWS = 35
# COLS = 35
m=maze.maze(ROWS,COLS)
# m.CreateMaze()
m.CreateMaze(loadMaze='maze_2.csv')

def distance(cell1, cell2):  
   x1, y1 = cell1
   x2, y2 = cell2 

   return abs(x1 - x2) + abs(y1 - y2)
    

def aStar(m):
   start = (1,1)
   end = (m.rows, m.cols)

   priority_queue = PriorityQueue()
   priority_queue.put((0 + distance(start, end), start))
   traveled_distance = { cell: float("inf") for cell in m.grid }
   traveled_distance[start] = 0
   where_do_i_come = {} # donde estoy / de donde vengo
   forward_path = {}

   while not priority_queue.empty():
   # current = priority_query.get()[1] -> (1,1)
      # priority_queue.
      priority_queue_el = priority_queue.get()
      current = priority_queue_el[1]
      current_distance = priority_queue_el[0]
      # current = priority_queue.get()[1]


      if (current_distance > traveled_distance[end]):
         break


      for direction in 'WENS':
         if m.maze_map[current][direction] == True:
            row, col = current
            if direction == 'E':
               next = (row, col + 1) 
            if direction == 'W':
               next = (row, col - 1) 
            if direction == 'S':
               next = (row + 1, col) 
            if direction == 'N':
               next = (row - 1, col) 
            
            if (traveled_distance[next] > traveled_distance[current] + 1):
               traveled_distance[next] = traveled_distance[current] + 1
               where_do_i_come[next] = current
               priority_queue.put((traveled_distance[next] + distance(next, end), next))

   cell = end
   count = 0
   while cell != start:
      count += 1
      forward_path[cell] = where_do_i_come[cell]
      cell = where_do_i_come[cell]
   print(count)
   return forward_path

#

# - diccionario de donde vengo
# - inicializar la pq con el valor START (con la distancia inicial que es 0)
# - miras las coordenada y ase las sumas o restas al current 

# si el current+1 < que el next se ha encontrado un camino mejor y substituto el next con el current + 1 y se añade el punto a la PriorityQueue


# si el get de la pq la distancia recorrida + lo que me falta por recorrer es más grande que el goal es que

# comprobar siempre la distancia recorrida comparando con el goal pq.get()[0] + distancia que me queda > que la distancia que hay en el diccionario de DR del goal, True == 1


pre_Astar = time.time()
path = aStar(m)

post_Astar = time.time()
print(post_Astar - pre_Astar)
a=maze.agent(m,footprints=True)
m.tracePath({a:path},delay=5)
m.run()

