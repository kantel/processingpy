from fish import Fish
from pipes import Pipe

fluffyFish = Fish()
pipes = []

def setup():
    size(640, 320)
    fluffyFish.loadPic()
    pipe = Pipe()
    pipes.append(pipe)
    
def draw():
    background(0, 153, 204)
    
    for i in range(len(pipes) - 1, -1, -1):
        if pipes[i].offscreen():
            pipes.pop(i)
    # print(str(len(pipes)))
        if pipes[i].collidesWith(fluffyFish):
            pipes[i].hilite = True
        else:
            pipes[i].hilite = False
        pipes[i].update()
        pipes[i].display()


    fluffyFish.update()
    fluffyFish.display()
    
    
    if (frameCount % 100 == 0):
        pipe = Pipe()
        pipes.append(pipe)
    

def keyPressed():
    if (key == " "):
        # print("SPACE")
        fluffyFish.up()
