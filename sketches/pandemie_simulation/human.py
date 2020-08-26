from random import randint

class Human:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.state = 0          # State: 0 = normal, 1 = infected, 2 = recovered, 3 = dead
        self.time_to_cure = 2000
        self.chance_to_die = 0.25
        self.movement_rate = 3
    
    def update(self):
        if self.state != 3:      # Only move if not dead
            x_old = self.x       # Store last x position
            y_old = self.y       # Store last y position
            self.x += randint(-self.movement_rate, self.movement_rate)
            self.y += randint(-self.movement_rate, self.movement_rate)
            # Check border
            if (self.x <= self.radius or self.x >= width - self.radius):
                self.x = x_old   # Back to the old x position     
            if (self.y <= self.radius or self.y >= height - self.radius):
                self.y = y_old   # Back to the old y position
            if self.state == 1:  # Only reduce time_to_cure if infected
                self.time_to_cure -= 1
        if self.state == 1 and self.time_to_cure <= 1:  # Recover or die
            if random(1.0) > self.chance_to_die:
                self.state = 2   # Recover
            else:
                self.state = 3   # Die
    
    def show(self):
        stroke(255)
        if self.state == 3:
            noFill()             # Dead, white ring
        elif self.state == 2:
            fill(0, 200, 0)      # Recoverd, green circle
        elif self.state == 1:
            fill(200, 0, 0)      # Infected, red circle
        else:
            fill(255)            # Normal, white circle
        circle(self.x, self.y, 2*self.radius)

    def collision(self, other):
        if self != other:
            distance = dist(self.x, self.y, other.x, other.y)
            if distance <= self.radius + other.radius:
                # One object must be infected and one object must be normal
                if self.state == 1 and other.state == 0:
                    other.state = 1  # Set the normal to infected
                elif self.state == 0 and other.state == 1:
                    self.state == 1  # Set the normal to infected
