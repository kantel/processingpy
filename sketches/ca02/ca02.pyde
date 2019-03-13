GRID_W = 101
GRID_H = 101
N_GENERATIONS = 48

generation = 0

class Cell():
    
    def __init__(self, c, r, state = 0):
        self.c = c
        self.r = r
        self.state = state
    
    def display(self):
        if self.state == 1:
            fill(0)   # schwarz
        else:
            fill(255)   # weiß
        rect(sz*self.r, sz*self.c, sz, sz)
    
    def check_neighbors(self, clist):
        if self.state == 1: return(1)
        neighbs = 0
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            try:
                if clist[self.r + dr][self.c + dc].state == 1:
                    neighbs += 1
            except IndexError:
                continue
        if neighbs in [1, 3]:
            return(1)
        else:
            return(0)

def setup():
    global sz, cellList
    size(600, 600)
    this.surface.setTitle("CA 2")
    sz = width//GRID_W + 1
    cellList = createCellList()
    frameRate(5)

def draw():
    global generation, cellList
    cellList = update(cellList)
    for row in cellList:
        for cell in row:
            cell.display()
    generation += 1
    if generation == N_GENERATIONS:
        noLoop()
        # generation = 1
        # cellList = createCellList()

def createCellList():
    sz = width // GRID_W + 1
    newList = []
    for j in range(GRID_H):
        newList.append([])
        for i in range(GRID_W):
            newList[j].append(Cell(i, j, sz))
    newList[GRID_H // 2][GRID_W // 2].state = 1
    return(newList)

def update(cList):
    newList = []
    for r, row in enumerate(cList):
        newList.append([])
        for c, cell in enumerate(row):
            newList[r].append(Cell(c, r, cell.check_neighbors(cList)))
    return(newList[::])
