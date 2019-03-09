from shaun import Sheep, Settings

shaun = Sheep(300, 200)
s = Settings()

def setup():
    size(s.WIDTH, s.HEIGHT)
    this.surface.setTitle("Shaun das Schaf (1)")
    frameRate(s.FPS)
    
def draw():
    background(s.GREEN)
    shaun.update()
