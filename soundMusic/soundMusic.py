from pygame import *

def running():
    for evt in event.get():
        if evt.type == QUIT:
            return False
    return True

def pattern(mx,my):
    c = mx*255/800
    draw.circle(screen,(c,c,c), (mx,my), 20)
    
init()
screen = display.set_mode((800,600))
fireSound = mixer.Sound("laser.wav")
mixer.music.load("Ambianica.mp3")
mixer.music.play()
        
while running():
    mb = mouse.get_pressed()
    mxy = mouse.get_pos()

    if mb[0] == 1:
        fireSound.play()
        pattern(mxy[0],mxy[1])
    if mb[2] == 1:
        screen.fill((0,0,0))
    display.flip()

quit()
