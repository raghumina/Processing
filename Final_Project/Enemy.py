
# two type of enemy 
# Red and black

# red once will appear from x axis 
# red once will be slow 
# They are more in number claim one life once touched 

# Can add other random ball 

# black will appear from y axis 
# They will be faster 
# less in number but more deadly can claim 2 life once touched 


# speed, attack, deathTime, number_of_enemy, axis from which they attack, color, size, fall speed, position 
# effect on death 

#Screen Variable
ballFallSpeedFactor = 1.3
screenHeight = 100
screenWidth = 200

class Enemy(object):
    def __init__(self, positionX, positionY, damage, sizeHeight, sizeWidth, speed, health):
        self.positionX = positionX
        self.positionY = positionY
        self.damage = damage
        self.sizeHeight = sizeHeight
        self.sizeWidth = sizeWidth
        self.speed = speed
        self.ballSF = ballFallSpeedFactor # ball speed factor 
        self.isDead = False
        self.health  = 5 
        self.size = random(30, 60)
        self.speedH = 4
        self.radius = 40
    def move(self, screenHeight):
        pass

            
        
    def death(self):
        pass
        
    def Ehealth(self):
        pass
 
 
    def draw(self):
        pass
  
        

        
        
        
     
         
                 
