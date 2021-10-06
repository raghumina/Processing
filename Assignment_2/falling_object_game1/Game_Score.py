
add_library("sound")

def setup():
    global sf
    size(200,200)
    # Load sound file, you provide, put in data/
    sf = SoundFile(this,"pop.wav")

def draw():
    pass

def mouseClicked():
    # Play sound when mouse clicked on canvas.
    sf.play()
