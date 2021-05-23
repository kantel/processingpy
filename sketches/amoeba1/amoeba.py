class Amoeba():
    
    def __init__(self, _x, _y, _diameter, _x_speed, _y_speed):
        self.location = PVector(_x, _y)
        self.propulsion = PVector(_x_speed, _y_speed)
        self.d = _diameter
        self.nucleus = {
                        "fill": color(random(20, 250), random(20, 250), random(20, 250)),
                        "x": self.d*random(-0.15, 0.15),
                        "y": self.d*random(-0.15, 0.15),
                        "d": self.d/random(2.5, 4)
                        }
        
    def update(self):
        self.location += self.propulsion
        r = self.d/2
        if (self.location.x + r > width) or (self.location.x - r < 0):
            self.propulsion.x *= -1
        if (self.location.y + r > height) or (self.location.y - r < 0):
            self.propulsion.y *= -1
        
    def show(self):
        # nucleus
        fill(self.nucleus["fill"])
        noStroke()
        circle(self.location.x + self.nucleus["x"], self.location.y + self.nucleus["y"], self.nucleus["d"])
        # cell membrane
        fill(234, 218, 184, 50)
        stroke(255, 255, 255)
        strokeWeight(3)
        r = self.d/2.0
        cpl = r*0.55
        cpx, cpy = self.circle_point(frameCount/(r/2), r/8)
        xp, xm = self.location.x + cpx, self.location.x - cpx
        yp, ym = self.location.y + cpy, self.location.y - cpy
        with beginShape():
            vertex(self.location.x, self.location.y - r)                        # top vertex
            bezierVertex(xp + cpl, yp - r, xm + r, ym - cpl,
                         self.location.x + r, self.location.y)                  # right vertex
            bezierVertex(xp + r, yp + cpl, xm + cpl, ym + r,
                         self.location.x, self.location.y + r)                  # bottom vertex
            bezierVertex(xp - cpl, yp + r, xm - r, ym + cpl,
                         self.location.x - r, self.location.y)                  # left vertex
            bezierVertex(xp - r, yp - cpl, xm - cpl, ym - r,
                         self.location.x, self.location.y - r)                  # back to top vertex
    
    def circle_point(self, theta, rho):
        x = cos(theta)*rho
        y = sin(theta)*rho
        return[x, y]
