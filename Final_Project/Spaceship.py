

'''

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


def setup():
    
    global bullet, isFiring
    background(0)
    size(1000, 1000)
    
    # isFiring = True
    
    
def draw():
    background(0)
    # if keyPressed == 'G' or keyPressed == 'g':
    #     fireBullets()

    spaceShip()
    drawBullets()
    
    
def spaceShip():
    global bullet
    
    squarePosX = mouseX
    squarePosY = mouseY
    
    if keyPressed: 
        if key == 'G' or key == 'g':
            print ("fire G")
            bullet.append(PVector(squarePosX, squarePosY))
    m = millis()
    noStroke()
    fill(m % 255, 255 ,25)
    square(squarePosX, squarePosY, 50)
    
def drawBullets():
    global bullet, isFiring, bulletFiringStartTime, bulletTimer, bulletRateOfFire, bulletBurst, bulletBurstCounter, bulletSpeed

    bCounter = 0
    for b in bullet:
        
        # is b colliding with some enemy        
        
        b.y = b.y + bulletSpeed
        fill(255)        
        circle(b.x, b.y, 4)
        
    # draw all bullets

def createBullet():
    global bullet
    # bulletCountTillNow = bullet.count + 1

    bullet.append(1)
    print ("creating bullet")
   
def fireBullets():
    global isFiring, bulletFiringStartTime, bulletTimer, bulletBurstCounter
    isFiring = True
    bulletFiringStartTime = millis()
    bulletTimer = millis()
    bulletBurstCounter = 0
    
    print ("Firing bullets")
    
    
def stopFiringBullets():
    global isFiring, bulletFiringStartTime, bulletTimer, bulletBurstCounter
    isFiring = False
    bulletFiringStartTime = 0
    bulletTimer = 0
    bulletBurstCounter = 0
    
    print ("Stop firing bullets")
    
    
'''
    
