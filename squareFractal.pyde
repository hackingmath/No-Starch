'''Square Fractal
November 12, 2017'''

def setup():
    size(600,600)
    
def draw():
    background(255)
    translate(10,10)
    squareFractal(500,2)
    
def squareFractal(sz,level):
    if level == 0:
        fill(0)
        rect(0,0,sz,sz)
        noFill()
    else:
        pushMatrix()
        squareFractal(sz/2.0,level-1)
        translate(sz/2.0,0)
        squareFractal(sz/2.0,level-1)
        translate(-sz/2.0,sz/2.0,0)
        squareFractal(sz/2.0,level-1)
        #translate(0,-sz/2.0)
        popMatrix()