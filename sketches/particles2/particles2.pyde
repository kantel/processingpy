from particlesystem import ParticleSystem

systems = []

def setup():
    size(640, 480)
    this.surface.setTitle("Partikelsysteme 2")

def draw():
    background(235)
    for ps in systems:
        ps.addParticle()
        ps.run()

def mousePressed():
    systems.append(ParticleSystem(PVector(mouseX, mouseY)))
