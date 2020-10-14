#paintProject.py
#Nafis Fardin 
#This is a dragon ballz themed paint prject with the ability to save load, drawing of multiple tools and includes many tools for free hand drawing.

#######################################indvidual features##########################################################################################################

#every tool accept fill and save/load is resizable with the scroll wheel
#theme song of dragon ballz will play while using the program
#pausing and playing can be done with the music
#fixed unfilled rectangle (corners)
#normal spray paint
#dripping spray paint
#polygon tool (closes by itself when close to starting point)
#paint brush with no spacing in between strokes
#fill tool 
#transparent background
#eraser that erases transparent background (texture brush)
#text tool
#undo/redo 
#eyedropper tool
#tk color paltte added for extra precis color options
#save and load allows user to click on drop down area and choose file
#window is always centered on screen


################################################## attention to detail #################################################################################

#Shows the mouse position only within canvas
#Text box that shows thickness of tools
#A text box shows what tool is currently being used
#scrolling or pressing of button will not add to the undo/redo list
#change of mouse cursor type depedning on mouse location(pencil on canvas, Arrow of canvas)
#filled and unfilled versions of all ashape tools (for filled ellipse tool right click when ellipse tool selected)
#tools highlet blue when hoveering on top of them and green when selected
#save and load is done with getname not tk to prevent crashing
#save tool automatically adds .png if file type not specified






#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
from pygame import*
from math import*
from random import*
from text import *
from getname import*
from os import*




#--------------------------------------------------------------------------------

font.init()
comicFont = font.SysFont("Comic Sans MS", 20)                 #text font


#---------------------------------------------------------------------------------
init()
inf = display.Info()
w,h = inf.current_w,inf.current_h
#os.environ['SDL_VIDEO_WINDOW_POS'] = ('300,30')
 

screen = display.set_mode((1024,760))
running = True
#=======================================================================================
drawingspace_1 = Rect(300,30,700,500)  #i just made this so my cursor works

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



arrow = ( "xX                      ",
          "X.X                     ",
          "X..X                    ",
          "X...X                   ",
          "X....X                  ",
          "X.....X                 ",
          "X......X                ",
          "X.......X               ",
          "X........X              ",
          "X.........X             ",
          "X......XXXXX            ",
          "X...X..X                ",
          "X..XX..X                ",
          "X.X XX..X               ",
          "XX   X..X               ",
          "X     X..X              ",
          "      X..X              ",
          "       X..X             ",
          "       X..X             ",
          "        XX              ",
          "                        ",
          "                        ",
          "                        ",
          "                        ")






#=================================================================================

from tkinter import *                
from tkinter.colorchooser import *  # module for colorchooser

root = Tk()             # this initializes the Tk engine
root.withdraw()         # by default the Tk root will show a little window. This
                        # just hides that window



#================================================================================
black  = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
yellow = (255,255,0)
pink = (255,105,180)
gold = (212,175,55)                         #Some frequently used colors
purple = (128,0,128)
orange = (255,165,0)
turquoise = (175,238,238)
grey = (192,192,192)
lightgreen = (144,238,144)


color = black    #pen color

r = 1            #pen size

k = 0

#//////////////////////////////////////////////////////////////////////////////////////////
 
polygon_index = -1
                                         #polygon tool releated lists and index
polygon_cord = []


#//////////////////////////////////////////////////////////////////////////////////////////
background_type = ""
#===========================================================================================
background = image.load("images/dragonballz.jpg")  #dragonballz back ground
background = transform.scale(background,(1024,760))
screen.blit(background,(0,0))


#===========================================================================================
logo = image.load("images/Picture3.png")
logo = transform.scale(logo,(300,100))                      #paint logo
screen.blit(logo,(10,10))

#===============================================================================================


#=====================================================================================

supers = logo = image.load("images/Picture5.png")
#supers = transform.scale(supers,(300,100))             #pic of gokku            #

screen.blit(supers,(50,70))

#=====================================================================================
drawingspace = draw.rect(screen,white,(300,30,700,500))  #canvas
canvas_border = draw.rect(screen,black,(299,29,702,502),1)  #canvas border

drawingspace_sub = Rect(300,30,700,500)   #subsurface for save and load

draw_sub = Surface((700,500),SRCALPHA)     #drawing space sun surface

color_rect = Rect((874,610,140,140))  # imaginary box around color palatte

#======================================================
colorpallate = image.load("images/color-picker.png")
colorpallate=transform.scale(colorpallate,(140,140))           #color picker image
screen.blit(colorpallate,(874,610))

color_pallate_border = draw.rect(screen,orange,(873,608,142,144),2)


#===============================================================
tools_background = Surface((350,500),SRCALPHA)

draw.rect(tools_background,(255,127,80,120),(0,0,190,310))       #orange back ground

screen.blit(tools_background,(20,240))

#===========================================================

pencil_icon = image.load("images/pen.jpg")
pencil_icon = transform.scale(pencil_icon,(50,50))            #bliting and scaling of pencil icon
screen.blit(pencil_icon,(30,250))
draw.rect(screen,black,(30,250,50,50),1)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++

paint_icon = image.load("images/paint-brush.jpg")
paint_icon = transform.scale(paint_icon,(50,50))              #bliting and scaling of paint icon
screen.blit(paint_icon,(90,250))


#+++++++++++++++++++++++++++++++++++++++++++++++++++

eraser_icon = image.load("images/eraser.png")
eraser_icon = transform.scale(eraser_icon,(50,50))              #eraser image
screen.blit(eraser_icon,(30,310))


