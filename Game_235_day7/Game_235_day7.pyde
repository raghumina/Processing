# Day 7 
# Games 235 
# Class work

def setup():
    size(700, 500)
    background(120, 120, 255)
    textSize(32)
    
def draw():
    background(255, 120, 120)
    text(str(myMax(mouseX, mouseY)), 20, 50)
    
def myBoolean():
    return False

def myMax(par1, par2):
    if par1 > par2:
        return par1
    else:
        return par2
    

    
