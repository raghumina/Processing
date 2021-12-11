# FINAL GAME 
# INSTRUCTOR: ZAC EMERZIAN 
# SUBMITED BY: RAGHU MINA 

# THIS GAME IS A SPACE SHIP SHOOTER GAME BASED ON SPACE WAR 
# HERE PLAYER CONTROLS A SPACE SHIP HE HAVE TO SHOOT OTHER OBJECTS IN SPACE AFTER EACH SHOOT HE WILL GET SCORE 
# PLAYER CAN TRY TO CREATE HIGH SCORE 


# CONTROLS ARE SIMPLE PLAYE CONTROLS THE SHIP WITH THE HELP OF MOUSE AND SHOOT BULLETS WITH MOUSE PRESS 


#Screen Variable
ScreenHeight = 800
ScreenWidth = 1200

#score and Life variable
score = 0
Life = 10

ballRadius = 40
ballFallSpeedFactor = 1.3
ballsStartingY = 50


# Unique for each ball 
ballsFallSpeed = [1, 2, 3, 4]
ballsPosX = [120, 240, 360, 480]
ballsPosY = [60, 60, 60, 60]
ballsColor = [color(255,255, 120)]

# ENEMY VARIABLES 
VEnemies = []
HEnemies = [] 

# Game Variables 
gamestate = 1       # 1 state  = menue, 2nd = play, 3rd = end 
gamescore = 0
gamelevel = 1
gametime = 0


# BULLET varaible
bullet = []
bulletBurst = 4 # number of shots fired
bulletRateOfFire = 120 # bullets per minute
isFiring = False
bulletBurstCounter = 0
bulletTimer = 0.0
bulletFiringStartTime = 0.0
bulletSpeed = 3
bulletWidth = 6
BulletHeight = 7
bulletSpeed = -5

hEnemyTimer = 4000
hEnemyNextTime = 0
vEnemyTimer = 1000
vEnemyNextTime = 0

from HEnemy import HEnemy
from VEnemy import VEnemy
from Particle import Particle
from ParticleSystem import ParticleSystem
def setup():
    global gamestate,  EnemyClass, ps

    background(0)
    size(ScreenWidth, ScreenHeight)
    
    createHEnemy()
    createVEnemy()
    
    position = PVector(500, 500)
    ps = ParticleSystem(100, position)

def draw():
    global  ScreenHeight, HEnemies, VEnemies, enemy, ps
    background(5)
    drawGame()
    spaceShip()
    createHEnemy()
    createVEnemy()
    drawBullets()
    ps.update()
    ps.draw()
    
    for enemy in VEnemies:
        enemy.draw()
        enemy.move(ScreenHeight)
        
    for enemy in HEnemies:
        enemy.draw()
        enemy.move(ScreenHeight)
        
    
def spaceShip():
    global bullet
    
    squarePosX = mouseX
    squarePosY = mouseY
    
    if mousePressed: 
        
            print ("fire G")
            bullet.append(PVector(squarePosX, squarePosY))
    m = millis()
    noStroke()
    fill(m % 255, 255 ,25)
    square(squarePosX, squarePosY, 30)
    
    
      # Print the game score
    textSize(40)
    text("Score: ",5, 50) 
    text(gamescore, 120, 50)

def createHEnemy():
    global hEnemyNextTime, hEnemyTimer
    
    if millis() > hEnemyNextTime:
        HEnemies.append(HEnemy(random(0, 100), random(20, 200), 5, 60, 60, 1, 10))        
        hEnemyNextTime = millis() + hEnemyTimer
    
def createVEnemy():
    global vEnemyNextTime, vEnemyTimer
    
    if millis() > vEnemyNextTime:  
        VEnemies.append(VEnemy(random(0, 1200), 10, 5, 60, 60, 1, 10))
        vEnemyNextTime = millis() + vEnemyTimer
    
def drawBullets():
    global bullet, bulletSpeed
    fill(255)        

    for b in bullet:
        b.y = b.y + bulletSpeed
        circle(b.x, b.y, 4)

def createBullet():
    global bullet
    bullet.append(1)
    print ("creating bullet")

def drawGame():
    global ballsColor
    global ballsPosY
    global barPosX, barPosY
    global gamescore, gamelevel, ballFallSpeedFactor, ballsFallSpeed, gamestate
   # global b.x, b.y
    
    for i in range(len(ballsPosY)):
        ballsPosY[i] = ballsPosY[i] + (ballsFallSpeed[i] * ballFallSpeedFactor)
        
        for b in bullet:
            # Collision check of bullet with enemy 
            if (ballsPosX[i] > (b.x - ballRadius) and ballsPosX[i] < (b.x + ballRadius)) and \
             (ballsPosY[i] > b.y - ballRadius and ballsPosY[i] < b.y + ballRadius):
                
                # for score 
                gamescore = gamescore + 1
                ballsPosY[i] = ballsStartingY
                ballsPosX[i] = random(0, 1200)

     
         # Ball falling of the screen 
        if ballsPosY[i] > (ScreenHeight + ballRadius):
            # Apply -negative score
            # randomizeBallPosition()
            ballsPosY[i] = ballsStartingY
            ballsPosX[i] = random(0, 1200)
            # gamescore = gamescore - 1  # hight negative score so that stakes are high for the player :)
    
    for i in range(len(self.positionY)):
        self.positionY = self.positionY + (self.speed * self.ballSF)
        
     for b1 in bullet:
         if self.positionX > (b1.x - ballRadius) and self.positionX < (b1.x + ballRadius)) and \
         self.positionY > b1.y - ballRadius and self.positionY < b1.y + ballRadius):
            
                
                    
                        
                            
                                
                                    
                                        
                                            
                                                
                                                    
                                                            
    for i in range(len(ballsPosX)):
        fill(ballsColor[color(255, 255, 255)])
        circle(ballsPosX[i], ballsPosY[i], ballRadius)
    
def SpaceShipControl():
    pass
    
    
    
    
    

    
    
    



    
    
    
    
    
    
    
    
    
    
    
