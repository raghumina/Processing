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


isSound1Playing = False
isSound2Playing = False
isSound3Playing = False
isSound4Playing = False
isSound5Playing = False
isSound6Playing = False


#booleanb = True 



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
    
    
    file1 = SoundFile(this, "Sound001.mp3")
    file2 = SoundFile(this, "Sound002.mp3")
    file3 = SoundFile(this, "Sound003.mp3")
    file4 = SoundFile(this, "Sound004.mp3")
    file5 = SoundFile(this, "Sound005.mp3")
    file6 = SoundFile(this, "Sound006.mp3")
    osc = SqrOsc(this)    
    
    #env = Env(this)
    
    #file2.play()
    #file3.play()
    
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

    fill(255, 0, 0)
    
    if isSound1Playing: 
        fill(0, 255, 0)  
    rect( 50, 500, 55, 55, 7)
    fill(255, 255, 255)
    
    if isSound2Playing: 
        fill(0, 255, 0)  
    rect(150, 500, 55, 55, 7)
    fill(255, 255, 255)
    
    if isSound3Playing: 
        fill(0, 255, 0)  
    rect(250, 500, 55, 55, 7)
    fill(255, 255, 255)
    
    # 4,5,6
    rect(350, 500, 55, 55, 7)
    rect(450, 500, 55, 55, 7)
    rect(550, 500, 55, 55, 7)

    # use the mix buffer to draw the waveforms.
    # because these are MONO files, we could have used the left or right buffers and got the same data
    # bufferSizeP = kick.bufferSize() - 1
    # print("bufferSizeP: " + bufferSizeP)
    for i in xrange(kick.bufferSize()-1):
        line(i, 250 - kick.left.get(i)*50, i+1, 250 - kick.left.get(i+1)*50)

def keyPressed():
    global isSound1Playing, isSound2Playing, isSound3Playing, isSound4Playing, isSound5Playing, isSound6Playing
    global file1, file2, file3, file4, file5, file6 
    
    if key == 'k': 
        kick.trigger()
    if key == '1': 
        isSound1Playing = not isSound1Playing
    if key == '2': 
        isSound2Playing = not isSound2Playing
    if key == '3': 
        isSound3Playing = not isSound3Playing
    if key == '4': 
        isSound4Playing = not isSound4Playing
    if key == '5': 
        isSound5Playing = not isSound5Playing
    if key == '6': 
        isSound6Playing = not isSound6Playing
    
    if isSound1Playing: 
        file1.play()
    else:
        file1.Stop() # stop the music.
        
    if isSound2Playing: 
        file2.play()  
    else:
        file2.Stop()
           
    if isSound3Playing: 
        file3.play() 
    else:
        file3.Stop()
        
        
    if isSound4Playing: 
        file4.play() 
    else:
        file4.Stop()
        
        
    if isSound5Playing: 
        file5.play() 
    else:
        file5.Stop() 
        
    if isSound6Playing: 
        file6.play() 
    else:
        file6.Stop() 
        
         
         
        

    

def stop():
    # always close Minim audio classes when you are done with them
    kick.close()
    minim.stop()   
    
    
    
    
    
    
    
    
    
    
    
