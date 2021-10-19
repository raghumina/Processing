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



#### Note ####
# This program may give runtime error or insufficient error to resolve that error please close or quit the ongoing programs
# on your computer 
# Also it may takes some time to run to please have patience while waiting for run
# 
# These problems are due to size of the audio files and little memory used by processing to process the code and run it.







# This program is a audio visualizer program which plays and visualizes the given audio samples 
# It visualizes the audio sample frequency which result in linear wave form on the canvas
# To use this audio visualizer you have to run the program(Which may take some time as the program consist big audio files
#  -and processing need more time and memory to process and run them).
# Once the canvas get opend it show 6 buttons on footer of the canvas.
# Each button is assigned to a specific audio file. when pressed on that button the button changes the color to green and 
# and starts playing the sound. we have to press number keys on the keyboard "1", "2", "3", "4", "5", "6". for audio's samples 
# to stop the playing audio we have to click same number key. then it will stop and we can move to another sound by clicking
# another number key on the keyboard.
                                                        
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

# I Didn't used sound library in this program

screenWidth = 650
screenHeight = 600


isSound1Playing = False
isSound2Playing = False
isSound3Playing = False
isSound4Playing = False
isSound5Playing = False
isSound6Playing = False



def setup():
    global file1, file2, file3, file4, file5, file6, f
    global minim, player, kick1, kick2, kick3, kick4, kick5, kick6
    background(0)
    size(screenWidth, screenHeight)
    ellipseMode(CENTER)
    strokeWeight(4)
    f = createFont("Arial", 30)


    # 
    minim = Minim(this)
    kick1 = minim.loadSample("Sound001.mp3", 650)
    kick2 = minim.loadSample("Sound002.mp3", 650)
    kick3 = minim.loadSample("Sound003.mp3", 650)
    kick4 = minim.loadSample("Sound004.mp3", 650)
    kick5 = minim.loadSample("Sound005.mp3", 650)
    kick6 = minim.loadSample("Sound006.mp3", 650)
    
    file1 = SoundFile(this, "Sound001.mp3")
    file2 = SoundFile(this, "Sound002.mp3")
    file3 = SoundFile(this, "Sound003.mp3")
    file4 = SoundFile(this, "Sound004.mp3")
    file5 = SoundFile(this, "Sound005.mp3")
    file6 = SoundFile(this, "Sound006.mp3")
   

#
def draw():
    global f
    background(0)
    
    textFont(f,16)            
    fill(255)                       
    text("Audio Visualizer",screenWidth/2,screenHeight/2)
    
    stroke(255, 0, 0)
    
    # This conditional statements are for the button color when inactive they will appear white.
    #when active they will appear green 
    if isSound1Playing: 
        fill(0, 255, 0)  
    rect( 50, 500, 55, 55, 7)
    fill(255, 255, 255)
    
 #   fill(255, 0, 0)
    if isSound2Playing: 
        fill(0, 255, 0)  
    rect(150, 500, 55, 55, 7)
    fill(255, 255, 255)
    
    if isSound3Playing: 
        fill(0, 255, 0)  
    rect(250, 500, 55, 55, 7)
    fill(255, 255, 255)
    
    # 4
    if isSound4Playing: 
        fill(0, 255, 0)
    rect(350, 500, 55, 55, 7)
    fill(255, 255, 255)
    
    if isSound5Playing: 
        fill(0, 255, 0)
    rect(450, 500, 55, 55, 7)
    fill(255, 255, 255)
    
    
    if isSound6Playing: 
        fill(0, 255, 0)
    rect(550, 500, 55, 55, 7)
    fill(255, 255, 255)
    
    
    # use the mix buffer to draw the waveforms.
    # because these are MONO files, we could have used the left or right buffers and got the same data
    # bufferSizeP = kick.bufferSize() - 1
    # print("bufferSizeP: " + bufferSizeP)
    if isSound1Playing:
        for i in xrange(kick1.bufferSize()-1):
            line(i, 100 - kick1.left.get(i)*50, i+1, 100 - kick1.left.get(i+1)*50)
            
    if isSound2Playing:
        for i in xrange(kick2.bufferSize()-1):
            line(i, 100 - kick2.left.get(i)*50, i+1, 100 - kick2.left.get(i+1)*50)        

    if isSound3Playing:
        for i in xrange(kick3.bufferSize()-1):
            line(i, 100 - kick3.left.get(i)*50, i+1, 100 - kick3.left.get(i+1)*50) 
            
    if isSound4Playing:
        for i in xrange(kick4.bufferSize()-1):
            line(i, 100 - kick4.left.get(i)*50, i+1, 100 - kick4.left.get(i+1)*50) 
            
    if isSound5Playing:
        for i in xrange(kick5.bufferSize()-1):
            line(i, 100 - kick5.left.get(i)*50, i+1, 100 - kick5.left.get(i+1)*50) 
            
    if isSound6Playing:
        for i in xrange(kick6.bufferSize()-1):
            line(i, 100 - kick6.left.get(i)*50, i+1, 100 - kick6.left.get(i+1)*50) 
            

# This function allows user to give the input to the computer that Hey I want to play this sound001 and and I want to stop it 
# It takes both play and stop input from the user and gives output according to it.
def keyPressed():
    global isSound1Playing, isSound2Playing, isSound3Playing, isSound4Playing, isSound5Playing, isSound6Playing
    global minim, file1, file2, file3, file4, file5, file6, kick1, kick2, kick3, kick4, kick5, kick6 
    
   # if key == 'k': 
   #     kick.trigger()
    if key == '1': 
        isSound1Playing = not isSound1Playing
        stop()
     #   kick1.trigger()
    if key == '2': 
        isSound2Playing = not isSound2Playing
        stop()
     #   kick2.trigger()
    if key == '3': 
        isSound3Playing = not isSound3Playing
        stop()
    if key == '4': 
        isSound4Playing = not isSound4Playing
        stop()
    if key == '5': 
        isSound5Playing = not isSound5Playing
        stop()
    if key == '6': 
        isSound6Playing = not isSound6Playing
        stop()
    
    if isSound1Playing: 
        file1.play()    
        kick1.trigger()
    else:
        file1.stop() # stop the music.
        
    if isSound2Playing: 
        file2.play() 
        kick2.trigger()
    else:
        file2.stop()

           
    if isSound3Playing: 
        file3.play()
        kick3.trigger()
    else:
        file3.stop()
        
        
    if isSound4Playing: 
        file4.play() 
        kick4.trigger()
    else:
        file4.stop()
        
        
    if isSound5Playing: 
        file5.play() 
        kick5.trigger()
    else:
        file5.stop() 
        
    if isSound6Playing: 
        file6.play()
        kick6.trigger() 
    else:
        file6.stop() 
        
# This function works when we again press same number key to stop the playing audio file 
# It activates the stop keyword to stop the ongonig process
def stop():
    # always close Minim audio classes when you are done with them
    kick1.stop()
    kick2.stop()
    kick3.stop()
    kick4.stop()
    kick5.stop()
    kick6.stop()
   # minim.stop()   
    
    
    
    
    
    
    
    
    
    
    
