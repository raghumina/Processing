# Raghu Mina
# GAME-235-50 Game Developmnt 1 
# Instructor - Zac Emerzian

# Assignment 4: Create a musical instrument/soundboard/audio visualizer.

# Grading Ruberic
#3 points - describe how to use/play your instrument in comments at the top of your code
#5 points - use at least 5 sounds (through audio files, audio waves, or sound envelopes)
#2 points - have a visual component that changes depending on what sounds are playing
#Extra Credit (1 point) - use more than 5 sounds
#Extra Credit (1 point) - add more interesting controls than simply "press some key to play the sound"

# Lets Start 


# Source: https://www.fesliyanstudios.com
# Sound1 = Sound001.mp3  
# Sound2 = Sound002.mp3
# Sound3 = Sound003.mp3
# Sound4 = Sound004.mp3
# Sound5 = Sound005.mp3
# Sound6 = Sound006.mp3


add_library('sound') # This Library provides a simple way to work with audio. It can play, analyze and syntheisize sound.
add_library('minim') #  An audio library that provides easy to use classes for playback, recording, analysis, and synthesis of sound

isReleased = False
NOTE_MAX_SIZE = 500
noteX = []
noteY = []
noteSize = []
attackTime = 1
sustainTime = 5
sustainLevel = 8
releaseTime = 10


hudOffsetX = 0 
hudOffsetY = 200

screenWidth = 800
screenHeight = 600


booleanb = True 



def setup():
    global file1, file2, file3, file4, file5, file6, osc, env
    global minim, player, kick
    background(0)
    size(screenWidth, screenHeight)
    ellipseMode(CENTER)
    strokeWeight(4)
    f = createFont("Arial", 30)
    
    minim = Minim(this)
    kick = minim.loadSample("Sound001.mp3")
    
    
   # file1 = SoundFile(this, "Sound001.mp3")
    file2 = SoundFile(this, "Sound002.mp3")
    file3 = SoundFile(this, "Sound003.mp3")
    file4 = SoundFile(this, "Sound004.mp3")
    file5 = SoundFile(this, "Sound005.mp3")
    file6 = SoundFile(this, "Sound006.mp3")
    osc = SqrOsc(this)
    
    
    env = Env(this)
    
    file2.play()
    file3.play()
    
# New Function HuD for the buttones and slide bar to control audio.    

def drawHuD():
    global screenWidth, screenHeight
    global hudOffsetX, hudoffsetY, f
    
    
''' 

    
def draw():
    global isReleased
    background(0)
    fill(0,0,0,0)
    
    if mousePressed:
        stroke(0, 0, 255)
        circle(mouseX, mouseY, 40)
        isReleased = True
        
    elif isReleased:
        osc.play()
        osc.freq(mouseX + 100)
        env.play(osc, attackTime, sustainTime, sustainLevel, releaseTime)
        
        noteX.append(mouseX)
        noteY.append(mouseY)
        noteSize.append(5)
        
        isReleased = 5
        
    for i in range(len(noteX)):
        noteSize[i] += 1
        stroke(50, 50, 255, 255 * (NOTE_MAX_SIZE - noteSize[i])/ float(NOTE_MAX_SIZE))
        
        circle(noteX[i], noteY[i], noteSize[i])
        
def keyPressed():
    if key =="w" or key == "W":
        file2.play()

 '''
def draw():
    background(100)
    stroke(255)

    
    
    rect(50, 500, 55, 55, 7)
    rect(150, 500, 55, 55, 7)
    rect(250, 500, 55, 55, 7)
    rect(350, 500, 55, 55, 7)
    rect(450, 500, 55, 55, 7)
    rect(550, 500, 55, 55, 7)

    # use the mix buffer to draw the waveforms.
    # because these are MONO files, we could have used the left or right buffers and got the same data
    for i in xrange(kick.bufferSize()-1):
        line(i, 250 - kick.left.get(i)*50, i+1, 250 - kick.left.get(i+1)*50)

def keyPressed():
    if key == 'k': kick.trigger()

def stop():
    # always close Minim audio classes when you are done with them
    kick.close()
    minim.stop()   
    
    
    
    
    
    
    
    
    
    
    
