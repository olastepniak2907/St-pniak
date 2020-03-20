def setup():
    size(500,500)
    rectMode(CORNERS)
def draw():
    #point(200,50)
    #rect(mouseX, mouseY,width/3*2, height/3*2)
    clear()
    if mousePressed:
        rect(50,50,220,200) # wskazane byłoby używać wielkości relatywnych, nie sztywnych
    else:
        circle(100,100,100)
    
#def mouseClicked():
    #clear()
    #circle(100,150,120)
    
1,75pkt
        
