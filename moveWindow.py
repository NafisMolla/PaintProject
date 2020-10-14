from pygame import *
import os

init()
inf = display.Info()
w,h = inf.current_w,inf.current_h
os.environ['SDL_VIDEO_WINDOW_POS'] = '25,25'

screen = display.set_mode((w-50,h-50),NOFRAME) 

for x in range(0,screen.get_width(),10):
    draw.line(screen, (0, 0, 255), (x,0), (x,screen.get_height()))  

display.flip()         

time.wait(3000)         
quit()  
