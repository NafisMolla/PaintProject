from random import*
from pygame import*
screen = display.set_mode((1000,900))
running = True


r=1


while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            pic = screen.copy()

            if e.button == 1:
                startx,starty = e.pos                                #related to shape tools

            if e.button == 3:
                startx,starty = e.pos

            if e.button == 4:     #makes radius bigger
                r += 1

            if e.button == 5:     #makes radius smaller
                r -= 1
            

            

    #---------------------------------------

    green = (0,255,0)

    mx,my = mouse.get_pos()


    mb = mouse.get_pressed()

    if r < 0:
        r = 1

   



    if mb[0] == 1 :

        #screen.blit(pic,(0,0))
    

        ellipse_border = Rect(startx,starty,mx-startx,my-starty)

        ellipse_border.normalize()

        surf = Surface(ellipse_border.size).convert()

        surf.set_colorkey((255,255,254))  #sets suface color

        trans = Rect(r,r,(mx-startx)-(2*r),(my-starty)-(2*r))

        trans.normalize()

        

        
        if ellipse_border.height > r *2 and ellipse_border.width > r *2:

            draw.ellipse(surf,green,ellipse_border)
            draw.ellipse(surf,(255,255,254,0),trans)
            screen.blit(surf,(mx,my))
                

        else:
            draw.ellipse(surf,green,ellipse_border)

        




    if mb[1] == 1:
        screen.fill((255,255,255))


    omx, omy = mx,my
#---------------------------------------
    display.flip()
quit()
