# A typical 5 x 5 maze

# (1, 1)    (1, 2)    (1, 3)    (1, 4)    (1, 5)
# (2, 1)    (2, 2)    (2, 3)    (2, 4)    (2, 5)
# (3, 1)    (3, 2)    (3, 3)    (3, 4)    (3, 5)
# (4, 1)    (4, 2)    (4, 3)    (4, 4)    (4, 5)
# (5, 1)    (5, 2)    (5, 3)    (5, 4)    (5, 5)

from pymaze import maze, COLOR, agent
from queue import PriorityQueue

def h_of_x(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x2 - x1) + abs(y2 - y1) # Manhattan Distance
def AStar(m):
    # The heuristic function will be
    # f(x) = g(x) + h(x)
    # g(x) = Cost of the path from start node to x
    # h(x) = Cheapest path from x to goal
    start = (m.rows, m.cols)
    g_score={cell : float('inf') for cell in m.grid} # Assigning ∞ to each cell
    g_score[start] = 0
    f_score={cell : float('inf') for cell in m.grid} # Assigning ∞ to each cell
    f_score[start] = h_of_x(start, (1, 1))
    open = PriorityQueue()
    open.put((h_of_x(start, (1, 1)), h_of_x(start, (1, 1)), start)) # f_score(cell), h_score(cell), cell will be pushed in the priority Q
    astarpath = {}
    while not open.empty():
        currrent_cell = open.get()[2]
        if currrent_cell == (1, 1):
            break
        for d in 'ESNW':
            if m.maze_map[currrent_cell][d] == True:
                if d == 'E':
                    child = (currrent_cell[0], currrent_cell[1] + 1)  # 'x' coordinate remains same, while 'y' coordinate increases by one
                elif d == 'S':
                    child = (currrent_cell[0] + 1, currrent_cell[1])  # 'x' coordinate increases by one, while 'y' coordinate remains same
                elif d == 'N':
                    child = (currrent_cell[0] - 1, currrent_cell[1])  # 'x' coordinate decreases by one, while 'y' coordinate remains same
                elif d == 'W':
                    child = (currrent_cell[0], currrent_cell[1] - 1)  # 'x' coordinate remains same, while 'y' coordinate decreases by one

                temp_g_score = g_score[currrent_cell] + 1 # For each level the value of g(x) increases by 1
                temp_f_score = temp_g_score + h_of_x(child, (1, 1)) # as the heuristic function is f(x) = g(x) + h(x)
                if temp_f_score < f_score[child]: # If the cost found is less than what is present currently, modifiy the cost
                    g_score[child] = temp_g_score
                    f_score[child] = temp_f_score
                    open.put((temp_f_score, h_of_x(child, (1, 1)), child)) # Put it back to the Priority Q
                    astarpath[child] = currrent_cell # Update the path
    fwdpath = {}
    cell = (1, 1)
    while cell != start:
        fwdpath[astarpath[cell]] = cell
        cell = astarpath[cell]
    return fwdpath
m = maze(50, 50)
m.CreateMaze()
path = AStar(m)
a = agent(m, filled = True, footprints=True)
m.tracePath({a: m.path}, delay = 10)
m.run()