#++++++++++++++++++++++++++++++++++++++++++++++++++++

airbrush_icon = image.load("images/airbrush.png")
airbrush_icon = transform.scale(airbrush_icon,(50,50))       #airbrush image
screen.blit(airbrush_icon,(90,310))

#++++++++++++++++++++++++++++++++++++++++++++++++++++++

linetool_icon = image.load("images/linetool.png")
linetool_icon = transform.scale(linetool_icon,(50,50))   #linetool
draw.rect(screen,white,(150,250,50,50))           #White box that the picture sits in
screen.blit(linetool_icon,(150,250))

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

rectangle_icon = image.load("images/unfilled-rect.png")      #Rectangle tool pic
rectangle_icon = transform.scale(rectangle_icon,(40,40))
draw.rect(screen,white,(150,310,50,50))    #White box that the picture sits in
screen.blit(rectangle_icon,(155,314))

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

ellipse_icon = image.load("images/ellipse.jpeg")
ellipse_icon = transform.scale(ellipse_icon,(50,50))              #ellipse tool pic
screen.blit(ellipse_icon,(30,370))

#====================================================================================================
stickersbox = draw.rect(screen,white,(400,650,460,100))
stickerborder = draw.rect(screen,black,(398,648,464,104),2)   

#====================================================================================================

polygon_icon = image.load("images/polygon.png")

polygon_icon = transform.scale(polygon_icon,(60,60))                    #polygon tool icons

draw.rect(screen,white,(90,370,50,50))  

screen.blit(polygon_icon,(85,367))        

#=======================================================================================================

fill_icon = image.load("images/fill.png")

fill_icon = transform.scale(fill_icon,(50,50))     #fill tool icon

draw.rect(screen,white,(150,430,50,50))

screen.blit(fill_icon,(150,430))
#====================================================================================================

filled_rect_box = image.load("images/rectangletool.png")
filled_rect_box = transform.scale(filled_rect_box,(50,50))
draw.rect(screen,white,(150,370,50,50))    #White box that the picture sits 
screen.blit(filled_rect_box,(150,370))                                                      #filled rectangletool

#======================================================================================================

drip_spray =  image.load("images/drip.png")
drip_spray = transform.scale(drip_spray,(50,50))
#draw.rect(screen,white,(150,370,50,50))    #White box that the picture sits 
screen.blit(drip_spray,(30,430)) 

#====================================================================================================

eye_dropper = image.load("images/dropper.png")   
eye_dropper = transform.scale(eye_dropper,(48,48))
draw.rect(screen,white,(90,430,50,50))    #White box that the picture sits 
screen.blit(eye_dropper,(90,430))          
#====================================================================================================

text_icon = image.load("images/text.png")

text_icon = transform.scale(text_icon,(40,40))

draw.rect(screen,white,(30,490,50,50))       #text tool pics

screen.blit(text_icon,(33,493))

#===================================================================================================

dragonballz_bottom_logo = image.load("images/dragonlogo3.png")

#dragonballz_bottom_logo = transform.scale(dragonballz_bottom_logo,(80,80))

screen.blit(dragonballz_bottom_logo,(17,680))

#====================================================================================================
#music stuff

mixer.init()
mixer.music.load('music/themmusic.mp3')
mixer.music.play()
stopplay = 0   # flag for stopping and playing

play_icon = image.load('images/pause.png')                        #music pics

play_icon = transform.scale(play_icon,(40,40))

draw.rect(screen,white,(150,490,50,50))

screen.blit(play_icon,(155,495))

#-----------------------------------------------------------------------------------------------------

colored_line = image.load("images/coloredline.png")

colored_line = transform.scale(colored_line,(50,50))         #random line color tool

screen.blit(colored_line,(90,490))




#=====================================================================================================

savesquare = draw.rect(screen,white,(250,690,60,60))                #save and load boxes
save_icon = image.load("images/save-icon.png")
save_icon = transform.scale(save_icon,(50,50))
screen.blit(save_icon,(255,695))

draw.rect(screen,black,(250,690,60,60),2)


loadsquare = draw.rect(screen,white,(320,690,60,60))
load_icon = image.load("images/load-icon.png")
load_icon = transform.scale(load_icon,(50,50))
screen.blit(load_icon,(325,694))
draw.rect(screen,black,(320,690,60,60),2)

#=======================================================================================================

undorect = draw.rect(screen,white,(110,690,60,60))
draw.rect(screen,black,(110,690,60,60),2)
undo_icon = image.load("images/undo-icon.png")
undo_icon = transform.scale(undo_icon,(50,50))
screen.blit(undo_icon,(115,695))



redorect = draw.rect(screen,white,(180,690,60,60))                           #undo redo related things
draw.rect(screen,black,(180,690,60,60),2)
redo_icon = image.load("images/redo.png")
redo_icon = transform.scale(redo_icon,(50,50))
screen.blit(redo_icon,(185,695))

firstpic = screen.subsurface(Rect(300,30,700,500)).copy()

undo = []

redo = []



#=====================================================================================================
tool = "pencil"         #What tool im currently using

stick_tab_tool = "characters"

saveloadtool = ""


#======================================================================================================

#----------------------------------sticker boxes/ lines/ backgrounds------------------------------------------------

#note: dont load images in while loop makes program very slow

# i am loading all my backgrounds here






# ------------------------------------------- TEXT -----------------------------------------------------


