add_library('minim')

def setup():
    size(700, 600)
     # always start Minim before you do anything with it
    global minim, player
    minim = Minim(this)
    global kick
     # load BD.mp3 from the data folder with a 1024 sample buffer
    kick = minim.loadSample("Sound001.mp3")
     # load BD.mp3 from the data folder, with a 512 sample buffer
     #kick = minim.loadSample("BD.mp3", 2048)

def draw():
    global minim, player, kick
    background(0)
    stroke(0,0,255)
     # use the mix buffer to draw the waveforms.
     # because these are MONO files, we could have used the left or right buffers and got the same data
    for i in xrange(kick.bufferSize()-1):
        line(i, 100 - kick.left.get(i)*50, i+1, 100 - kick.left.get(i+1)*50)

def keyPressed():
    if key == 'k': kick.trigger()

def stop():
     # always close Minim audio classes when you are done with them
    kick.close()
