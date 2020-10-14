# pygameRev1.py
from pygame import *

init()
size = width, height = 800, 600
green = 0, 255, 0
red = 255, 0, 0
screen = display.set_mode(size)

pencil_strings = (            #sized 24x24
      "X                       ",
      "XXX                     ",
      "XX.XX                   ",
      "XX...XX                 ",
      "XX.....XX               ",
      "XX.....XXX              ",
      "XX..XXX...X             ",
      " XXX......X             ",
      " X...X.....X            ",
      "  X...X.....X           ",
      "  X...X.....X           ",
      "   X...X.....X          ",
      "   X...X.....X          ",
      "    X...X.....X         ",
      "    X...X.....X         ",
      "     X...X.....X        ",
      "     X...X.....X        ",
      "      X...X.....X       ",
      "      X...X.....X       ",
      "       X...X...XXX      ",
      "       X...XXXXX        ",
      "        XXXX            ",
      "                        ",
      "                        ")

datatuple, masktuple = cursors.compile( thickarrow_strings,black='.', white='X', xor='o' )
datatuple, masktuple = cursors.compile( pencil_strings,black='.', white='X', xor='o' )
mouse.set_cursor( (24,24), (0,0), datatuple, masktuple )

running = True
mx,my = 0,0
screen.fill((111,111,111))
while running:
    for evnt in event.get():                # checks all events that happen
        if evnt.type == QUIT:
            running = False

    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()

    if mb[0]==1:
        draw.circle(screen, green, (mx,my),4)

    display.flip()
                       
    
quit()
