def setup(): 
    size(200, 200)
    global pg
    pg = createGraphics(100, 100)

def draw(): 
    background(204)
    pg.beginDraw()
    pg.stroke(0, 102, 153)
    pg.line(0, 0, mouseX, mouseY)
    pg.endDraw()
    image(pg, 50, 50)

# Click to clear the PGraphics object
def mousePressed(): 
    pg.clear()
