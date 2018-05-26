class Food(object):
    
    def __init__(self, num):
        self.num = num
        self.foods = []
        for foods in range(self.num):
            food = PVector(random(width), random(height))
            self.foods.append(food)
        
    def run(self):
        rectMode(CENTER)
        fill(0, 0, 255)
        for food in self.foods:
            rect(food.x, food.y, 5, 5)
        
        if random(1) < 0.005:
            self.newFood(PVector(random(width), random(height)))
    
    def newFood(self, loc):
        food = PVector(loc.x, loc.y)
        self.foods.append(food)
