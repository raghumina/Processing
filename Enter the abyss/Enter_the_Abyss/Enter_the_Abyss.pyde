#Payton Final Project
#Enter the Abyss
#Save your Fiance!
#BGM from Octopath Traveler(the battle theme II)
#A start the Game, Q restart the game


#how to make trap platform
#how to record level 


add_library("sound")

#About Triangle Spike on the top---------------------------
triPos=[]
triColor=[]
grid_Size=20


#About Platform---------------
# platFormX1=[random(20,100),random(101,180),random(181,260),random(261,320),random(262,400)]
# platFormY1=[random(1200,1001),random(1000,801),random(851,800),random(799,750),random(750,700)]

# platFormX=random(50,650)
# platFormY=700
platFormX=[]
platFormY=[]
platForms=[]
platFormW=70
platFormH=20
platFormUpSpeed=2

#About Warrior----------------
circleX=20
circleY=20
circleRadius=36
circleFallingSpeed=2

#GameScene--------------------
gameState=0
titleState=0
playState=1
gameOverState=2
countDownState=3


startTime=0
usedTime=0

levelNumber=0



def setup():
    size(500,700)
    background(0)
    rectMode(CENTER)
    #background music
   # file=SoundFile(this,"oc.mp3")
   # file.play()


    
    
def draw():
    global platFormUpSpeed,platFormL,platFormW,platFormH
    global circleX,circleY,circleRadius
    background(0)
    

#     platFormX.append(random(width))
#     platFormY.append(random(700))
#     fill(50,50,50)
    
    #Gamestate condition
    if gameState==titleState:
        drawTitleScreen()
    elif gameState==playState:
        drawPlayScreen()
    elif gameState==gameOverState:
        drawGameOverScreen()
    elif gameState==countDownState:
        drawCountDownScreen()
        
        
    for i in range(len(triPos)):
        fill(triColor[i])
        triangle(triPos[i].x,triPos[i].y,(triPos[i].x)-20,(triPos[i].y)-15,triPos[i].x+30,triPos[i].y-50)
        
        
        
def respawn():
    global platForms
    if len(platForms)==0:
    # platFormX.append(width/2)
    # platFormY.append(height+10)
        platForms.append(Platform(width/2,height+10))
    if platForms[len(platForms)-1].posY<height-platFormH:
        print("Yes")
        # platFormY.append(random(700,900))
        # platFormX.append(random(30,430))
        platForms.append(Platform(random(30,430),random(700,900)))
        
    for i in range(len(platForms)):
        platForms[i].posY-=platFormUpSpeed
        platForms[i].dra()
        
        # if platFormY<500:
        #     platFormX.append(random(Width))
        #     platFormX.append(700)
    
    #     fill(50,50,50)
    #     rect(platForms.posX,platForms.posY,platFormW,platFormH)    
    
    # for i in platFormY: 
    #     if platFormY[0]==height-platFormH:
    #         platFormY.append(random(700,900))    
    #         platFormX.append(random(30,770))

#Details for each game state        
def drawTitleScreen():

    textAlign(CENTER)
    textSize(25)
    fill(255)
    text("Enter the",200,height/3)
    textSize(35)
    fill(237,14,14)
    text("Abyss", 310,height/3)
    fill(155,155,155)
    textSize(15)
    text("Press A to rescue ur Fiance!! Hurry!! ", width/2, height/2)
    
def drawPlayScreen():

    global circleX,circleY,circleRadius,gameState,gameOverState
    fill(255)
    triangle(0,0,5,30,10,0)
    
    for i in range(width/10):
    
        triangle(0+i*10,0,5+i*10,30,10+i*10,0)
    # Platform()
    respawn()


    #draw warrior and warrior movement
    circle(circleX,circleY,circleRadius)
    circleY+=circleFallingSpeed
    if circleY>700:
         gameState=gameOverState
         
    if circleY<20:
        gameState=gameOverState
    if keyPressed:
        if key=="A" or key=="a":
            circleX-=2
        
        if key=="S" or key=="s":
            circleY+=2
        if key=="D" or key=="d":
            circleX+=2
        if key=="W" or key=="w":
            circleY-=2
            
    # Collision and Stand on the Platform  
    for i in range(len(platForms)): 
        if circleX>platForms[i].posX-platFormW/2 and circleX<platForms[i].posX+platFormW/2:
            if circleY>platForms[i].posY-platFormH/2 and circleY<platForms[i].posY+platFormH/2:
                circleY=platForms[i].posY
    
    
def drawGameOverScreen():
    textAlign(CENTER)
    fill(250,5,5)
    textSize(20)
    text("You stupid scumbag, get out of my abyss!!!",width/2,height/2)
    text("Press Q to restart if you dare!!", width/2,height/1.7)
    

def drawCountDownScreen():
    global countDown, startTime, gameState
    countDown =3
    ms=millis()
    s=(ms-pms)/1000
    countDown-=s
    
    textAlign(CENTER)
    textSize(128)
    if countDown>=0:
        fill(178,7,7)
        text(countDown,width/2,height/2)
    if countDown<0:
        gameState=playState
        startTime=millis()
        
    
    

# def Platform():
#     global platFormX,platFormY,platFormW,platFormH
#     for i in range(len(platFormX)):
#         platFormY[i]-=platFormUpSpeed
        
#         # if platFormY<500:
#         #     platFormX.append(random(Width))
#         #     platFormX.append(700)
        
#         fill(50,50,50)
#         rect(platFormX[i],platFormY[i],platFormW,platFormH)
#     # platFormY-=platFormUpSpeed
#     # fill(50,50,50)
#     # rect(platFormX[i],platFormY[i],platFormW,platFormH)
    
#     for i in range (len(platFormX1)):
#         platFormY1[i]-=platFormUpSpeed
#         rect(platFormX1[i],platFormY1[i],platFormW,platFormH)
        
        
        
    
        
#Transfer from every game states----------------------------------------------
def keyPressed():
    global gameState,gameOverState,circleY,pms
    
    if key=="A" or key=="a":
        if gameState==titleState:
            gameState=countDownState
            pms=millis()
        
        
    elif gameState==playState:
        if circleY>700:
            gameState=gameOverState
    elif gameState==gameOverState:
        circleY=20
        if key=="Q"or key=="q":
            gameState=titleState


#class------------------------------------------------------------
class Platform:
    def __init__(self,temPosX,temPosY):
        self.posX=temPosX
        self.posY=temPosY
        self.w=platFormW
        self.t=platFormH
         
    def dra(self):
        # for i in range(len(platFormX)):
        #     platFormY[i]-=platFormUpSpeed
            fill(50,50,50)
            rect(self.posX,self.posY,platFormW,platFormH)
        

class SpikePlatform(Platform):
    def __init__(self):
        super().__init__()
        
    def dra(self):
        rectMode(CORNERS)
        for i in range(len(platFormX)):
            platFormY[i]-=platFormUpSpeed
            fill(50,50,50)
            rect(platFormX[i],platFormY[i],platFormW,platFormH)
            triangle(platFormX[i],platFormY[i],platFormX[i]+15,platFormY[i],platFormX[i]+7,platFormY[i]-7)
        


  


    
            
