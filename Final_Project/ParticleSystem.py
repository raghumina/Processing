
from Particle import Particle

class ParticleSystem(object):
    def __init__(self, n, position):
        self.particles = [Particle(position) for _ in range(n)]
        
    def draw(self):
        for p in self.particles:
            p.draw()

    def update(self):
        for p in self.particles:
            p.update()
    
    