draw.rect(screen,orange,(20,210,190,20))

draw.rect(screen,black,(19,209,191,21),1)

comicFont = font.SysFont("Comic Sans MS", 15)                                 #tools text for actual tools
tools_font = comicFont.render("Tools / Shapes", True, (255,0,0))

screen.blit(tools_font,(70,207))

#------------------------------------------------------------------------------------------

tool_text_box = draw.rect(screen,white,(20,600,220,50))

tool_text_box_border = draw.rect(screen,black,(18,598,224,54),2)


text_for_tool = font.SysFont("Comic Sans MS", 20)                                 #tools text for tool text box






#.........................................................................................


canvas_background1 = image.load("images/editedbackground1.jpg")

canvas_background1 = transform.scale(canvas_background1,(700,500))


canvas_background2 = image.load("stickers/toke.png")

canvas_background2 = transform.scale(canvas_background2,(700,500))


canvas_background3 = image.load("stickers/pond.png")

canvas_background3 = transform.scale(canvas_background3,(700,500))




background_sub = background.subsurface((300,30,700,500))   #subsurface for drawing space

#earth_sub = canvas_background1.subsurface((300,30,700,500))



clear_rect = draw.rect(screen,black,(410,665,100,70),1)     #rect for clear background 

earth_rect = draw.rect(screen,black,(520,665,100,70),1)     #rect for earth background

border_b2 = draw.rect(screen,black,(630,665,100,70),1)      #rect for dragon background

border_b3 = draw.rect(screen,black,(740,665,100,70),1)      #rect for pond background



#============================================================================================================


background1 = image.load("images/background(1).png")

background1 = transform.scale(background1,(100,70))





#--------------------------------------------------------------------------

background2 = image.load('stickers/dragonwallpaper.jpeg')

background2 = transform.scale(background2,(100,70))




#---------------------------------------------------------------------------

background3 = image.load('stickers/water.png')

background3 = transform.scale(background3,(100,70))










while running:

    click = False
    up = False
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    for e in event.get():
        
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:

            click = True


            pic = screen.copy()   #takes pic of the screen

            if e.button == 1:
                startx,starty = e.pos                                #related to shape tools

            if e.button == 3:
                startx,starty = e.pos
            #-----------------------------------------------------------------
            if len(polygon_cord) >= 0 and drawingspace.collidepoint(mx,my) and tool == "polygonmaker":
                polygon_index += 1
                polygon_cord.append((mx,my))
                
                

            #---------------------------------------------------------------
            if e.button == 4:     #makes radius bigger
                r += 1

            if e.button == 5:     #makes radius smaller
                r -= 1

        if e.type == MOUSEBUTTONUP:

            if e.button == 1:
                up=True
                if tk_color.collidepoint(mx,my):

                    try:
                
                        color, drawcolorAsString = askcolor(title ='pick your colour.')

                    except:
                        pass

                
                    

        if up and drawingspace.collidepoint(mx,my):
            pic_undo = screen.subsurface(Rect(300,30,700,500)).copy()
            undo.append(pic_undo)
                    





    if r < 0:
        r = 1

    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()

#-----------------------------------------------------------------
    
    if drawingspace_1.collidepoint(mx,my):
        datatuple, masktuple = cursors.compile( pencil_strings,black='.', white='X', xor='o' )
        mouse.set_cursor( (24,24), (0,0), datatuple, masktuple )

    else:
        datatuple, masktuple = cursors.compile( arrow,black='.', white='X', xor='o' )
        mouse.set_cursor( (24,24), (0,0), datatuple, masktuple )


    print(mx,my)





    if mb[0] == 1:
        if color_rect.collidepoint(mx,my):
            screen.set_clip(color_rect)
            color = screen.get_at((mx,my))             #ONly gets color is mouse collides with the color palatte
            screen.blit(colorpallate,(874,610,140,140))
            draw.ellipse(screen,black,(mx-5,my-5,10,10),1)



#-----------------------------------------------------------------
    cord_size = font.SysFont("Comic Sans MS", 13)  
    #screen.blit(background.subsurface(80,544,200,200),(80,544))     #white box for cordinates
    coordinates = cord_size.render("MX: %d,   MY: %d"% (mx,my), True, black )        #cordinates when mouse collides with mouse
    coordinates_else = cord_size.render("MX: ---,    MY: ---", True, black )        #coordinates when mouse not collided with canvas

    draw.rect(screen,white,(20,560,190,20))
    draw.rect(screen,black,(20,560,190,20),2)
    if drawingspace.collidepoint(mx,my):
        screen.blit(coordinates,(70,560))
    else:
        screen.blit(coordinates_else,(75,560))

#====================================================================================================================


    size_box = draw.rect(screen,white,(700,567,140,50))

    draw.rect(screen,black,(700,567,140,50),2)

    pen_size = font.SysFont("Comic Sans MS", 23)

    pen_size_text = pen_size.render("Size: %d"% (r), True, black )

    screen.blit(pen_size_text,(727,575))







