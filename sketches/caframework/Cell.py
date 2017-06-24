class Cell():
    
    def __init__(self, ex, why):
        self.x = ex*cellSize
        self.y = why*cellSize
        if random(2) > 1:
            self.nexState = True
        else:
            self.nextState = False
        self.state = self.nextState