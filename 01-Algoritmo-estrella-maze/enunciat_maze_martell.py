import time
import pyamaze as maze
from queue import PriorityQueue


# inicio maze bottom-right - final top-left
# (1,1) > row/col, dentro de maze.map hay las posiciones
# 1 abierto, 0 cerrado
# fila -> celda (no es array 1 es 1 no 0)
# before: 0.11550378799438477 -> 0.08526206016540527

ROWS = 50
COLS = 50
# ROWS = 35
# COLS = 35
m=maze.maze(ROWS,COLS)
m.CreateMaze()
# m.CreateMaze(loadMaze='maze_2.csv')

def distance(cell1, cell2):  
   x1, y1 = cell1
   x2, y2 = cell2 

   return abs(x1 - x2) + abs(y1 - y2)

def get_next_direction(direction, cell):
   row, col = cell
   if direction == 'E':
      return (row, col + 1) 
   if direction == 'W':
      return (row, col - 1) 
   if direction == 'S':
      return (row + 1, col) 
   if direction == 'N':
      return (row - 1, col) 

def next_direction_is_inside_grid(cell):
   row, col = cell

   return row > 0 and row <= m.rows and col > 0 and col <= m.cols
    

def aStar(m):
   HAMMER_VALUE = 10
   start = (1,1)
   end = (m.rows, m.cols)

   priority_queue = PriorityQueue()
   priority_queue.put((0 + distance(start, end), start))
   traveled_distance = { cell: float("inf") for cell in m.grid }
   traveled_distance[start] = 0
   where_do_i_come = {} # donde estoy / de donde vengo
   forward_path = {}
   hammer_points = []

   while not priority_queue.empty():
      priority_queue_el = priority_queue.get()
      current = priority_queue_el[1]
      current_distance = priority_queue_el[0]

      # if (current_distance > traveled_distance[end]):
      #    break


      for direction in 'WENS':
         if m.maze_map[current][direction] == True:
            next = get_next_direction(direction, current) 
            
            if (traveled_distance[next] > traveled_distance[current] + 1):
               traveled_distance[next] = traveled_distance[current] + 1


               if (next in hammer_points):
                  hammer_points.remove(next)

               where_do_i_come[next] = current
               priority_queue.put((traveled_distance[next] + distance(next, end), next))
         else: 
            next = get_next_direction(direction, current)

            if (next_direction_is_inside_grid(next) and (traveled_distance[next] > traveled_distance[current] + HAMMER_VALUE)):
               traveled_distance[next] = traveled_distance[current] + HAMMER_VALUE
               where_do_i_come[next] = current
               priority_queue.put((traveled_distance[next] + distance(next, end), next))
               hammer_points.append(next)
               
      



   cell = end
   hammers_used = 0
   count = 0

   while cell != start:
      count +=1
      if (cell in hammer_points):
         hammers_used += 1
      forward_path[cell] = where_do_i_come[cell]
      cell = where_do_i_come[cell]

   print(count)
   return forward_path

#

# - diccionario de donde vengo
# - inicializar la pq con el valor START (con la distancia inicial que es 0)
# - miras las coordenada y ase las sumas o restas al current 

# si el get de la pq la distancia recorrida + lo que me falta por recorrer es más grande que el goal es que

# comprobar siempre la distancia recorrida comparando con el goal pq.get()[0] + distancia que me queda > que la distancia que hay en el diccionario de DR del goal, True == 1


pre_Astar = time.time()
path = aStar(m)

post_Astar = time.time()
print(post_Astar - pre_Astar)
a=maze.agent(m,footprints=True)
m.tracePath({a:path},delay=5)
m.run()