#--------------------------------------------------------------------
    pencil = draw.rect(screen,black,(30,250,50,50),1)    #box around pencil icon
    eraser = draw.rect(screen,black,(30,310,50,50),1)    #box around eraser icon
    paint = draw.rect(screen,black,(90,250,50,50),1)    #box around paint icon
    airbrush = draw.rect(screen,black,(90,310,50,50),1) #box around airbrush icon
    linemaker = draw.rect(screen,black,(150,250,50,50),1)          #box around line maker
    rectanglemaker = draw.rect(screen,black,(150,310,50,50),1)     #box around rect maker
    ellipsemaker = draw.rect(screen,black,(30,370,50,50),1)        #box around ellipse maker
    polygonmaker = draw.rect(screen,black,(90,370,50,50),1)
    filledrectmaker = draw.rect(screen,black,(150,370,50,50),1)
    dripspray = draw.rect(screen,black,(30,430,50,50),1)
    eyedropper = draw.rect(screen,black,(90,430,50,50),1)
    canvasfill = draw.rect(screen,black,(150,430,50,50),1)
    textmaker = draw.rect(screen,black,(30,490,50,50),1)
    some_other_tool = draw.rect(screen,black,(90,490,50,50),1)
    musicmaker = draw.rect(screen,black,(150,490,50,50),1)








#----------------------------------------------------------------

    draw.rect(screen,white,(880,556,50,50))

    tk_color_icon = image.load("images/color-icon.png")

    tk_color_icon = transform.scale(tk_color_icon,(40,40))

    screen.blit(tk_color_icon,(885,560))

    tk_color = draw.rect(screen,black,(880,556,50,50),1)

    
    colr_indicator = draw.rect(screen,color,(960,556,50,50))

    if color == (black):
        draw.rect(screen,white,(959,555,52,52),1)

    else:
        draw.rect(screen,black,(959,555,52,52),1)



#----------------------------------------------------------------

    if mb[0] == 1 and pencil.collidepoint(mx,my):
        tool = "pencil"
        
        draw.rect(screen,white,(20,600,220,50))

        text_tool = text_for_tool.render("Pencil Tool", True, (255,0,0))

        screen.blit(text_tool,(70,610))


    if mb[0] == 1 and eraser.collidepoint(mx,my):          #Tool if statements( for collison )
        tool = "eraser"

        draw.rect(screen,white,(20,600,220,50))

        text_tool = text_for_tool.render("Eraser Tool", True, (255,0,0))

        screen.blit(text_tool,(70,610))

    if mb[0] == 1 and paint.collidepoint(mx,my):
        tool = "paint"

        draw.rect(screen,white,(20,600,220,50))

        text_tool = text_for_tool.render("Paint Tool", True, (255,0,0))

        screen.blit(text_tool,(70,610))

    if mb[0] == 1 and airbrush.collidepoint(mx,my):
        tool = "airbrush"

        draw.rect(screen,white,(20,600,220,50))

        text_tool = text_for_tool.render("airbrush Tool", True, (255,0,0))

        screen.blit(text_tool,(70,610))

    if mb[0] == 1 and linemaker.collidepoint(mx,my):
        tool = "linemaker"

        draw.rect(screen,white,(20,600,220,50))

        text_tool = text_for_tool.render("linemaker Tool", True, (255,0,0))

        screen.blit(text_tool,(60,610))

    if mb[0] == 1 and rectanglemaker.collidepoint(mx,my):
        tool = "rectanglemaker"

        draw.rect(screen,white,(20,600,220,50))

        text_tool = text_for_tool.render("Rectangle Tool", True, (255,0,0))

        screen.blit(text_tool,(60,610))

    if mb[0] == 1 and ellipsemaker.collidepoint(mx,my):
        tool = "ellipsemaker"

        draw.rect(screen,white,(20,600,220,50))

        text_tool = text_for_tool.render("Ellipse Tool", True, (255,0,0))

        screen.blit(text_tool,(70,610))

        '''e = font.SysFont("Comic Sans MS", 13)

        text_tool = e.render("Ellipse Tool (Right click for filled)", True, (255,0,0))

        screen.blit(text_tool,(70,610))'''

    if mb[0] == 1 and polygonmaker.collidepoint(mx,my):
        tool = "polygonmaker"

        draw.rect(screen,white,(20,600,220,50))

        text_tool = text_for_tool.render("Polygon Tool", True, (255,0,0))

        screen.blit(text_tool,(70,610))

    if mb[0] == 1 and filledrectmaker.collidepoint(mx,my):
        tool = "filledrectmaker"

        draw.rect(screen,white,(20,600,220,50))

        text_tool = text_for_tool.render("Filled Rectangle Tool", True, (255,0,0))

        screen.blit(text_tool,(30,610))

    if mb[0] == 1 and dripspray.collidepoint(mx,my):
        tool = "dripspray"

        draw.rect(screen,white,(20,600,220,50))

        text_tool = text_for_tool.render("dripspray Tool", True, (255,0,0))

        screen.blit(text_tool,(70,610))

    if mb[0] == 1 and eyedropper.collidepoint(mx,my):
        tool = "eyedropper"

        draw.rect(screen,white,(20,600,220,50))

        text_tool = text_for_tool.render("Eyedropper Tool", True, (255,0,0))

        screen.blit(text_tool,(60,610))

    if mb[0] == 1 and canvasfill.collidepoint(mx,my):
        tool = "canvasfill"

        draw.rect(screen,white,(20,600,220,50))

        text_tool = text_for_tool.render("Fill Tool", True, (255,0,0))

        screen.blit(text_tool,(70,610))

    if mb[0] == 1 and textmaker.collidepoint(mx,my):
        tool = "textmaker"

        draw.rect(screen,white,(20,600,220,50))

        text_tool = text_for_tool.render("Text Tool", True, (255,0,0))

        screen.blit(text_tool,(70,610))

    if mb[0] == 1 and some_other_tool.collidepoint(mx,my):
        tool = "some_other_tool"

        draw.rect(screen,white,(20,600,220,50))

        text_tool = text_for_tool.render("Random Line Tool", True, (255,0,0))

        screen.blit(text_tool,(40,610))



    if mb[0] == 1 and tk_color.collidepoint(mx,my):

        draw.rect(screen,white,(20,600,220,50))

        color_tool = text_for_tool.render("Color palatte", True, (255,0,0))

        screen.blit(color_tool,(40,610))


    

