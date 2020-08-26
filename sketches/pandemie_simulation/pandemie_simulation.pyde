from random import randint
from human import Human

num_humans = 100

humans = []

def setup():
    size(600, 600)
    this.surface.setTitle("Pandemie-Simulation")
    for _ in range(num_humans):
        humans.append(Human(randint(20, width - 20), randint(20, height - 20)))
    humans[randint(0, num_humans)].state = 1  # Patient 0

def draw():
    background(0)
    for human in humans:
        human.update()
        for other in humans:
            other.collision(human)
        human.show()
