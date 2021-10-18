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



def setup():
    background(0)
    size(800, 600)
    ellipseMode(CENTER)
    strokeWeight(5)
    
    file = SoundFile(this, 
