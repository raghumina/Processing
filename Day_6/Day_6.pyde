# Sound Demo 

add_library("sound")

isReleased = False
NOTE_MAX_SIZE = 100
NoteX = []
NoteY = []
noteSize = []
attackTime = 0.001
sustainTime = 0.008
sustainLevel = 0.3
releaseTime = 0.4


def setup():
    global file, osc, env
    size(600, 400)
    background(0)
    file = SoundFile(this, "sound.mp3")
    osc = SqrOsc(this,)
    env = Env(this)
    
    
    
    
    
    file.play()
    
    
def draw():
    global isReleased
    background(0)
    fill(0,0,0,0)
    circle(mouseX, mouseY, 20)
   # file = SoundFile(this, "sound.mp3")
    #file.play()
    
    if mousePressed:
        stroke(50)
        circle(mouseX, mouseY, 50)
        isReleased = True
    elif isReleased:
        osc.play()
        osc.freq(mouseX + 100)
        env.play(osc, attackTime, sustainTime, sustainLevel, releaseTime)
        
        NoteX.append(mouseX)
        NoteY.append(mouseY)
        noteSize.append(5)
        
    for i in range(len(NoteX)):
        noteSize[i] += 1
        stroke(50, 50, 255)
        square(NoteX[i], NoteY[i], noteSize[i])
    
def keyPressed():
    if key == "w" or key == "W":
        print("you pressed w")
        file.play()
        # sound playing code below 
        
