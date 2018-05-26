from bloop import Bloop
from dna import DNA
from food import Food

class World(object):
        
    def __init__(self, num):
        self.num = num
        self.food = Food(num)
        self.bloops = []
        for i in range(num):
            loc = PVector(random(width), random(height))
            dna = DNA()
            self.bloops.append(Bloop(dna, loc))
            
        
            

    def run(self):
        self.food.run()
        
        for i in range(len(self.bloops) - 1, -1, -1):
            self.bloops[i].run()
            self.bloops[i].eat(self.food.foods)
            if self.bloops[i].isDead():
                self.food.newFood(self.bloops[i].location)
                self.bloops.pop(i)
            
            if random(1) < 0.001:
                child = self.bloops[i].reproduce()
                self.bloops.append(child)
