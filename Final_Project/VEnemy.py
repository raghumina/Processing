



# Class for vertical enemy 

from Enemy import Enemy 

class VEnemy(Enemy):
    
    def move(self, screenHeight):
        self.positionY = self.positionY + (self.speed * self.ballSF)
        if self.positionY > (screenHeight + self.radius):
            self.death()
            
            
        
    def death(self):
        self.isDead = True
        
    def Ehealth(self):
        return self.health
 
    def draw(self):
        m = millis()
        noStroke()
        fill(m % 225, 125 ,125)
        triangle(self.positionX - self.radius * 0.66, self.positionY + self.radius * 0.66, 
                 self.positionX, self.positionY - self.radius * 0.66, 
                 self.positionX + self.radius * 0.66, self.positionY + self.radius * 0.66) 
        # circle(self.positionX, self.positionY, self.size)
        print("enemy")
