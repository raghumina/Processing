
add_library("sound")  # To play audio in the game


GameState = 0 # menue, title 
PlayState = 1 # gameplay
GameOver = 2 # Gameover message, and result 


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
    drawMenu()
    button()
    
def drawHUD():
    global backgroundImage
    ''' 
    Game Area 
    '''
    fill(255)
    rect(10, 10, 1480, 790)
    image(backgroundImage, 10, 10, 1480, 790)
    image(policeCar, mouseX, mouseY)
    
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
    rect(10, 810, 170, 50)
    fill(0)
    textSize(25)
    stroke(204, 102, 120)
    text("Start Game" , 15, 840)
    
    # Button 2 
    fill(255, 120, 100)
    rect(200, 810, 170, 50)
    fill(0)
    textSize(25)
    stroke(204, 102, 120)
    text("Pause Game", 210, 840)
    
    # Button 3
    fill(255, 120, 100)
    rect(390, 810, 170, 50)
    fill(0)
    textSize(25)
    stroke(204, 102, 120)
    text("Save Game", 400, 840)
    
    # Button 4
    fill(255, 120, 100)
    rect(580, 810, 170, 50)
    fill(0)
    textSize(25)
    stroke(204, 102, 120)
    text("Quit Game", 590, 840)
    
    # Car Control 
    # Button 5 
    fill(100, 120, 100)
    rect(820, 810, 190, 50)
    fill(0)
    textSize(25)
    stroke(204, 102, 120)
    text("Start Car", 830, 840)
    
    # Button 6
    fill(100, 120, 100)
    rect(1020, 810, 190, 50)
    fill(0)
    textSize(25)
    stroke(204, 102, 120)
    text("Acclerate Car", 1030, 840)
    
    # By default car starts in first gear 
    # Button 7
    fill(100, 120, 100)
    rect(1220, 810, 190, 50)
    fill(0)
    textSize(25)
    stroke(204, 102, 120)
    text(" Gear 1, 2, 3", 1230, 840)
    
    
def keyPressed():
    if key == "r" or key == "R":
        pass
        
    
    
    
    
    
    
     
    
    
    
