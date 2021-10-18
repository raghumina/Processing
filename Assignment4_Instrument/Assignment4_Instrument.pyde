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

add_library('sound') # This Library provides a simple way to work with audio. It can play, analyze and syntheisize sound.
add_library('minim') #  An audio library that provides easy to use classes for playback, recording, analysis, and synthesis of sound

isReleased = False
NOTE_MAX_SIZE = 100
noteX = []
noteY = []
noteSize = []
attackTime = 0.001
sustainTime = 0.008
sustainLevel = 0.3
releaseTime = 0.4

def setup():
    global file, osc, env
    background(0)
    size(800, 600)
    ellipseMode(CENTER)
    strokeWeight(5)
    
    file = SoundFile(this, "sound1.wav")
    osc = SqrOsc(this)
    env = Env(this)
    
    file.play()
    
def draw():
    global isReleased
    background(0)
    fill(0,0,0,0)
    
    if mousePressed:
        stroke(50)
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
        file.play()
    
    
    
    
    
    
    
    
    
    
    
    
    
