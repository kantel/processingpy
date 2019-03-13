from cell import Cell

GRID_W = 51
GRID_H = 51

def setup():
    global cellList
    size(600, 600)
    this.surface.setTitle("CA 1")
    cellList = createCellList()
    
def draw():
    for row in cellList:
        for cell in row:
            cell.display()

def createCellList():
    sz = width//GRID_W + 1
    newList = []
    for j in range(GRID_H):
        newList.append([])
        for i in range(GRID_W):
            newList[j].append(Cell(i, j, sz))
    newList[GRID_H//2][GRID_W//2].state = 1
    return(newList)
