
# Changes and addition s
# line 98 = created carAccleration variable 
# Line 102 to 105 ceated a new key condition for accleration 
# You can use these formuls to creatae a gear mechanism for your car 
# only you need is to change variable "carAccleration" name and its value and assign it to a new button 


#Game 235 Dragster style race game
#Payton Jan

add_library("sound")


gameState=0
TITLE_STATE=0
PLAY_STATE=1
GAME_OVER_STATE=2
RESULT=3

stoppedTimes=[]
MAX_TIMES =21

startTime=0

carX1=50
carY1=340
carSpeed=1
carHoldSpeed=3

" new additions"
start = 10


def setup():
    global carX1, file
    size(800,600)
    background(134,197,218)
    textSize(32)
    file=SoundFile(this,"SMTV.mp3")
    file.play()

def draw():
    global carX1,carY1
    #Sky color
    background(134,197,218)
    
    #race rail color
    fill(211,138,47)
    rect(0,300,width,200)
    
    #Audiences Stand color(grass)
    fill(86,125,70)
    rect(0,400,width,400)
    
    #Sun
    fill(245,233,101)
    circle(80,80,100)

    #Winline
    line(700,300,700,400)

  #use these code to determine the state of the game   
    if gameState== TITLE_STATE:
        drawTitleScreen()
    elif gameState==PLAY_STATE:
        drawPlayScreen()
    elif gameState==GAME_OVER_STATE:
        drawGameOverScreen()
    elif gameState==RESULT:
        drawResultScreen()
        
        
#UI and data         
def drawTitleScreen():
     textAlign(CENTER)
     textSize(64)
     text("Super Race Sunshine",width/2,height/3)
     
     textSize(20)
     textAlign(LEFT)
     
     fill(0)
     text("Today's date:" +str(month())+"-"+str(day())+"-"+str(year()),20,20)
     
     textAlign(RIGHT)
     text(str(hour())+":"+nf(minute(),2)+":"+nf(second(),2),width-20,20)
     
     textAlign(CENTER)
     fill(156,212,255)
     text("Press R to Start",width/2,360)
     
def drawPlayScreen():
    global carX1, carY1, carSpeed
    #Car
    car=rect(carX1,carY1,50,20)
    
    carAccleration = 1
    if keyPressed:
        if key=="V"or key=="v":
            carX1 += carSpeed
        else:
            if key == "A" or key == "a":    # A or a = accleration
                carSpeed += carAccleration
                carX1 += carSpeed

    offsetTime=millis()-startTime
    millisString=str(offsetTime/1000)+":"+str(offsetTime/100 - offsetTime/100*10)+":"+nf(offsetTime%100,2)
    textAlign(RIGHT)
    text(millisString,width/2,height/2)
    for time in stoppedTimes:
        time.drawStoppedTime()
        
    # #Win condition            
    if carX1>700:
        Win()
        
def drawGameOverScreen():
    textAlign(CENTER)
    text("Game Over",width/2,height/2)
    
    for time in stoppedTimes:
        time.drawStoppedTime()

def drawResultScreen():

    textAlign(CENTER)
    text("You win", width/2,height/2)
    
    fill(255)
    textSize(50)

def keyPressed():
    global gameState,stoppedTimes,startTime
    
    if key=="R" or key=="r":



        if gameState==TITLE_STATE:
            gameState=PLAY_STATE
        elif gameState==PLAY_STATE:
        
            offsetTime= millis()-startTime
            millisString=str(offsetTime/1000)+":"+str(offsetTime/100 - offsetTime/100*10)+":"+nf(offsetTime%100,2)
            stoppedTimes.append(StoppedTime(PVector(width-10, 30*len(stoppedTimes)+30),millisString))
            if len(stoppedTimes)>=MAX_TIMES:
                gameState=GAME_OVER_STATE
                
        elif gameState==GAME_OVER_STATE:
            gameState=TITLE_STATE
            stoppedTimes=[]   
            

class StoppedTime():
    def __init__(self,temPos,tempString):
        self.pos=temPos
        self.string=tempString
    
    def drawStoppedTime(self):
        textAlign(RIGHT)
      
def Win():
    global carX1   
    drawResultScreen()
    if keyPressed:
        if key=="s" or key== "S":
            carX1=50
   

# 1 point - have a title screen on which pressed a given key to starts the countdown timer  ///  Done
# 3 point - have a countdown timer of some sort (during which pressing the accelerator will result in a false start)
# 1 point - pressing a given key will start moving the player forward  ///Done
# 1 point - the player accelerates the longer they hold down the key
# 1 point - a results screen appears after crossing the finish line or false starting    /// "you win" is in the middle, but the timer is still running
# 2 point - the total travel time (time from the end of the countdown to crossing the finish line)/if the player false started is shown on the results screen
# 1 point - a given key allows the game to restart when on the results screen /// Done
# Extra Credit (2 points) - implement a system of gear shifting or another method of changing the player's speed
# Extra Credit (1 points) - add particles
# Extra Credit (1 points) - sound effects  ///not working 
    
    
    
    
    
    
        