#//////////////////////////////////////////////////////////////////////////////////////////////////////


    if click and musicmaker.collidepoint(mx,my):               #music player 
        stopplay += 1

        if stopplay % 2 == 1:
            mixer.music.pause()

        elif stopplay % 2 == 0:
            mixer.music.play()






#-----------------------------------------------------------------------
    if tool == "pencil":
        draw.rect(screen,green,pencil,1)

        draw.rect(screen,white,(20,600,220,50))

        text_tool = text_for_tool.render("Pencil Tool", True, (255,0,0))

        screen.blit(text_tool,(70,610))
    
    if tool == "eraser":
        draw.rect(screen,green,eraser,1)
    
    if tool == "paint":
        draw.rect(screen,green,paint,1)
    
    if tool == "airbrush":
        draw.rect(screen,green,airbrush,1)

    if tool == "linemaker":
        draw.rect(screen,green,linemaker,1)

    if tool == "rectanglemaker":
        draw.rect(screen,green,rectanglemaker,1)
    
    if tool == "ellipsemaker":
        draw.rect(screen,green,ellipsemaker,1)

    if tool == "polygonmaker":
        draw.rect(screen,green,polygonmaker,1)

    if tool == "tkcolormaker":
        draw.rect(screen,green,tk_color,1)

    if tool == "filledrectmaker":
        draw.rect(screen,green,filledrectmaker,1)

    if tool == "dripspray":
        draw.rect(screen,green,dripspray,1) 

    if tool == "eyedropper":
        draw.rect(screen,green,eyedropper,1)
    
    if tool == "canvasfill":
        draw.rect(screen,green,canvasfill,1)

    if tool == "textmaker":
        draw.rect(screen,green,textmaker,1)

    if tool == "some_other_tool":
        draw.rect(screen,green,some_other_tool,1) 






#----------------------------------------------------------------------

    if eraser.collidepoint(mx,my):
        draw.rect(screen,blue,(30,310,50,50),1)             
    
    if pencil.collidepoint(mx,my):
        draw.rect(screen,blue,(30,250,50,50),1)

    if paint.collidepoint(mx,my):
        draw.rect(screen,blue,(90,250,50,50),1)            #makes tools turn blue when mouse collides with it

    if airbrush.collidepoint(mx,my):
        draw.rect(screen,blue,(90,310,50,50),1)

    if linemaker.collidepoint(mx,my):
        draw.rect(screen,blue,(150,250,50,50),1)

    if rectanglemaker.collidepoint(mx,my):
        draw.rect(screen,blue,(150,310,50,50),1)

    if ellipsemaker.collidepoint(mx,my):
        draw.rect(screen,blue,(30,370,50,50),1)

    if polygonmaker.collidepoint(mx,my):
        draw.rect(screen,blue,(90,370,50,50),1)

    if tk_color.collidepoint(mx,my):
        draw.rect(screen,blue,(880,556,50,50),1)

    if filledrectmaker.collidepoint(mx,my):
        draw.rect(screen,blue,(150,370,50,50),1)

    if dripspray.collidepoint(mx,my):
        draw.rect(screen,blue,(30,430,50,50),1)

    if eyedropper.collidepoint(mx,my):
        draw.rect(screen,blue,(90,430,50,50),1)

    if canvasfill.collidepoint(mx,my):
        draw.rect(screen,blue,(150,430,50,50),1)

    if textmaker.collidepoint(mx,my):
        draw.rect(screen,blue,(30,490,50,50),1)

    if musicmaker.collidepoint(mx,my):
        draw.rect(screen,blue,(150,490,50,50),1)

    if some_other_tool.collidepoint(mx,my):
        draw.rect(screen,blue,(90,490,50,50),1)







