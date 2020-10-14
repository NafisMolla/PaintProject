from random import*
from pygame import*
screen = display.set_mode((1000,900))
running = True
screen.fill((255,255,255))

r=8


while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            pic = screen.copy()

            if e.button == 1:
                startx,starty = e.pos 
                y = abs(my-starty)                               #related to shape tools

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


    #y = abs(my-starty)

   
   



    if mb[0] == 1 :

        screen.blit(pic,(0,0))
        draw.rect(screen,green,(startx,starty,mx-startx,my-starty),1+r)

        
        draw.rect(screen, green, (startx - r // 2, starty - r // 2, r, r))
        draw.rect(screen, green, (mx - r // 2 , my - r // 2 , r, r))
        draw.rect(screen, green, (mx - r // 2 , starty - r // 2, r, r))
        draw.rect(screen, green, (startx - r // 2, my - r // 2 , r,r))

        
            

        





        

        


     

    

    

        




    if mb[1] == 1:
        screen.fill((255,255,255))


    omx, omy = mx,my

    
#---------------------------------------
    display.flip()
    
quit()

