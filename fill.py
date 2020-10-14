from pygame import *
    
screen = display.set_mode((900,675))

canvasRect = Rect(100,50,400,375)

running =True
screen.fill((255,255,255))

tool = "fill"

color = (123456)



while running:
    click = False
    up = False
    for e in event.get():
        
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:

            click = True
    
    fill_rect = draw.rect(screen,(0),(700,50,50,50),1)

    draw.rect(screen,0,(200,190,90,90),1)

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    draw.rect(screen,(0,0,0), canvasRect,2)
    
    if mb[0]==1 and tool == "pen":
        draw.line(screen, (0,0,0), (omx,omy),(mx,my),1)

    if mb[0] == 1 and fill_rect.collidepoint(mx,my):

        tool = "fill"




    if tool == "fill" and click and canvasRect.collidepoint(mx,my):

        fill_list = []

        oldcolor = screen.get_at((mx, my))

        fill_list.append((mx,my))

        if color != oldcolor:

            while len(fill_list) > 0:

                for i in range(len(fill_list)):

                    cx, cy = fill_list.pop()
                    screen.set_at((cx, cy), color)    #sets a color to a single pixel

                    if screen.get_at((cx+1,cy)) == oldcolor:

                        fill_list.append((cx+1,cy))

                    if screen.get_at((cx-1,cy)) == oldcolor:

                        fill_list.append((cx-1,cy))

                    if screen.get_at((cx,cy+1)) == oldcolor:

                        fill_list.append((cx,cy+1))

                    if screen.get_at((cx,cy-1)) == oldcolor:

                        fill_list.append((cx,cy-1))

    print(tool)



    omx,omy = mx,my    

    screen.set_clip(canvasRect)

    display.flip()

quit()