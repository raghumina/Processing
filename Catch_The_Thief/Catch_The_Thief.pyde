
add_library("sound")  # To play audio in the game


MenuState = 0 # menu
CountdownState = 1
PlayState = 2 # gameplay
GameOverState = 3  # Gameover message, and result 
CurrentState = 0

countdown = 5

# Car Variable
carSpeed = 2
carX1 = 0

def setup():
    global backgroundImage, audio1, policeCar
    size(1500, 900)
    background(0)
    
    audio1 = SoundFile(this,"audio1.mp3")
   # audio1.loop()
    audio1.play()
    backgroundImage = loadImage("gameBackground.png")
    policeCar = loadImage("police.png")
    
    
def draw():
    global backgroundImage, audio1
    drawHUD()

    if CurrentState == 0:
        button()
        drawMenu()
    elif CurrentState == 1:
        drawCountdown()
    elif CurrentState == 2:
        drawPlayState()
    elif CurrentState == 3:
        drawGameOverState()
    
        
def drawHUD():
    global backgroundImage
    ''' 
    Game Area 
    '''
    fill(255)
    rect(10, 10, 1480, 790)
    image(backgroundImage, 10, 10, 1480, 790)

    
def drawMenu():
    global audio1
    #audio1.play()
    fill(255, 100, 100)
    textAlign(CENTER)
    textSize(74)
    text("Welcome to Game",width/2,200)
    
    textAlign(CENTER)
    textSize(64)
    text("Catch_The_Thief",width/2,height/3)
    
    textAlign(CENTER)
    textSize(44)
    text("Please Press R or r to run the game", width/2, 600)

    textSize(30)
    textAlign(LEFT)
    fill(100, 255, 200)
    text("Today's date:" +str(month())+"-"+str(day())+"-"+str(year()),50,50)
        

def button():
    '''
    All these button's are assigned with keys they will not work by clicking on them 
    to do that player have to press specific key's on keyboard
    '''
    
    # Button 1 
    fill(255, 120, 100)
    rect(10, 810, 170, 50, 20)
    fill(0)
    textSize(20)
    stroke(204, 102, 120)
    text("Start Game: R" , 15, 840)
    
    # Button 2 
    fill(255, 120, 100)
    rect(200, 810, 170, 50, 20)
    fill(0)
    textSize(20)
    stroke(204, 102, 120)
    text("Pause Game: P", 210, 840)
    
    # Button 3
    fill(255, 120, 100)
    rect(390, 810, 170, 50, 20)
    fill(0)
    textSize(20)
    stroke(204, 102, 120)
    text("Save Game: S", 400, 840)
    
    # Button 4
    fill(255, 120, 100)
    rect(580, 810, 170, 50, 20)
    fill(0)
    textSize(20)
    stroke(204, 102, 120)
    text("Quit Game Q", 590, 840)
    
    # Car Control 
    # Button 5 
    fill(100, 120, 100)
    rect(820, 810, 190, 50, 20)
    fill(0)
    textSize(20)
    stroke(204, 102, 120)
    text("Start Car: A ", 830, 840)
    
    # Button 6
    fill(100, 120, 100)
    rect(1020, 810, 190, 50, 20)
    fill(0)
    textSize(20)
    stroke(204, 102, 120)
    text("Acclerate Car: SPACE", 1030, 840)
    
    # By default car starts in first gear 
    # Button 7
    fill(100, 120, 100)
    rect(1220, 810, 190, 50, 20)
    fill(0)
    textSize(20)
    stroke(204, 102, 120)
    text(" Gear 1, 2, 3", 1230, 840)
    
def drawCountdown():
  #  countdown = 5
  
    text(countdown - int(second()),50,50)
    
    
def drawPlayState():
    global carSpeed, carX1, CurrentState
    
    car = image(policeCar, carX1, 560)
    
    carAccleration = 4
    if keyPressed:
        if key=="A"or key=="a":
            carX1 += carSpeed
        else:
            if key == "G" or key == "g":    # A or a = accleration
                carSpeed += carAccleration
                carX1 += carSpeed
    print(carX1)
    

    if carX1 >= 1480:
        CurrentState = 3
    

def  drawGameOverState():
    fill(255, 200, 160)
    textAlign(CENTER)
    textSize(74)
    text("Game OVER ",width/2,200)
    
    fill(255, 200, 160)
    textAlign(CENTER)
    textSize(74)
    text("Time Taken ",width/2,500)
    

def keyPressed():
    global CurrentState
    if key == "r" or key == "R":
      
        CurrentState = 2
        print(CurrentState)
        
    
    
    
    
    
    
     
    
    
    
