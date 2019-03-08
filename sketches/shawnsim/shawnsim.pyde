from shawn import Sheep, Settings

shawn = Sheep(300, 200)
s = Settings()

def setup():
    size(s.WIDTH, s.HEIGHT)
    this.surface.setTitle("Shawn das Schaf (1)")
    frameRate(s.FPS)
    
def draw():
    background(s.GREEN)
    shawn.update()