#----------------------------------------------------------------


    if mb[0] == 1 and drawingspace.collidepoint(mx,my):

        screen.set_clip(drawingspace)

        if tool == "pencil":
            draw.line(screen,color,(omx,omy),(mx,my),1)    #draws pencil lines


        if tool == "eraser":
            x = mx-omx

            y = my-omy

            d = hypot(x,y)

            if d == 0:
                d = 1




            ex = max(mx,drawingspace.x+r)

            ex = min(mx,drawingspace.right-r)

            ey = max(my,drawingspace.y-r)

            ey = min(my,drawingspace.bottom+r)





            for i in range(int(d)):

                sx = int(omx+i/d*x)
                sy = int(omy+i/d*y)          #similar trinagles relationship for eraser


                if background_type == "":
                
                    draw.rect(screen,white,(sx-(3+r)/2, sy - (3+r)/2, 3+r,3+r))

                

                if background_type == "clear":

                    sample = background.subsurface(Rect(ex,ey,r,r))
                    screen.blit(sample,(ex,ey))

                    clear_eraser = Surface((500,500),SRCALPHA)
                    draw.rect(clear_eraser,(135,206,250,120),(0,0,r,r))                   
                    screen.blit(clear_eraser,(ex,ey))



                if background_type == "background1":

                    sample = canvas_background1.subsurface(ex,ey,r,r)
                    screen.blit(sample,(ex,ey))




        if tool == "paint":


            x = mx-omx

            y = my-omy

            d = hypot(x,y)

            if d == 0:
                d = 1


            for i in range(int(d)):

                sx = int(omx+i/d*x)
                sy = int(omy+i/d*y)          #similar trinagles relationship for paint


                draw.circle(screen,color,(sx,sy),3+r)



        if tool == "airbrush":
            for x in range(0,10):
                air_x = randint(-40+(-1*r),40+r)
                air_y = randint(-40+(-1*r),40+r)

                if air_x**2+air_y**2<=(40+r)**2:
                    draw.circle(screen,color,(mx+air_x,my+air_y),0)

        if tool == "linemaker":
            screen.blit(pic,(0,0))
            draw.line(screen,color,(startx,starty),(mx,my),r)

        if tool == "rectanglemaker":
            screen.blit(pic,(0,0))
            draw.rect(screen,color,(startx,starty,mx-startx,my-starty),1+r)

            draw.rect(screen, color, (startx - r // 2, starty - r // 2, r, r))  #filling in the four squares in each corner
            draw.rect(screen, color, (mx - r // 2 , my - r // 2 , r, r))
            draw.rect(screen, color, (mx - r // 2 , starty - r // 2, r, r))
            draw.rect(screen, color, (startx - r // 2, my - r // 2 , r,r))

        if tool == "ellipsemaker":

            screen.blit(pic,(0,0))

            ellipse_border = Rect(startx,starty,mx-startx,my-starty)

            ellipse_border.normalize()

            if ellipse_border.height > r *2 and ellipse_border.width > r *2:

                draw.ellipse(screen,color,ellipse_border,r)


            else:
                draw.ellipse(screen,color,ellipse_border)


        if tool == "filledrectmaker":
            screen.blit(pic,(0,0))
            draw.rect(screen,color,(startx,starty,mx-startx,my-starty))


        if tool == "dripspray":

                bx = randint(-20+(-1*r),20+r)
                by = randint(-20+(-1*r),20+r)

                for i in range (15):
                    if bx**2 + by**2 <= (20+r)**2:
                        for x in range(0,4):
                            while drawingspace.collidepoint(mx+bx,my+by):
                                z = screen.get_at((mx+bx,my+by))
                                if z == color:
                                    by += 1
                                else:
                                    break
                            for x in range(0,100):
                                draw.circle(screen,color,(mx+bx,my+by),0)


        if tool == "canvasfill":


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

                        if screen.get_at((cx-1,cy)) == oldcolor:   #cheeks every color around and finds all the non-color pixels

                            fill_list.append((cx-1,cy))

                        if screen.get_at((cx,cy+1)) == oldcolor:

                            fill_list.append((cx,cy+1))

                        if screen.get_at((cx,cy-1)) == oldcolor:

                            fill_list.append((cx,cy-1))


        if tool == "some_other_tool":
            screen.blit(pic,(0,0))
            draw.line(screen,randint(0,16777215),(startx,starty),(mx,my),r)
#===================================================================================================================================



        srx = 30+r*10  #sticker size variables

        sry = 30+r*10
        
        if tool == "c1":

            
            screen.blit(pic,(0,0))

            c1_1 = image.load('images/picture1.png')

            c1_1 = transform.scale(c1_1,(srx,sry+30))

            screen.blit(c1_1,(mx-srx/2,my-sry/2))


        if tool == "c2":

            screen.blit(pic,(0,0))

            c2_1 = image.load('stickers/gohan.png')

            c2_1 = transform.scale(c2_1,(srx,sry+30))

            screen.blit(c2_1,(mx-srx/2,my-sry/2))

        if tool == "c3":

            screen.blit(pic,(0,0))

            c3_1 = image.load('stickers/vegeta.png')

            c3_1 = transform.scale(c3_1,(srx,sry+30))  #'stickers/vegeta.png'  'stickers/master.png'   'stickers/picilo.png'

            screen.blit(c3_1,(mx-srx/2,my-sry/2))


        if tool == "c4":

            screen.blit(pic,(0,0))

            c4_1 = image.load('stickers/master.png')

            c4_1 = transform.scale(c4_1,(srx,sry+10))

            screen.blit(c4_1,(mx-srx/2,my-sry/2))

        if tool == "c5":

            screen.blit(pic,(0,0))

            c5_1 = image.load('stickers/picilo1.png')

            c5_1 = transform.scale(c5_1,(srx,sry+30))

            screen.blit(c5_1,(mx-srx/2,my-sry/2))


        if tool == "i1":
            screen.blit(pic,(0,0))    #'stickers/meter.png'  'stickers/cloud.png'  'stickers/armour.png'  'stickers/dragonlogo.png'

            i1_1 = image.load('stickers/meter.png')

            i1_1 = transform.scale(i1_1,(srx,sry))

            screen.blit(i1_1,(mx-srx/2,my-sry/2))

        if tool == "i2":
            screen.blit(pic,(0,0))    

            i2_1 = image.load('stickers/cloud.png')

            i2_1 = transform.scale(i2_1,(srx+30,sry))

            screen.blit(i2_1,(mx-srx/2,my-sry/2))


        if tool == "i3":
            screen.blit(pic,(0,0))    

            i3_1 = image.load('stickers/armour.png')

            i3_1 = transform.scale(i3_1,(srx,sry+40))

            screen.blit(i3_1,(mx-srx/2,my-sry/2))


        if tool == "i4":
            screen.blit(pic,(0,0))    

            i4_1 = image.load('stickers/dragonlogo.png')

            i4_1 = transform.scale(i4_1,(srx,sry))

            screen.blit(i4_1,(mx-srx/2,my-sry/2))










    if tool == "eyedropper" and click:

        color = screen.get_at((mx,my))



    if tool == "polygonmaker" and drawingspace.collidepoint(mx,my):
        
        if len(polygon_cord) >= 1: #will crash if not greater or equal to one
            screen.blit(pic,(0,0))

            draw.line(screen,color,polygon_cord[polygon_index],(mx,my),r)

            polstartx, polstarty = polygon_cord[0]   #starting positon for polygon tool

            close_rect = Rect(polstartx-10,polstarty-30,60,60)   #closes polygon if in the rect

            if close_rect.collidepoint(mx,my) and len(polygon_cord) >= 3:
                draw.line(screen,color,polygon_cord[polygon_index], polygon_cord[0],1)
                mouse.set_pos([polstartx,polstarty])
            
            if (mx,my) == (polstartx,polstarty) and mb[0] == 1:
                polygon_index = -1
                polygon_cord = []                                         #resets the variables when the shape closes
                
            


        


    if tool == "textmaker" and drawingspace.collidepoint(mx,my) and click:
        txt = gettext(screen,False,mx,my)                     # this is how you would call my getName function
                                                # your main loop will stop looping until user hits enter
        txtPic = comicFont.render(txt, True, (color))
        screen.blit(txtPic,(mx,my))


    



#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



    if mb[2] == 1 and drawingspace.collidepoint(mx,my):

        screen.set_clip(drawingspace)



        if tool == "ellipsemaker":

            screen.blit(pic,(0,0))

            ellipse_border = Rect(startx,starty,mx-startx,my-starty)

            ellipse_border.normalize()

            
            draw.ellipse(screen,color,ellipse_border)

    


#------------------------------------------------------------------------------------------------------------------------
    #----------------------------------sticker boxes/ lines------------------------------------------------



    


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#back ground blitting


#----------------------------------------------------------------------------------------------
    if click and clear_rect.collidepoint(mx,my) and stick_tab_tool == "backgrounds":

        screen.blit(background_sub,(300,30))

        t_background = Surface((1000,1000),SRCALPHA)

        draw.rect(t_background,(135,206,250,120),(0,0,700,500))       #orange back ground

        clear_background_sticker = screen.blit(t_background,(300,30))

        background_type = "clear"   #used for type of eraser


    if click and earth_rect.collidepoint(mx,my) and stick_tab_tool == "backgrounds":

        #canvas_background1 = image.load("images/editedbackground1.jpg")

        #canvas_background1 = transform.scale(canvas_background1,(700,500))

        screen.blit(canvas_background1,(300,30))

        background_type = "background1"

    if click and border_b2.collidepoint(mx,my) and stick_tab_tool == "backgrounds":

        screen.blit(canvas_background2,(300,30))

        background_type = "background2"

    if click and border_b3.collidepoint(mx,my) and stick_tab_tool == "backgrounds":

        screen.blit(canvas_background3,(300,30))

        background_type = "background3" 



#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#sticker tool selection if statemetns

    if click and stick_tab_tool == "characters":

        if c1.collidepoint(mx,my):
            tool = "c1"

        if c2.collidepoint(mx,my):
            tool = "c2"

        if c3.collidepoint(mx,my):
            tool = "c3"

        if c4.collidepoint(mx,my):
            tool = "c4"

        if c5.collidepoint(mx,my):
            tool = "c5"


    #----------------------------------------------------------------------------------------

    if click and stick_tab_tool == "items":

        if i1.collidepoint(mx,my):
            tool = "i1"
        if i2.collidepoint(mx,my):
            tool = "i2"

        if i3.collidepoint(mx,my):
            tool = "i3"

        if i4.collidepoint(mx,my):
            tool = "i4"











#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    rect_1_box = draw.rect(screen,grey,(403,619,70,30))
    rect_1_box_border = draw.rect(screen,orange,(402,619,72,31),1)
    draw.line(screen,grey,(402,649),(474,649),1)



  
#----------------------------------------------------------------------------------------------

    rect_2_box = draw.rect(screen,grey,(490,619,70,30))
    rect_2_box_border = draw.rect(screen,orange,(489,619,72,31),1)
    draw.line(screen,grey,(489,649),(561,649),1)

#----------------------------------------------------------------------------------------------

    rect_3_box = draw.rect(screen,grey,(577,619,70,31))
    rect_3_box_border = draw.rect(screen,orange,(576,619,72,31),1)
    draw.line(screen,grey,(577,649),(649,649),1)


#------------------------------------------------------------------------------------------------------

    if click and rect_1_box.collidepoint(mx,my):
        stick_tab_tool = "characters"

    if click and rect_2_box.collidepoint(mx,my):
        stick_tab_tool = "items"

    if click and rect_3_box.collidepoint(mx,my):
        stick_tab_tool = "backgrounds"

    
    if stick_tab_tool == "characters":
        points_rect_1 = ((403,649),(403,619),(473,619),(473,649))
        draw.rect(screen,white,(403,619,70,30))
        draw.polygon(screen,orange,points_rect_1,1)
        draw.line(screen,white,(403,649),(473,649),1)
        draw.rect(screen,white,(400,650,460,100))

        #-------------------------------------------------------------

        character_1 = image.load('images/picture1.png')

        #character_1 = transform.scale(character_1,(60,60))

        screen.blit(character_1,(410,660))

        c1 = Rect((410,660,50,90))

        #--------------------------------------------------------------

        character_2 = image.load('stickers/gohan.png')
        screen.blit(character_2,(490,663))

        c2 = Rect((500,663,50,80))

        #---------------------------------------------------------------  

        character_3 = image.load('stickers/vegeta.png')

        screen.blit(character_3,(590,658))

        c3 = Rect((590,658,50,90))

        #-------------------------------------------------------------------

        character_4 = image.load('stickers/master.png')

        screen.blit(character_4,(675,655))

        c4 = Rect((675,655,76,95))

        #--------------------------------------------------------------------

        character_5 = image.load('stickers/picilo.png')

        screen.blit(character_5,(770,655))

        c5 = Rect((770,655,70,95))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
    #loading and blitting of sticker previews

    if stick_tab_tool == "items":
        draw.rect(screen,white,(490,619,70,30))
        draw.rect(screen,orange,(489,618,72,32),1)
        draw.line(screen,white,(489,649),(561,649),1)
        draw.rect(screen,white,(400,650,460,100))

        #-----------------------------------------------------------

        item_1 = image.load('stickers/meter.png')   

        screen.blit(item_1,(410,660))

        i1 = Rect((410,680,80,40))

        #------------------------------------------------------------

        item_2 = image.load('stickers/cloud.png')

        screen.blit(item_2,(520,680))

        i2 = Rect((520,680,80,55))

        #---------------------------------------------------------------

        item_3 = image.load('stickers/armour.png')

        screen.blit(item_3,(640,588))

        i3 = Rect((640,650,80,100))

        #---------------------------------------------------------------

        item_4 = image.load('stickers/dragonlogo.png')

        screen.blit(item_4,(750,650))

        i4 = Rect((750,660,90,80))


        

#/////////////////////////////////////////////////////////////////////////////
    if stick_tab_tool == "backgrounds":
        draw.rect(screen,white,(577,619,70,30))
        draw.rect(screen,orange,(576,618,72,32),1)
        draw.line(screen,white,(577,649),(649,649),1)
        draw.rect(screen,white,(400,650,460,100))
             


        clear_background = Surface((350,500),SRCALPHA)

        draw.rect(clear_background,(135,206,250,120),(0,0,100,70))       #orange back ground

        screen.blit(clear_background,(410,665))    

        clear_rect = draw.rect(screen,black,(410,665,100,70),1)

        #-----------------------------------------------------


        screen.blit(background1,(520,665))

        draw.rect(screen,black,(520,665,100,70),1)    #rect for earth background


        #--------------------------------------------------------------------------


        screen.blit(background2,(630,665))

        draw.rect(screen,black,(630,665,100,70),1)

        

        #---------------------------------------------------------------------------

        screen.blit(background3,(740,665))

        draw.rect(screen,black,(740,665,100,70),1)

        



#============================== text for sticker tabs ======================================

    comicFont_stickers = font.SysFont("Comic Sans MS", 12)                                 #character text
    characters_font = comicFont_stickers.render("Characters", True, (0,0,0))

    screen.blit(characters_font,(407,626))

#--------------------------------------------------------------------------------------------------

    items_font = comicFont_stickers.render("Items", True, (0,0,0))

    screen.blit(items_font,(502,626))

#---------------------------------------------------------------------------------

    backgrounds_font = comicFont_stickers.render("Backgrounds", True, (0,0,0))

    screen.blit(backgrounds_font,(576,626))



#----------------------------------------------------------------------------------------------
    



    if click and savesquare.collidepoint(mx,my):

        saveloadtool = "save"

    if saveloadtool == "save":

        userinput = getName(screen,True)  #gets the users input using the getname function

        if "." not in userinput:

            userinput = userinput + ".png"

        if userinput > ".png" and userinput > ".jpg":  #this if statement makes it so saveing works if the user actually eneters a file name

            try:


                image.save(screen.subsurface(drawingspace_sub),userinput)               #reseting the tool makes it so the user can get out of the save function 

                screen.set_clip(drawingspace_sub)

                saveloadtool = ""

            except:
                pass
                saveloadtool = ""




    if click  and loadsquare.collidepoint(mx,my):

        saveloadtool = "load"

        if saveloadtool == "load":


            userinput = getName(screen,True)

            if userinput > "":

                try:

                    load_image = image.load(userinput)

                    load_image = transform.scale(load_image,(700,500))

                    screen.blit(load_image,(300,30))


                    saveloadtool = ""


                except:
                    pass
                    saveloadtool = ""


#------------------------------------------------------
#undo redo 

    if len(undo) == 0:
        undo.append(firstpic)

    

    if click and drawingspace.collidepoint(mx,my):
        redo = []


    if click and undorect.collidepoint(mx,my) and len(undo) >= 1:
        try:
            screen.blit(undo[-2],(300,30))
            redo.append(undo[-1])
            del(undo[-1])

        except:
            pass
            screen.blit(firstpic,(300,30))


    if click and redorect.collidepoint(mx,my) and len(redo) >= 1:
        screen.blit(redo[-1],(300,30))
        undo.append(redo[-1])
        del(redo[-1])


#----------------------------------------------------------------------------------------------------------------------

    screen.set_clip(None)



    omx,omy = mx,my    #mouse old positon

    display.flip()

font.quit()
del comicFont
quit()
