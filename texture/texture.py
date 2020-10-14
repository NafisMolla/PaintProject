# Mr. McKenzie
# texture.py
# simple example to demonstrate the use of subsurface
from pygame import *
    
screen = display.set_mode((800,600))

# This section is so slow that I could use a real loading screen here.
# I load a few pictures to be used to grab parts of for painting.
picnames = ["brick.jpg","dirt.jpg","dry-dirt.jpg","sky.jpg","grass.jpg"]
textures = []
for name in picnames:
    pic = image.load(name)
    textures.append(pic)

canvasRect = Rect(100,50,600,500)               # draw my basic layout
screen.fill((255,170,200))                      # 
draw.rect(screen,(255,255,255),canvasRect)
draw.rect(screen,(0,0,0),canvasRect,2)

mx,my = 0,0         # need this because my omx,omy crashes if mx,my do not have values
pos = 0             # position in my texture list
screen.blit(textures[pos].subsurface((0,0,50,50)),(25,50)) # draw texture preview
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            n = len(textures)
            if e.button == 4:
                pos = (pos+1) % n
            if e.button == 5:
                pos = (pos+n-1) % n     # redraw texture preview-it could have changed
            screen.blit(textures[pos].subsurface((0,0,50,50)),(25,50)) 
            
    mb = mouse.get_pressed()
    omx,omy = mx,my
    mx,my = mouse.get_pos()
    
    if canvasRect.collidepoint(mx,my):
        pixelCol = screen.get_at((mx,my))
        draw.rect(screen,pixelCol,(25,90,50,50))
        if mb[0]==1:
            draw.line(screen,(0,0,0),(omx,omy),(mx,my),2)
        if mb[2]==1:                    # grab a small part of the texture from my list
                                        # and blit it on the screen.
            sample = textures[pos].subsurface((mx,my,40,40))
            screen.blit(sample,(mx-20,my-20))

    display.flip()

quit()
