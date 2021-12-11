

# Class for partices 


class Particle(object):
    def __init__(self, position):
        self.gravity = PVector(0, .001)
        #self.position = position
        self.position = PVector(position.x, position.y)
        self.lifespan = 100
        self.velocity = PVector(random(-1, 1.5), random(-2, 0))
        #print(self.velocity)
        self.size = random(10, 30)
      #  print(self.size)
        
    def updatePos(self):
        self.position.x = ( self.position.x) + (self.velocity.x)
        self.position.y = ( self.position.y) + (self.velocity.y)
        
    def isDead(self):
        return self.lifespan < 0

    def update(self):
        self.lifespan -= 1
       # self.velocity.add(self.gravity)
       # self.setTint(color(255, self.lifespan))
        self.updatePos()
       
    def draw(self):
        fill(color(255, 255,255, self.lifespan))
        circle(self.position.x, self.position.y, self.size)

    
