from random import*
from pygame import*
screen = display.set_mode((1000,900))
running = True







polygon = []

index = -1

tool = "pol"









while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            pic = screen.copy()
            if len(polygon) >= 0:
                polygon.append((mx,my))

                index+=1

                tool = "p"





    #---------------------------------------

    green = (0,255,0)

    mx,my = mouse.get_pos()




    mb = mouse.get_pressed()

    



    if tool == "p":

        
        screen.blit(pic,(0,0))

        draw.line(screen,green,polygon[index],(mx,my),1)

        startx, starty = polygon[0]

        close_rect = Rect(startx-10,starty-30,60,60)

        if close_rect.collidepoint(mx,my) and len(polygon) >= 3:
            draw.line(screen,green,polygon[index], polygon[0],1)
            mouse.set_pos([startx,starty])
            
            if (mx,my) == (startx,starty) and mb[0] == 1:
                index = -1
                polygon = []
                tool = "pol"

        




    if mb[1] == 1:
        screen.fill((0,0,0))


    omx, omy = mx,my
#---------------------------------------
    display.flip()
quit()