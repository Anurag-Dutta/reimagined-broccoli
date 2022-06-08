# A typical 5 x 5 maze

# (1, 1)    (1, 2)    (1, 3)    (1, 4)    (1, 5)
# (2, 1)    (2, 2)    (2, 3)    (2, 4)    (2, 5)
# (3, 1)    (3, 2)    (3, 3)    (3, 4)    (3, 5)
# (4, 1)    (4, 2)    (4, 3)    (4, 4)    (4, 5)
# (5, 1)    (5, 2)    (5, 3)    (5, 4)    (5, 5)

from pymaze import maze, COLOR, agent
# Movement: W -> N -> S -> E
def DFS(m):
    start = (m.rows, m.cols)
    explored = [start]
    frontier = [start]
    dfspath = {}
    while len(frontier) > 0:
        currrent_cell = frontier.pop() # Popping from the end, LIFO Strategy
        if currrent_cell == (1, 1):
            break
        for d in 'ESNW':
            if m.maze_map[currrent_cell][d] == True:
                if d == 'E':
                    child = (currrent_cell[0], currrent_cell[1] + 1) # 'x' coordinate remains same, while 'y' coordinate increases by one
                elif d == 'S':
                    child = (currrent_cell[0] + 1, currrent_cell[1]) # 'x' coordinate increases by one, while 'y' coordinate remains same
                elif d == 'N':
                    child = (currrent_cell[0] - 1, currrent_cell[1]) # 'x' coordinate decreases by one, while 'y' coordinate remains same
                elif d == 'W':
                    child = (currrent_cell[0], currrent_cell[1] - 1) # 'x' coordinate remains same, while 'y' coordinate decreases by one
                if child in explored:
                    continue
                explored.append(child)
                frontier.append(child)
                dfspath[child] = currrent_cell
    fwdpath = {}
    cell = (1, 1)
    while cell != start:
        fwdpath[dfspath[cell]] = cell
        cell = dfspath[cell]
    return fwdpath
m = maze(100, 100)
m.CreateMaze()
path = DFS(m)
a = agent(m, filled = True, footprints=True)
m.tracePath({a: m.path}, delay = 10)
m.run()