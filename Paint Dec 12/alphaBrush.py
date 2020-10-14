'''
alphaBrush.py
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

eraserHead = Surface((100,100),SRCALPHA)                  # make blank Surface
draw.rect(eraserHead,(255,255,0,44),(0,0,40,40),2)     # draw using alpha
brushHead = Surface((20,20),SRCALPHA)       
draw.circle(brushHead,(0,111,0,44),(10,10),10)

running =True
mx,my = 0,0
screen.fill((255,255,255))
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    
    mb = mouse.get_pressed()
    omx,omy = mx,my
    mx,my = mouse.get_pos()

    if mx!=omx or my!=omy:
        if mb[0]==1:
            screen.blit(brushHead, (mx-10,my-10))       # this is where it uses the alpha
        if mb[2]==1:
            screen.blit(eraserHead, (mx-20,my-20))

    display.flip()

quit()
