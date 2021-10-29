'''
MID TERM
QUESTION 2 
Mystery_things.txt

Raghu Mina]
10/27/2021







This code creates a canvas divided equally divided into 2 parts on y axis upper half in blue shade and lower half in green.
with each time mouse pressed on lower side it creates multiple plants with yellow colored petals on it of two predefined sizes.
so the new plant numbers and sizes are random in between given criteria.
In easy words this program creates a scene with plants whenever mouse pressed on defined area.
'''


MAX_NUMBER_THINGS = 10
# HINT: Look below at these two global constant names
MIN_THING_PETAL_RADIUS = 25   # smaller petal length variable with defined petal length 
MAX_THING_PETAL_RADIUS = 70   # bigger petla length vatialbe with defined petal length 

numberThings = 0
# all list variables to store the data 
startThingsX = []
startThingsY = []
currentThingsX = []
currentThingsY = []
targetThingsX = []
targetThingsY = []
currentThingsRadius = []
targetThingsRadius = []

'''
Below is an example for how you should explain what the code does for each function:
     
This function sets the size of the application to 600px wide by 400px tall, 
and then sets the location from which rectangles are drawn to the center.
'''

def setup():
    size(600, 400)
    rectMode(CENTER)

'''
This function sets the bckground color, after proceeding that ir will update the canvas them it wills draws the ground,
fill color in it giving it the half size of the canvas 

In easy words it will draw a rectange half of the size of application and fills color in it 
'''
def draw():
    # This is very soft blue
    background(134, 197, 218)
    
    # First we update everything
    updateMysteryThings()
    
    # Then we draw everything
    # HINT: draws the ground
    pushStyle()
    rectMode(CORNER)
    # This is the color lawn green
    fill(86, 125, 70)
    rect(0, height/2, width, height/2)
    popStyle()

    drawMysteryThings()



# This function creates and dissapears images when user pressed mouse in specific area 

def mousePressed():
    if(mouseY > height/2):
        # defined are create and remove things only after this citeria is met
        if(mouseX > width * 0.25 and mouseX < width * 0.75): # area where mouse should be pressed 
            removeThings()  # Remove plants
            createThings(mouseX, mouseY)  # again creates plants
            
'''
This function comes into play when mouse pressed 
As defined in def mousePressed(): function
Removes all the variables that are mentiones below 
which are helping in creating the plants with petals 
so it removes them from the canvas so that after removed and mouse pressed again a new set of plants can imerge.
'''
def removeThings():
    global numberThings, startThingsX, startThingsY, currentThingsX, currentThingsY, targetThingsX, targetThingsY, currentThingsRadius, targetThingsRadius
    
    numberThings = 0
    startThingsX = []
    startThingsY = []
    currentThingsX = []
    currentThingsY = []
    targetThingsX = []
    targetThingsY = []
    currentThingsRadius = []
    targetThingsRadius = []

'''
This function create plants in in a specific range. 
Range defined in MAX_NUMBER_THINGS variable.
and creates the plant in random number 
the size will be random between max and min as provided by programmer 
'''
def createThings(x, y):
    global numberThings
    
    numberThings = int(random(MAX_NUMBER_THINGS))
    
    # This condition creates the plants with specific specification 
    for i in range(numberThings):
        createThing(x + random(-width/4, width/4), y)

'''
This function comes into play after mouse is pressed on the specific area for the first time or after removel of plants.
It again creates new plants with all that available global variables.
'''

def createThing(x, y):
    global numberThings, startThingsX, startThingsY, currentThingsX, currentThingsY, targetThingsX, targetThingsY, currentThingsRadius, targetThingsRadius

    startThingsX.append(x)
    startThingsY.append(y)
    currentThingsX.append(x)
    currentThingsY.append(y)
    targetThingsX.append(x)
    targetThingsY.append(y - random(20, height/2))  # random height variable to create plant with diff heights 
    currentThingsRadius.append(0)
    targetThingsRadius.append(random(MIN_THING_PETAL_RADIUS, MAX_THING_PETAL_RADIUS))  # for random size of plant petals 


# This function updates the animation the appearence of the plant 
# first the appearnce of stem, the petals on them
def updateMysteryThings():
    global currentThingsY
    
    for i in range(len(startThingsX)):
        if(not animationComplete(i)):
            currentThingsY[i] -= 1
        else:
            doOtherThing(i)


# This function it complewtes the animation if it completes its good if mouse pressed them removes them from screen 
def animationComplete(index):
    if(currentThingsY[index] <= targetThingsY[index]):
        return True
    
    return False


# This function check the radius of the plant petals
def doOtherThing(index):
    global currentThingsRadius
    
    if(currentThingsRadius[index] <= targetThingsRadius[index]):
        currentThingsRadius[index] += 2
        

# This function draws the pant petal and stems and keeps updating the list

def drawMysteryThings():
    for i in range(numberThings): # number of plants in the given range 
        if(animationComplete(i)): 
            pushStyle()
            # This is yellow
            fill(255, 255, 0)  # color od petal
            # This is gray
            stroke(128)  # oulinr color of petal
            circle(currentThingsX[i], currentThingsY[i], currentThingsRadius[i])  # shape of petal
            popStyle()  # to update the list 

        # HINT: Draws the stem
        pushStyle()
        # This is the color black
        fill(0)
        # This is also the color black
        stroke(0)
        # small ellipse with black color on stem line
        ellipse(currentThingsX[i], currentThingsY[i], 10, 10)  
        # stem in shape of line with black color
        line(startThingsX[i], startThingsY[i], currentThingsX[i], currentThingsY[i])
        popStyle() 
