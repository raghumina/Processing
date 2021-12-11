

from Enemy import Enemy 

class HEnemy(Enemy):
    

    def move(self, screenWidth):
        self.positionX = self.positionX + (self.speedH)
        if self.positionX > (screenWidth - self.radius):
            self.death()
            
            
        
    def death(self):
        self.isDead = True
        
    def Ehealth(self):
        return self.health
 
    def draw(self):
        m = millis()
        noStroke()
        fill(m % 225, 125 ,125)
        square(self.positionX, self.positionY, self.size)
        # circle(self.positionX, self.positionY, self.size)
        print("enemy")
