from pymaze import maze, COLOR, agent
m = maze(10, 10)
m.CreateMaze()
# a = agent(m, filled = True, footprints=True)
# b = agent(m, 100, 1, filled = True, footprints=True, color = 'red')
# m.tracePath({a: m.path, b: m.path}, delay = 100)
# m.tracePath({b: m.path}, delay = 100)
m.run()