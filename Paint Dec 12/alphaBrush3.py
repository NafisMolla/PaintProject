'''
alphaBrush3.py
Mr. McKenzie
-----------------------
Colour in Python is actually RGBA. The A is the alpha. It controls
how transparent/opaque the colour is (0 = transparent, 255 = opaque.)
These values are only used when you blit a surface onto the screen. So,
if I want to draw a partially transparent circle I draw this circle to
a blank Surface then I blit this Surface to the screen.
'''

from pygame import *
    
screen = display.set_mode((1200,675))

cover = Surface((50,50)).convert()                  # make blank Surface
cover.set_alpha(5)
cover.fill((255,0,255)) 
cover.set_colorkey((255,0,255))
draw.circle(cover,(255,0,0),(25,25),24)

running =True
mx,my = 0,0
screen.fill((255,255,255))
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
                       
    
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    if mb[0]==1:
        screen.blit(cover,(mx-25,my-25))



    display.flip()

quit()
